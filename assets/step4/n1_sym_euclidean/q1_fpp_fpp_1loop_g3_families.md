# N=1 SYM `Q_1(f_{++}f_{++})` 1-loop `g^3` fully connected families

## Counts

- raw fully connected Wick contractions: `348`
- fully connected topological classes: `20`
- `12/21`-mirror-reduced families: `10`

## Mirror-reduced families

### `F01`

- action multiset: `V_AAA x 1`, `V_A_lambda_lambdabar x 2`
- representative:
  - `O:Qf1_lambdabar --fermion-- V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A --A-- V_A_lambda_lambdabar#1:A`
  - `V_AAA#1:A1 --A-- V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar --fermion-- V_A_lambda_lambdabar#2:lambda`
- external fields:
  - `V_AAA#1:A2`
  - `V_AAA#1:A3`
  - `V_A_lambda_lambdabar#2:lambdabar`
- interpretation:
  - mixed gauge-fermion completion
  - both extra external `A` legs live on the `AAA` vertex

### `F02`

- action multiset: `V_AAA x 1`, `V_A_lambda_lambdabar x 2`
- representative:
  - `O:Qf1_lambdabar --fermion-- V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A --A-- V_A_lambda_lambdabar#2:A`
  - `V_AAA#1:A1 --A-- V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar --fermion-- V_A_lambda_lambdabar#2:lambda`
- external fields:
  - `V_AAA#1:A2`
  - `V_AAA#1:A3`
  - `V_A_lambda_lambdabar#2:lambdabar`
- interpretation:
  - same channel as `F01`
  - mirror attachment of the operator `A` to the other `A\lambda\widetilde\lambda` vertex

### `F03`

- action multiset: `V_AAA x 1`, `V_A_lambda_lambdabar x 2`
- representative:
  - `O:Qf1_lambdabar --fermion-- V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A --A-- V_AAA#1:A1`
  - `V_AAA#1:A2 --A-- V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar --fermion-- V_A_lambda_lambdabar#2:lambda`
- external fields:
  - `V_AAA#1:A3`
  - `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#2:lambdabar`
- interpretation:
  - mixed gauge-fermion completion
  - one extra external `A` on `AAA`, one extra external `A` on the second `A\lambda\widetilde\lambda`

### `F04`

- action multiset: `V_AAA x 1`, `V_A_lambda_lambdabar x 2`
- representative:
  - `O:Qf1_lambdabar --fermion-- V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A --A-- V_AAA#1:A1`
  - `V_AAA#1:A2 --A-- V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar --fermion-- V_A_lambda_lambdabar#2:lambda`
- external fields:
  - `V_AAA#1:A3`
  - `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#2:lambdabar`
- interpretation:
  - same channel as `F03`
  - mirror attachment of the internal gauge leg to the other `A\lambda\widetilde\lambda` vertex

### `F05`

- action multiset: `V_AAA x 2`, `V_A_lambda_lambdabar x 1`
- representative:
  - `O:Qf1_lambdabar --fermion-- V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A --A-- V_AAA#1:A1`
  - `V_AAA#1:A2 --A-- V_AAA#2:A1`
  - `V_AAA#1:A3 --A-- V_A_lambda_lambdabar#1:A`
- external fields:
  - `V_AAA#2:A2`
  - `V_AAA#2:A3`
  - `V_A_lambda_lambdabar#1:lambdabar`
- interpretation:
  - gauge-line cubic completion
  - the `A\lambda\widetilde\lambda` vertex attaches to the first cubic gauge vertex

### `F06`

- action multiset: `V_AAA x 2`, `V_A_lambda_lambdabar x 1`
- representative:
  - `O:Qf1_lambdabar --fermion-- V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A --A-- V_AAA#1:A1`
  - `V_AAA#1:A2 --A-- V_AAA#2:A1`
  - `V_AAA#2:A2 --A-- V_A_lambda_lambdabar#1:A`
- external fields:
  - `V_AAA#1:A3`
  - `V_AAA#2:A3`
  - `V_A_lambda_lambdabar#1:lambdabar`
- interpretation:
  - same channel as `F05`
  - the `A\lambda\widetilde\lambda` vertex attaches to the second cubic gauge vertex

### `F07`

- action multiset: `V_AAAA x 1`, `V_A_lambda_lambdabar x 1`
- representative:
  - `O:Qf1_lambdabar --fermion-- V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A --A-- V_AAAA#1:A1`
  - `V_AAAA#1:A2 --A-- V_A_lambda_lambdabar#1:A`
- external fields:
  - `V_AAAA#1:A3`
  - `V_AAAA#1:A4`
  - `V_A_lambda_lambdabar#1:lambdabar`
- interpretation:
  - quartic/contact gauge completion

### `F08`

- action multiset: `V_A_lambda_lambdabar x 3`
- representative:
  - `O:Qf1_lambdabar --fermion-- V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A --A-- V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar --fermion-- V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar --fermion-- V_A_lambda_lambdabar#3:lambda`
- external fields:
  - `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#3:A`
  - `V_A_lambda_lambdabar#3:lambdabar`
- interpretation:
  - fermion-line completion
  - extra `A` insertions live on the downstream fermion chain

### `F09`

- action multiset: `V_A_lambda_lambdabar x 3`
- representative:
  - `O:Qf1_lambdabar --fermion-- V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A --A-- V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar --fermion-- V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar --fermion-- V_A_lambda_lambdabar#3:lambda`
- external fields:
  - `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#3:A`
  - `V_A_lambda_lambdabar#3:lambdabar`
- interpretation:
  - same channel as `F08`
  - operator `A` inserted on the middle `A\lambda\widetilde\lambda` vertex

### `F10`

- action multiset: `V_A_lambda_lambdabar x 3`
- representative:
  - `O:Qf1_lambdabar --fermion-- V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A --A-- V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar --fermion-- V_A_lambda_lambdabar#3:lambda`
  - `V_A_lambda_lambdabar#2:lambda --fermion-- V_A_lambda_lambdabar#3:lambdabar`
- external fields:
  - `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#2:lambdabar`
  - `V_A_lambda_lambdabar#3:A`
- interpretation:
  - crossed fermion-chain completion

## Coarser analytic channels

- channel `C_1`: `V_AAA (V_{A\lambda\widetilde\lambda})^2`
  - families: `F01`, `F02`, `F03`, `F04`

- channel `C_2`: `(V_AAA)^2 V_{A\lambda\widetilde\lambda}`
  - families: `F05`, `F06`

- channel `C_3`: `V_AAAA V_{A\lambda\widetilde\lambda}`
  - families: `F07`

- channel `C_4`: `(V_{A\lambda\widetilde\lambda})^3`
  - families: `F08`, `F09`, `F10`

## Extraction for `(\nabla-\partial)(f_{++}\widetilde\lambda)`

- under the strict fully connected criterion, the candidate `g^3` completion sector is exactly the union
  - `C_1 \cup C_2 \cup C_3 \cup C_4`
- the disconnected ghost pair channel disappears
- the disconnected `AAA-AAA` bubble channel disappears
- the disconnected insertion terms `O_{A\widetilde\lambda,A}`, `O_{\widetilde\lambda,AA}`, `O_{AA,\widetilde\lambda}` disappear
