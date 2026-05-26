#!/usr/bin/env node
// Enriches a single _datasets/*.md file with a `keywords` field using the GitHub Models API.
// Called by the enrich-keywords GHA workflow on push to main.
// Usage: GITHUB_TOKEN=... node scripts/enrich-keywords-gh.mjs _datasets/foo.md

import { resolve } from 'path'
import { enrichDataset } from './enrich-keywords-lib.mjs'

async function main () {
  const filePath = resolve(process.argv[2])
  if (!filePath.endsWith('.md')) {
    console.log(`SKIP (not a markdown file): ${filePath}`)
    return
  }

  if (!process.env.GITHUB_TOKEN) {
    console.error('ERROR: GITHUB_TOKEN environment variable is required.')
    process.exit(1)
  }

  await enrichDataset(filePath)
}

main()
