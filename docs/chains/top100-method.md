# Top-100 chains audit: method (batch 1)

> Prepared 2026-10-09 (PT). Stage 0: nothing here implies a Hard Gate is passed. Companion to `chains/top100-audit.md`. Aligned to `chains/top100-qa-rubric.md` v1.0 (read, not edited). **Batches 2–4 are on hold** because priorities have shifted.

## 1. Question

Does the three-piece model (dOSPO + OMF + ORF), **as written**, close the OSS sustainability gap? Chains are evidence. They never change the model.

## 2. Definitions (quoted from the box copies of the whitepapers)

- **dOSPO** (`sources/dospo-whitepaper.txt` l.424–427; dOSPO WP §3, PDF p.13): "A dOSPO is a community-mandated coordination layer that separates policy authority from operational execution in order to steward open source infrastructure within decentralized Web3 ecosystems. It derives legitimacy from decentralized governance and operates through a neutral, replaceable execution function constrained by explicit mandate." The mandate is time-bounded and renewed on a 2–4 year charter cycle. "A dOSPO is explicitly not a foundation, a DAO, or a corporate OSPO under a different name."
- **OMF** (`sources/omf-whitepaper.txt` l.195–199; OMF WP p.5): "OMF is a portable operational architecture for sustaining decentralized open source infrastructure. It is designed to operate independently of any specific governance structure and can be executed by foundations, DAOs, elected committees, or independent operators. In ecosystems that adopt coordination bodies such as a Decentralized Open Source Program Office (dOSPO), OMF functions as the execution layer."
  - **Minimum Viable OMF** (l.626–650; PDF p.15): "An ecosystem has implemented OMF if it has all five of the following":
    1. Dependency audit capability
    2. Program governance authority
    3. At least one sustainment program
    4. Transparent reporting mechanism ("at minimum on a quarterly basis")
    5. Portfolio review cadence
