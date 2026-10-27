# Open Source Frontiers Lab Governance

> **Project charter and governance model**
> *LF Decentralized Trust · Open Source Frontiers Lab · Stage 0*

The lab researches and publishes specifications for open-source sustainability. Web3 treasuries are the primary audience. The same specifications also apply to Web2 foundations, companies, and public funders.

This file is the governance of the repository. It is not a claim that a hard gate has passed, and it does not appoint anyone who has not agreed to serve.

## 1. Principles

1. **Vendor neutrality.** No company, foundation, or consulting firm holds exclusive authority over the specifications.
2. **Evidence.** A maturity claim needs public evidence. A point score is not a hard gate.
3. **Operator replaceability.** Maintainer roles are public and can be ended.
4. **Open contributions.** Decisions happen in public pull requests. Code is Apache-2.0. Documentation is CC-BY-4.0. Commits are signed off with the Developer Certificate of Origin.

The lead maintainer's consulting firm gets no special status.

## 2. Who maintains

Active maintainers are listed in [MAINTAINERS.md](MAINTAINERS.md). Today that list has one person, Christian Taylor ([@ThatGuyLLC](https://github.com/ThatGuyLLC)). The GitHub organization account is not a maintainer.

TODO (Christian): recruit 2 to 4 outside maintainers. Do not add a name here until that person has agreed in public.

## 3. Becoming a maintainer

A maintainer is someone who has reviewed this repository in public over time and agrees to keep doing so.

Nomination is a pull request that adds the person to [MAINTAINERS.md](MAINTAINERS.md) and to [.github/CODEOWNERS](.github/CODEOWNERS). The nominee has to say yes on that pull request.

- When two or more maintainers exist, two of them must approve the pull request.
- When only one maintainer exists, that maintainer may not self-approve a second seat. TODO (Christian): name the LF Decentralized Trust role that must also approve the first outside maintainers. Until that role is named, the seat stays empty.

## 4. Leaving

A maintainer leaves by opening a pull request that removes their name from [MAINTAINERS.md](MAINTAINERS.md) and from [.github/CODEOWNERS](.github/CODEOWNERS), and that names who will take the reviews they still hold. If they cannot open the pull request, another maintainer may open it and the record must say why.

A maintainer who is inactive and unreachable is not removed in silence. The proposal stays open for others to see.

## 5. Decisions, including when there is no consensus

Ordinary changes are pull requests. The default is consensus: reviewers state objections, and the author changes the proposal or records why an objection stands.

If consensus fails:

- With two or more maintainers, a decision can be taken by a majority of the maintainers who vote on the pull request. At least two maintainers must vote. The dissent is left in the thread and summarized in the merge commit message.
- With one maintainer, there is no majority to take. The pull request stays open, or it is closed without a claim that a vote was held. A single maintainer merging their own specification change is bootstrap work, and the pull request must say that.

A hard-gate status in [VALIDATION.md](VALIDATION.md) is not changed by a vote alone. The evidence section of that file has to change in the same pull request.

## 6. Conflicts of interest

A maintainer discloses, on the pull request, any paid relationship with a treasury, vendor, or program that the change would advantage.

The lead maintainer's consulting firm gets no special status. Open Source Cowboy Consulting is an affiliation credit in [AUTHORS.md](AUTHORS.md). It is not a maintainer, it does not get a CODEOWNERS entry, and a document that names it is not an endorsement of a client.

A maintainer does not review a change whose main effect is to benefit their employer or their client. Another maintainer reviews it. Until a second maintainer exists, that change waits. TODO (Christian): this rule cannot be operated by one person. It is one reason the outside-maintainer seats in section 2 are open.

## 7. Replacing the lead

The lead maintainer is replaceable. The role is not a property right and it does not travel with a consulting contract.

- With two or more other maintainers, those maintainers may open a pull request that names a new lead. A majority of maintainers other than the current lead must approve it. The current lead may object in the thread. The objection is kept. It is not a veto.
- With fewer than two other maintainers, the repository cannot replace the lead from inside. TODO (Christian): write the LF Decentralized Trust path for that case, including who receives the request. Do not invent an address here.

The same pull request updates [MAINTAINERS.md](MAINTAINERS.md) and [.github/CODEOWNERS](.github/CODEOWNERS).

## 8. Meetings and discussion

A public meeting is the intention while the lab is in Stage 0. No cadence, weekday, or call link is set, because none has been agreed.

TODO (Christian): set the meeting cadence and publish the call details. Notes, when a meeting happens, go in [meetings/](meetings/README.md) using [meetings/TEMPLATE.md](meetings/TEMPLATE.md).

GitHub Discussions are not enabled by this file. Seed questions for the day they are enabled are in [discussions/SEED_QUESTIONS.md](discussions/SEED_QUESTIONS.md). TODO (Christian): enable Discussions on the repository.

## 9. Licensing

Code: [LICENSE](LICENSE) (Apache-2.0). Documentation: [LICENSE-DOCS](LICENSE-DOCS) (CC-BY-4.0). There is no `LICENSE-CODE` file.
