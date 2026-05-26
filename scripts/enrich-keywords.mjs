#!/usr/bin/env node
// Batch-enriches all _datasets/*.md files with a `keywords` field using the GitHub Models API.
// Run: GITHUB_TOKEN=<your-token> node scripts/enrich-keywords.mjs
// Idempotent: skips files that already have a `keywords` field.

import { readdirSync } from 'fs'
import { join, resolve, dirname } from 'path'
import { fileURLToPath } from 'url'
import { enrichDataset } from './enrich-keywords-lib.mjs'

const __dirname = dirname(fileURLToPath(import.meta.url))
const DATASETS_DIR = resolve(__dirname, '../_datasets')

if (!process.env.GITHUB_TOKEN) {
  console.error('ERROR: GITHUB_TOKEN environment variable is required.')
  process.exit(1)
}

async function main () {
  const files = readdirSync(DATASETS_DIR)
    .filter(f => f.endsWith('.md'))
    .map(f => join(DATASETS_DIR, f))

  console.log(`Processing ${files.length} dataset files...`)

  for (const file of files) {
    try {
      await enrichDataset(file)
      await new Promise(r => setTimeout(r, 200))
    } catch (err) {
      console.error(`ERROR processing ${file}:`, err.message)
    }
  }

  console.log('Done.')
}

main()
