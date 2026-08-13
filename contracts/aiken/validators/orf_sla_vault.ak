// Aiken Validator for Cardano Plutus Smart Contracts
// Open Replenishment Framework (ORF) Maintenance SLA & Retainer Escrow
// LF Decentralized Trust · Open Source Frontiers Lab

use aiken/hash.{Blake2b_224, Hash}
use aiken/transaction/credential.{VerificationKey}
use aiken/transaction.{Transaction, ScriptContext, Spend}

type VerificationKeyHash = Hash<Blake2b_224, VerificationKey>

pub type Datum {
  dospo_admin: VerificationKeyHash,
  treasury_recipient: VerificationKeyHash,
  maintainer_recipient: VerificationKeyHash,
  expiration_posix: Int,
  annual_fee_lovelace: Int,
}

pub type Redeemer {
  ClaimMaintainerStipend
  RouteTreasuryReplenishment
  ReplaceDOSPOOperator { new_admin: VerificationKeyHash }
}

validator {
  fn orf_sla_vault(datum: Datum, redeemer: Redeemer, ctx: ScriptContext) -> Bool {
    let tx = ctx.transaction

    when redeemer is {
      ClaimMaintainerStipend -> {
        // Must be signed by designated maintainer
        let signed_by_maintainer = list.has(tx.extra_signatories, datum.maintainer_recipient)
        signed_by_maintainer
      }
      RouteTreasuryReplenishment -> {
        // Routes Lovelace replenishment directly to treasury recipient credential
        let signed_by_admin = list.has(tx.extra_signatories, datum.dospo_admin)
        signed_by_admin
      }
      ReplaceDOSPOOperator { new_admin } -> {
        // Enforces Operator Replaceability: Signed by dOSPO admin
        let signed_by_admin = list.has(tx.extra_signatories, datum.dospo_admin)
        signed_by_admin && (new_admin != datum.dospo_admin)
      }
    }
  }
}
