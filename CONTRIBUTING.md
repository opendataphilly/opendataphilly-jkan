
## How to Contribute
- Take a look at our [issues](https://github.com/azavea/opendataphilly-jkan/issues) to get started. Additionally there are [good first issues](https://github.com/azavea/opendataphilly-jkan/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) for newcomers to get acquainted with the codebase.
- Workflows for forking repository and creating pull requests:
    - [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository)
    - [Create a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)
- Our policy is that contributors can use whatever tools they would like to craft their contributions, but there must be a human in the loop. Contributors must read and review all AI (Artificial Intelligence) / Large Language Model (LLM)-generated code or text before they ask other project members to review it. The contributor is always the author and is fully accountable for their contributions. Contributors should be sufficiently confident that the contribution is high enough quality that asking for a review is a good use of scarce maintainer time, and they should be able to answer questions about their work during review.

- For additional JKAN architecture information, please see the [Architecture](https://github.com/opendataphilly/opendataphilly-jkan/blob/main/docs/architecture.md) page in the docs.

## Tags and Keywords

Datasets carry two distinct vocabularies, maintained separately:

- **`tags:`** — a curated, controlled vocabulary used for browse/filter on the site. The canonical set lives in [`_data/tags.yml`](_data/tags.yml), and the raw → canonical mapping that normalizes tags found in dataset files lives in [`scripts/tag_normalization.yml`](scripts/tag_normalization.yml). To add or rename a canonical tag, edit **both** files, then run `python scripts/normalize_tags.py` to rewrite every `_datasets/*.md` to match. See the header comments in `tag_normalization.yml` for details.
- **`keywords:`** — synonyms and natural-language search terms generated automatically. On every push to `main` that touches `_datasets/**`, the [`enrich-keywords` workflow](.github/workflows/enrich-keywords.yml) runs against changed files and opens a follow-up PR titled `chore: auto-enrich keywords for changed datasets`. **Review and merge this PR like any other** — it's not skipped or auto-merged. Files that already have a `keywords:` field are skipped, so editing keywords by hand will stick.
