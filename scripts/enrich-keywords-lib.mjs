// Shared keyword enrichment logic for both batch and per-file entrypoints.
// Backend is GitHub Models (gpt-4o-mini) via fetch. Generates synonyms /
// related search terms from a dataset's title + notes, grounded in its
// existing canonical tags so synonyms expand around the taxonomy rather
// than inventing parallel vocabulary. Idempotent — files already containing
// `keywords:` are skipped.

import { readFileSync, writeFileSync } from 'fs'

const ENDPOINT = 'https://models.inference.ai.azure.com'
const MODEL = 'gpt-4o-mini'

export async function enrichDataset (filePath, { token } = {}) {
  const githubToken = token || process.env.GITHUB_TOKEN
  if (!githubToken) {
    throw new Error('GITHUB_TOKEN is required.')
  }

  const parsed = readDatasetForEnrichment(filePath)
  if (!parsed) return

  const { title, notes, tags } = parsed
  const keywords = await fetchKeywordsViaGitHubModels({ title, notes, tags, token: githubToken })
  if (!keywords) return

  writeKeywords(filePath, keywords)
}

// Read + validate a dataset file. Returns null (and logs SKIP) when the file
// is already enriched, has no frontmatter, or has no title.
export function readDatasetForEnrichment (filePath) {
  const raw = readFileSync(filePath, 'utf8')

  if (/^keywords:/m.test(raw)) {
    console.log(`SKIP (already has keywords): ${filePath}`)
    return null
  }

  const frontmatterMatch = raw.match(/^---\r?\n([\s\S]*?)\r?\n---/)
  if (!frontmatterMatch) {
    console.log(`SKIP (no frontmatter): ${filePath}`)
    return null
  }

  const fm = frontmatterMatch[1]
  const titleMatch = fm.match(/^title:\s*(.+)$/m)
  const title = titleMatch ? titleMatch[1].trim().replace(/^['"]|['"]$/g, '') : ''
  if (!title) {
    console.log(`SKIP (no title): ${filePath}`)
    return null
  }

  return {
    raw,
    title,
    notes: extractNotes(fm),
    tags: extractTags(fm)
  }
}

export function writeKeywords (filePath, keywords) {
  const raw = readFileSync(filePath, 'utf8')
  const keywordsYaml = `keywords:\n${keywords.map(k => `- ${k}`).join('\n')}\n`
  const closingIdx = raw.search(/\n---(\r?\n|$)/)
  if (closingIdx === -1) {
    console.error(`ERROR: could not find closing --- in ${filePath}`)
    return
  }
  const updated = raw.slice(0, closingIdx + 1) + keywordsYaml + raw.slice(closingIdx + 1)
  writeFileSync(filePath, updated, 'utf8')
  console.log(`ENRICHED: ${filePath} → [${keywords.join(', ')}]`)
}

// Stops at the next top-level YAML key so short `notes:` fields don't pull in
// garbage from neighboring frontmatter into the prompt.
function extractNotes (frontmatter) {
  const lines = frontmatter.split(/\r?\n/)
  const startIdx = lines.findIndex(l => /^notes:/.test(l))
  if (startIdx === -1) return ''

  const collected = [lines[startIdx].replace(/^notes:\s*/, '')]
  for (let i = startIdx + 1; i < lines.length; i++) {
    if (/^\w[\w-]*:/.test(lines[i])) break
    collected.push(lines[i])
  }
  return collected.join(' ').replace(/^['"\s]+|['"\s]+$/g, '').slice(0, 500)
}

// Pulls the canonical tag list out of frontmatter. Supports block, inline,
// and same-line YAML tag styles.
function extractTags (frontmatter) {
  const block = frontmatter.match(/^tags:\s*\n((?:[ \t]*-[ \t]+[^\n]+\n?)+)/m)
  if (block) {
    return [...block[1].matchAll(/^[ \t]*-[ \t]+(.+?)[ \t]*$/gm)]
      .map(m => m[1].replace(/^['"]|['"]$/g, ''))
      .filter(Boolean)
  }
  const inline = frontmatter.match(/^tags:\s*\[([^\]]*)\]/m)
  if (inline) {
    return inline[1].split(',').map(t => t.trim().replace(/^['"]|['"]$/g, '')).filter(Boolean)
  }
  const sameLine = frontmatter.match(/^tags:\s+([^\[\n]+)$/m)
  if (sameLine) {
    return sameLine[1].split(',').map(t => t.trim()).filter(Boolean)
  }
  return []
}

// Tag-grounded prompt. The LLM is told to expand around existing canonical
// tags so the keyword vocabulary reinforces (rather than competes with) the
// browseable taxonomy.
export function buildPrompt ({ title, notes, tags }) {
  const tagLine = tags && tags.length
    ? `Existing tags (controlled vocabulary): ${tags.join(', ')}`
    : 'Existing tags: (none)'

  return `Generate 5 to 10 lowercase keyword synonyms and related search terms for this open data dataset. Expand around the existing tags — include synonyms, related concepts, and natural-language terms a user might type to find this dataset. Order from most to least relevant. Return ONLY a JSON array of strings, no markdown fences.

Title: ${title}
Description: ${notes || '(none)'}
${tagLine}

Example: ["permits", "construction", "zoning"]`
}

export function parseKeywords (text, label) {
  if (!text) {
    console.error(`ERROR: no response (${label})`)
    return null
  }
  try {
    const cleaned = text.trim().replace(/^```json?\n?/, '').replace(/\n?```$/, '')
    const keywords = JSON.parse(cleaned)
    if (!Array.isArray(keywords)) throw new Error('not an array')
    return keywords
  } catch {
    console.error(`ERROR parsing response (${label}): ${text}`)
    return null
  }
}

async function fetchKeywordsViaGitHubModels ({ title, notes, tags, token }) {
  const response = await fetch(`${ENDPOINT}/chat/completions`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      model: MODEL,
      messages: [{ role: 'user', content: buildPrompt({ title, notes, tags }) }],
      max_tokens: 200
    })
  })

  const data = await response.json()
  return parseKeywords(data.choices?.[0]?.message?.content, title)
}
