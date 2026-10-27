# Status

Stage 0 research candidate. This page records what the repository supports today. It does not mark a [hard gate](GLOSSARY.md#hard-gates) passed. Checked 27 October 2026.

## What is true today

- One maintainer is listed in [MAINTAINERS.md](MAINTAINERS.md). Outside seats are empty until someone agrees.
- The eight governance hard gates default to NOT MET. The sample input is named as hypothetical. Its replenishment-ratio line can read PASSED. That line is the point rubric, not the eight gates. The sample does not supply gate evidence, so the eight gates stay NOT MET.
- Solidity and Aiken reference contracts were removed with the `contracts/` directory. They are not a current artifact. There is no `LICENSE-CODE` file. Code is Apache-2.0. Documentation is CC-BY-4.0.
- GitHub Pages is published from [docs/index.html](docs/index.html) at <https://lf-decentralized-trust-labs.github.io/os-frontiers/>. There is no `site/` directory.
- The Intersect POSM accelerator never launched. It was only described as intent in the scope of work. Notes about retainers in [VALIDATION.md](VALIDATION.md) are not a Stage 2 pass.
- The evaluator version is `0.8.0-rc.1`, the same string as the existing tag. It is not published to PyPI or npm.

## Validation stages

| Piece | Stage | Why it is not further along |
|---|---|---|
| dOSPO, OMF, ORF | Stage 0 | No independent review is recorded in this repository. |
| QUAID adapter | Stage 0 | Heuristic only. Continuous integration reads a saved fixture. |
| Reference contracts | Removed | Not restored. |

## Tooling

- Tests cover the 15 indicators, the level boundaries in the point rubric, and the eight gates.
- [evaluator/schema/sample_input_config.schema.json](evaluator/schema/sample_input_config.schema.json) describes the sample input.
- [evaluator/pyproject.toml](evaluator/pyproject.toml) and [evaluator/cli/package.json](evaluator/cli/package.json) both say `0.8.0-rc.1`. The command is `os-frontiers-assess`. `--version` prints that string.
- [evaluator/docs/CHAOSS_MAPPING.md](evaluator/docs/CHAOSS_MAPPING.md) cites CHAOSS pages and marks weak mappings.
- Pull-request CI checks DCO sign-off on the commits in the pull request and fails when one is missing. Markdown lint covers the front door, not the older research notes. External link checking runs weekly and is not a required pull-request check.
- The QUAID step uses [evaluator/fixtures/quaid_cardano_node.json](evaluator/fixtures/quaid_cardano_node.json), captured 27 October 2026. It does not call the GitHub API.

## Open item

TODO (Christian): decide whether to publish `os-frontiers-assess` to PyPI and the Node package to npm, and under which account. This repository does not publish either one.
