# Researchy validation pass — Web2/Web3 prototypes catalog

> **Pass date:** 2026-09-24 PT  
> **Catalog under test:** `use-cases/web2-web3-prototypes-draft.md` (§1–§16 + §17 briefs = **23** rows).  
> **Method:** Live HTTP (`curl -sI -L`) on every catalog `http(s)` URL; WebFetch/WebSearch for freshness; `/workspace/osfl/sources/ORF_ERRATA.md` controls magnitude claims.  
> **Stage 0 honesty:** research candidates only — **no Hard Gate passed**.  
> **Status key:**  
> - **Validated** — primary URLs live; description still accurate under errata  
> - **Partial** — live, but thin receipts / magnitudes UNKNOWN / mechanism-only certainty  
> - **Broken** — primary URL 404/dead  
> - **Needs update** — live, but catalog Sources/wording should be refreshed

---

## Summary count table

| Status | Count |
|--------|------:|
| Validated | **17** |
| Partial | **4** |
| Broken | **0** |
| Needs update | **2** |
| **Total** | **23** |

**Broken URLs in old catalog:** none (41 unique catalog URLs → HTTP 200 after redirects).

---

## §1–§16

### 1. Corporate OSPOs (e.g. TODO Group / LF guides) — **Validated**

| | |
|--|--|
| **HTTP** | https://todogroup.org · LF open-source strategy guide · LF participating-in-communities guide — all **200** |
| **Citation notes** | Still the right Web2 OSPO coordination precedent. Gaps (custodial budget; episodic sponsorship ≠ ORF) hold. No OSFL-owned interviews (`synthesis/gaps.md`). |
| **Errata** | n/a |

### 2. Linux Foundation / CNCF / Apache Software Foundation — **Validated**

| | |
|--|--|
| **HTTP** | https://www.linuxfoundation.org · https://www.cncf.io · https://www.apache.org — all **200** |
| **Citation notes** | Family C membership / conformance / training precedent class still supports. Not a Web3 closed loop; no eight-gate claim. |
| **Errata** | Catalog “90+ Certified Kubernetes offerings” remains PARTIAL until recounted on a dated page (dossier D). |

### 3. GitHub Sponsors — **Validated**

| | |
|--|--|
| **HTTP** | About-Sponsors docs · https://github.com/sponsors — **200** |
| **Citation notes** | Maintainer stipends / Family D voluntary routing still accurate. Fee structure: “see docs,” not invented. |

### 4. Open Collective — **Validated**

| | |
|--|--|
| **HTTP** | https://opencollective.com · GitHub Sponsors partnership · docs — **200** |
| **Citation notes** | Transparent collectives / fiscal hosts; donation/grant-heavy inflows — still correct. |

### 5. Protocol Labs / Filecoin — **Partial**

| | |
|--|--|
| **HTTP** | https://protocol.ai · https://filecoin.io · https://drips.network — **200** |
| **Citation notes** | Ecosystem R&D / public-goods adjacency verified as live orgs. **Closed-loop coverage vs cost floor: UNKNOWN** (gaps.md). Do not invent treasury magnitudes. |

### 6. Ethereum (Protocol Guild, Project Odin, ENS adjacency) — **Validated**

| | |
|--|--|
| **HTTP** | https://www.protocolguild.org · Q2 2026 quarterly audit post — **200** |
| **Citation notes** | Mechanism (voluntary ≈1% pledges, vesting, revocable) still the right Family D precedent. Project Odin remains coordination precedent (repo), not a rail. |
| **Errata** | **Do not** republish $7.2M / $80M+ as High. Recoverable membership: **196 funded members as of 22 May 2026** (audit post). |

### 7. Optimism / Superchain — **Validated**

| | |
|--|--|
| **HTTP** | capital-allocation docs · Year 3 budget forum · OP buybacks blog — **200** |
| **Citation notes** | Strongest L2 Family A structural fee precedent; Retro Funding = OMF **deployment**, not replenishment. |
| **Errata** | Cite Foundation Year 3 figures as Foundation narrative (Medium under Gate 2). OP Mainnet **100%** carve-out per current docs. Buybacks: cite **vote** (Jan 2026 pilot), not proposal-only. |

### 8. Polkadot / OpenGov / PCF — **Partial**

| | |
|--|--|
| **HTTP** | https://wiki.polkadot.com/general/pcf/ — **200** |
| **Citation notes** | Cayman PCF as Neutral Legal Entity executor — legal design supported on wiki. |
| **Errata** | “~$70.6M 2025 treasury spend,” Anemoy “$1.5M,” referenda #1122/#1416/#1591 — **unverified** this pass; do not assert as High. |

### 9. Cardano / Intersect POSM — **Partial**

