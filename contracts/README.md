# Proposed header contracts

These are ordered header lists, not client data or final accepted schemas. No sample taxpayer or financial records are included. Finalize exact required contact fields and test the client's actual importer before versioning an accepted schema. Store records only in the approved restricted workspace.

- [Weekly leads](weekly-leads-v1.columns.txt): one unique taxpayer prospect per row with primary-notice evidence.
- [Referral log](referral-log-v1.columns.txt): delivery, independent acceptance, activity, overlap and suppression.
- [Receipt log](receipt-log-v1.columns.txt): actual unique receipts and append-only adjustments; private approved terms determine fees, not column names.

Money in the receipt log uses integer cents and explicit currency; weekly export uses fixed decimal USD text. No SSN/EIN/fragments, card data, raw documents, private financial evidence or secret URLs. Evidence fields contain restricted references only. Fees/taxes and agreement windows are unset until qualified review and approval. CSV injection and access tests apply to logs as well as leads.