- **ORF** (`sources/orf-whitepaper.txt` l.49–51; ORF WP p.2, Author's Note): "the OMF defines the maintenance deployment layer (how resources go out); the ORF defines the replenishment layer (how resources come back)". (Spec only, not the definition: `sources/orf-docs/START_HERE.md` l.12, "a governance and economic design framework for identifying, validating, collecting, diversifying, and routing recurring sources of value back into the maintenance of shared open-source infrastructure.")
  - **Revenue families** (ORF WP §8): A Structural Network Revenue · B Enterprise Earned · C Membership, Certification & Training · D Voluntary & Incentivized · E Capital Income.
  - **Minimum Viable ORF** (l.655–677; PDF p.18):
    1. Verified cost floor
    2. Classified inflow inventory ("Issuance and routing are excluded from replenishment totals")
    3. At least one earned instrument "collecting real receipts … measured on net contribution"
    4. Net-contribution reporting (quarterly)
    5. Ratio and gate review cadence
- **POSM** (`chains/posm-cycle-chain-map.md` §2.1): P1 Funding In · P2 Steward Governance & Programs · P3 Outputs · P4 Commercialization Channels · P5 Commercial Adoption · P6 Return to Treasury. Placement = "the furthest POSM stage reached through a connected, evidenced path; a link to LEAK means value generated at P5 leaves without returning."

All three functions are defined, so none of the definitions is UNVERIFIED.

## 3. Snapshot

- Source: CoinGecko `/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250`.
- Page 1 fetched **2026-10-09 05:19:12–05:19:23 PT** (HTTP Date 12:19:23 GMT). Latest `last_updated` in the payload: 12:17:50Z (**05:17:50 PT**).
- Page 2 fetched 05:21:37 PT.
- Files: `chains/coingecko-snapshot-2026-10-09.json` and `chains/coingecko-snapshot-2026-10-09-page2.json`.
- Market cap is reported as CoinGecko's figure, not recomputed.

## 4. Scope and exclusion rules

**Rule D (Projects Manager, 2026-10-09):** "a token counts if it's the gas token of its own live chain with a public block explorer. Exchange chains and app chains count if they pass (CRO, OKB, KCS, GT, BGB, WBT). WLD is out, because its gas token is ETH. Ranks 1–10 stay unchanged."

- **Excluded:**
  - stablecoins
  - tokenized RWAs, funds and commodities
  - wrapped or staked derivatives
  - tokens with no own chain (app, DeFi, oracle, meme and exchange tokens)
  - non-gas tokens of a chain
  - L2 tokens whose gas is ETH
- **Explorer check:** HTTP 200 from a public explorer on 2026-10-09. Where an explorer was blocked, liveness rests on the alternative evidence below:

| Chain | Blocked for Researchy | Liveness evidence (9 Oct 2026) | Source |
|---|---|---|---|
| Avalanche | snowtrace.io, avascan.info (403; QA saw HTTP 202 challenge pages) | Public C-Chain RPC `api.avax.network/ext/bc/C/rpc`, `eth_getBlockByNumber latest` → block **97,122,948** at **05:36:17 PT** | USe Me, `chains/top100-qa-log.md`, Batch 1 QA §7 |
| Bitcoin Cash | bchexplorer.cash (403 for Researchy; HTTP 200 for QA); blockchair.com HTML 401 | `api.blockchair.com/bitcoin-cash/stats` → best block **972,125** at **05:30:44 PT** (15,203 tx/24h) | USe Me, `chains/top100-qa-log.md`, Batch 1 QA §7 |
| Canton | ccview.io (403) | lighthouse.cantonloop.com HTTP 200 ("Loop Data"), confirmed by QA | Researchy 2026-10-09; USe Me QA log §7 |
| X Layer (extra) | — | `rpc.xlayer.tech` → block 72,780,451 at 05:38:07 PT | USe Me, `chains/top100-qa-log.md`, Batch 1 QA §7 |
- **Cardano rank:** #11 with WBT excluded; #12 under the gas-token rule (WBT, CRO, OKB counted), CoinGecko top-100 snapshot 9 Oct 2026 05:19 PT; see top100-method.md.
- **Batches 2–4:** rule D has to be re-applied to ranks 26–100. The CoinGecko snapshot needs to extend to about rank 400 (≥ 2 pages; the QA cross-check put the 100th chain at CG #391 under the earlier rule).

## 5. Fields

| Field | Meaning |
|---|---|
| Rank | Chain rank after exclusions (batch 1 = 1–25) |
| Native coin / Market cap | CoinGecko symbol and `market_cap` at snapshot, with CG rank |
| Funding processes | Evidenced ways money reaches core OSS (protocol streams, foundations, grants, donations, fees), with figures and status |
| dOSPO-like / OMF-like / ORF-like | Present / Partial / Missing under §6, naming the mechanism |
| Missing pieces | In whitepaper terms only: dOSPO (i)–(iv), MV-OMF items 1–5, Families A–E, MV-ORF items 1–5 |
| Would adding them help? (PROPOSAL) | §7 |
| POSM stage | §2 rule; "→ leak" when value exits via burn, validators, buyback or exchange |
| Direction | Dated 2025–2026 signal, or "no signal / stationary" |
| Sources / Checked | URLs, all read 2026-10-09 |
| Confidence | High / Medium / Low. Medium and Low rows cannot support a Present cell. |

## 6. Rating rules (rubric §B, which quotes the whitepapers)

- **dOSPO-like:**
  - Present = all of (i) community mandate, (ii) policy/execution separation, (iii) replaceable operator, (iv) time-bounded or renewable charter.
  - Partial = some of these, named in the cell.
  - Missing = a foundation or company alone, or a token vote on monetary parameters only.
- **OMF-like:**
  - Present = a recurring, authorized maintenance-deployment program.
  - Partial = one-off or episodic grants only, or programs without reporting.
  - Missing = nothing, or only VC, accelerator, SAFE, buyback or burn.
  - Each cell lists the MV-OMF items shown.
- **ORF-like:**
  - Present = a non-issuance, recurring inflow flowing back to an OSS-maintenance treasury.
  - Partial = collection exists but is not routed to maintenance, is not net-accounted, or is issuance (excluded).
  - Missing = no collection, or only burns, validator income, grants, drawdown, or issuance not aimed at OSS.
  - Grants alone or issuance alone are never Present.
  - Issuance split (for rubric v1.1, QA A-2): issuance aimed at OSS is ORF Partial, excluded from replenishment (Zcash, Canton; Cardano's mixed τ). Issuance not aimed at OSS is Missing (MemeCore, Bittensor, NEAR's treasury share).
- **POSM:** P6 is never counted as reached when the return is issuance-dominated.

## 7. PROPOSAL cells

- Each cell starts with "PROPOSAL (example; not a finding):" and uses conditional language ("could", "would").
- It plugs a real, named program or incentive into OMF or ORF **exactly as the whitepaper defines it**, citing the WP section (OMF WP Program Architecture p.24 / Appendix B p.52; ORF WP §8 Families A–E; ORF WP §4 MV-ORF), with the spec ID in parentheses.
- Named external programs appear only as "-style" examples: Sovereign Tech Agency, Alpha-Omega, Tidelift, Protocol Guild.
- A cell never proposes changing the model, counting issuance, grants or Retro as replenishment, or relaxing any MV item or gate. It never introduces numbers.

## 8. Conventions

- **UNVERIFIED:** not confirmed on a primary page on 2026-10-09.
- **DERIVED:** computed by OSFL from cited inputs (inputs stated).
- **Self-reported** figures are labeled as such.
- Untagged figures were matched on the cited page on 2026-10-09.
- **Captures** (2026-10-09, `chains/data/`): `stellar-scf-v7-blog-`, `stellar-scf-handbook-`, `litecoin-bounty-litecoin-core-`, `shieldedlabs-home-`, `zfnd-home-` (05:41 PT); `xaodao-linkedin-week2-20260420-`, `xaodao-linkedin-month1-20260504-`, `xaodao-linkedin-week9-20260608-`, `nbtc-xaodao-20260909-` (05:41 PT); each name ends in `2026-10-09.html`.
- The UNVERIFIED count covers every table column, including Missing pieces and PROPOSAL.
- **Stale figures not used:** OpenSats "$32.1M / 377"; Zcash "$95M / 63,962 ZEC".
- Working files: `chains/work/rows.py` (row evidence), `chains/work/rows_qa.py` (rubric-aligned ratings, missing pieces, proposals), `chains/work/build.py` (generator, counts).