| | |
|--|--|
| **HTTP** | https://www.intersectmbo.org/news/the-paid-open-source-model — **200** |
| **Citation notes** | Program shape (OSC/OSO, retainers, Code for Us, incubation) supported on explainer. Strong OMF lab; **not** ORF replenishment proof. |
| **Errata** | “5.885M ADA” / “$300K bounty fully utilized” **not** on Intersect explainer — Unverified. |

### 10. Sovereign Tech Fund (Sovereign Tech Agency) — **Validated**

| | |
|--|--|
| **HTTP** | https://www.sovereign.tech/programs/fund · criteria/process news — **200** |
| **Citation notes** | Public-sector maintenance investment; site states minimum contract size **€50,000**. ORF absent (Bundestag / public budget inflows). |

### 11. OpenSSF (Open Source Security Foundation) — **Validated**

| | |
|--|--|
| **HTTP** | about · home · mission/vision/strategy blog — **200** |
| **Citation notes** | Industry security coalition; membership ≈ Family C; Alpha-Omega-style maintainer support still fair. Not a five-family ORF portfolio. |
| **Expansion note** | Alpha-Omega is distinct enough for a **new** expansion row (see expansion file). |

### 12. CHAOSS / GrimoireLab metrics — **Validated**

| | |
|--|--|
| **HTTP** | https://chaoss.community · https://chaoss.github.io/grimoirelab/ — **200** |
| **Citation notes** | Metrics ≠ money; Gate 1 health enabler only — still correct. |

### 13. Drips Protocol — **Validated**

| | |
|--|--|
| **HTTP** | https://drips.network · docs · radicle-dev/drips-contracts — **200** |
| **Citation notes** | Routing Rail S.1 only; zero independent replenishment under ORF taxonomy. |

### 14. Superfluid — **Validated**

| | |
|--|--|
| **HTTP** | https://www.superfluid.finance — **200** |
| **Citation notes** | Routing Rail S.2 CFA stipends; moves existing money — still correct. |

### 15. Merit Systems — **Needs update**

| | |
|--|--|
| **HTTP** | Catalog cites repo `tools/MERIT_SYSTEMS.md` only. Primary site **https://merit.systems** is **200** and should be added to Sources. |
| **Citation notes** | Attribution / AgentCash / x402 experiments still research-horizon. Magnitudes UNKNOWN without local receipts. Not Broken — Sources incomplete. |

### 16. Andamio — **Validated**

| | |
|--|--|
| **HTTP** | https://andamio.io · docs · GitHub org — **200** |
| **Citation notes** | Contributor pathways / credential ladders / escrow routing — still correct; ≠ replenishment. |

---

## §17 brief rows

### ENS DAO / Endowment — **Validated**

- URLs: EP 6.46 docs · KPK 2025 review forum — **200**
- **Errata:** Closest closed-loop judgment; yield ≈⅕ opex. **Do not stack** KPK Dec AUM with EP 6.46 AUM.

### Tidelift / Sonar — **Validated**

- URL: Sonar “to acquire Tidelift” press release — **200**
- **Errata:** Keep **definitive agreement** wording until a closing announcement is attached. Named customers hold.

### Octant (Golem) — **Partial**

- URL: Golem Foundation Octant announcement (2023-08-08) — **200**
- **Errata:** Epoch payout figures (e.g. “Epoch 8: ~460 ETH”) **unverified** this pass. Announcement supports staking-yield design, not epoch cash totals.

### Nouns DAO — **Needs update**

- Catalog Source cell: “Evidence Register: unverified” — **no primary URL**.
- Live primary: **https://nouns.wtf** (**200**). Magnitudes still Unverified — add URL; do not invent auction totals.

### Gitcoin Grants — **Validated**

- URL: https://gitcoin.co/program — **200**
- **Errata:** Quadratic rounds = Family D + allocation engine; **≠ replenishment**. Site counters are site counters.

### Open Source Observer — **Validated**

- URL: https://www.opensource.observer — **200**
- Impact tracing for Retro Funding; not revenue.

### LFX Crowdfunding — **Validated**

- URL: https://crowdfunding.linuxfoundation.org/for-companies — **200**
- LF invoicing platform for corporate contributions (Family C/D-like).

---

## Dead / broken URLs found in old catalog

**None.** All draft-catalog source URLs returned HTTP 200 on 2026-09-24 PT.

Catalog hygiene gaps (not HTTP-dead):

1. **Merit Systems** — add https://merit.systems  
2. **Nouns DAO** — add https://nouns.wtf (keep magnitudes Unverified)

---

## Method note

Live web via **WebSearch / WebFetch / curl** only. **No Grok CLI** this pass (per Christian). Prefer primary/official sources; mark UNKNOWN rather than invent; Stage 0 research candidates only.
