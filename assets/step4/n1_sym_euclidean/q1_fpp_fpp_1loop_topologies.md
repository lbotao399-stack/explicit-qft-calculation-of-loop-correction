# N=1 SYM Q_1(f_{++}f_{++}) 1-loop topological classes

- source raw Wick contractions: `9520`
- topological classes: `92`

## By explicit order

- `g^2`: `6`
- `g^3`: `20`
- `g^4`: `66`

## By explicit order and external sector

- `g^2` `['A', 'lbar']`: `6`
- `g^3` `['A', 'A', 'lbar']`: `20`
- `g^4` `['A', 'A', 'A', 'lbar']`: `66`

## Classes

### T001

- total explicit order: `g^2`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'lbar']`
- raw Wick contraction multiplicity: `6`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T002

- total explicit order: `g^2`
- insertion term: `O12_dlb_A`
- action vertices: `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'lbar']`
- raw Wick contraction multiplicity: `2`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_A_lambda_lambdabar#2:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T003

- total explicit order: `g^2`
- insertion term: `O12_dlb_A`
- action vertices: `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'lbar']`
- raw Wick contraction multiplicity: `2`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T004

- total explicit order: `g^2`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'lbar']`
- raw Wick contraction multiplicity: `6`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T005

- total explicit order: `g^2`
- insertion term: `O21_A_dlb`
- action vertices: `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'lbar']`
- raw Wick contraction multiplicity: `2`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_A_lambda_lambdabar#2:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T006

- total explicit order: `g^2`
- insertion term: `O21_A_dlb`
- action vertices: `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'lbar']`
- raw Wick contraction multiplicity: `2`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T007

- total explicit order: `g^3`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `6`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_AAA#1:A1` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A2` : `A`
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T008

- total explicit order: `g^3`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `6`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_AAA#1:A1` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A2` : `A`
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T009

- total explicit order: `g^3`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `12`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#2:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T010

- total explicit order: `g^3`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `12`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T011

- total explicit order: `g^3`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `36`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#1:A3` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAA#2:A2` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T012

- total explicit order: `g^3`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#2:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T013

- total explicit order: `g^3`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAAA` x 1, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `12`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAAA#1:A1`
  - `V_AAAA#1:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAAA#1:A3` : `A`
  - `V_AAAA#1:A4` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T014

- total explicit order: `g^3`
- insertion term: `O12_dlb_A`
- action vertices: `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `6`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
- representative external ports:
  - `V_A_lambda_lambdabar#2:A` : `A`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#3:lambdabar` : `lbar`

### T015

- total explicit order: `g^3`
- insertion term: `O12_dlb_A`
- action vertices: `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `6`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
- representative external ports:
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#3:lambdabar` : `lbar`

### T016

- total explicit order: `g^3`
- insertion term: `O12_dlb_A`
- action vertices: `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `6`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
  - `V_A_lambda_lambdabar#2:lambda` --[fermion]-- `V_A_lambda_lambdabar#3:lambdabar`
- representative external ports:
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`
  - `V_A_lambda_lambdabar#3:A` : `A`

### T017

- total explicit order: `g^3`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `6`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_AAA#1:A1` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A2` : `A`
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T018

- total explicit order: `g^3`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `6`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_AAA#1:A1` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A2` : `A`
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T019

- total explicit order: `g^3`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `12`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#2:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T020

- total explicit order: `g^3`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `12`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T021

- total explicit order: `g^3`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `36`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#1:A3` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAA#2:A2` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T022

- total explicit order: `g^3`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#2:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T023

- total explicit order: `g^3`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAAA` x 1, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `12`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAAA#1:A1`
  - `V_AAAA#1:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAAA#1:A3` : `A`
  - `V_AAAA#1:A4` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T024

- total explicit order: `g^3`
- insertion term: `O21_A_dlb`
- action vertices: `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `6`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
- representative external ports:
  - `V_A_lambda_lambdabar#2:A` : `A`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#3:lambdabar` : `lbar`

### T025

- total explicit order: `g^3`
- insertion term: `O21_A_dlb`
- action vertices: `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `6`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
- representative external ports:
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#3:lambdabar` : `lbar`

### T026

- total explicit order: `g^3`
- insertion term: `O21_A_dlb`
- action vertices: `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `6`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
  - `V_A_lambda_lambdabar#2:lambda` --[fermion]-- `V_A_lambda_lambdabar#3:lambdabar`
- representative external ports:
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`
  - `V_A_lambda_lambdabar#3:A` : `A`

### T027

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 1, `V_AAAA` x 1, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `24`
- automorphism order: `6`
- graph symmetry factor: `1/6`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAAA#1:A1`
  - `V_AAA#1:A3` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAAA#1:A2` : `A`
  - `V_AAAA#1:A3` : `A`
  - `V_AAAA#1:A4` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T028

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 1, `V_AAAA` x 1, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAAA#1:A1`
  - `V_AAAA#1:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAAA#1:A3` : `A`
  - `V_AAAA#1:A4` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T029

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 1, `V_AAAA` x 1, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAAA#1:A1`
  - `V_AAA#1:A1` --[A]-- `V_AAAA#1:A2`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAAA#1:A3` : `A`
  - `V_AAAA#1:A4` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T030

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 1, `V_AAAA` x 1, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAAA#1:A1`
  - `V_AAA#1:A1` --[A]-- `V_AAAA#1:A2`
  - `V_AAAA#1:A3` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAA#1:A2` : `A`
  - `V_AAA#1:A3` : `A`
  - `V_AAAA#1:A4` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T031

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `18`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_AAA#1:A1` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
- representative external ports:
  - `V_AAA#1:A2` : `A`
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#3:lambdabar` : `lbar`

### T032

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `18`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_AAA#1:A1` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
  - `V_A_lambda_lambdabar#2:lambda` --[fermion]-- `V_A_lambda_lambdabar#3:lambdabar`
- representative external ports:
  - `V_AAA#1:A2` : `A`
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`
  - `V_A_lambda_lambdabar#3:A` : `A`

### T033

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `18`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_AAA#1:A1` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
- representative external ports:
  - `V_AAA#1:A2` : `A`
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#3:lambdabar` : `lbar`

### T034

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `18`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_AAA#1:A1` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
  - `V_A_lambda_lambdabar#2:lambda` --[fermion]-- `V_A_lambda_lambdabar#3:lambdabar`
- representative external ports:
  - `V_AAA#1:A2` : `A`
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`
  - `V_A_lambda_lambdabar#3:A` : `A`

### T035

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `18`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_AAA#1:A1` --[A]-- `V_A_lambda_lambdabar#3:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
- representative external ports:
  - `V_AAA#1:A2` : `A`
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#3:lambdabar` : `lbar`

### T036

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `18`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_AAA#1:A1` --[A]-- `V_A_lambda_lambdabar#3:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
  - `V_A_lambda_lambdabar#2:lambda` --[fermion]-- `V_A_lambda_lambdabar#3:lambdabar`
- representative external ports:
  - `V_AAA#1:A2` : `A`
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T037

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `36`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#2:A` : `A`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#3:lambdabar` : `lbar`

### T038

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `36`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#3:lambdabar` : `lbar`

### T039

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `36`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
  - `V_A_lambda_lambdabar#2:lambda` --[fermion]-- `V_A_lambda_lambdabar#3:lambdabar`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`
  - `V_A_lambda_lambdabar#3:A` : `A`

### T040

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#1:A3` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#2:A2` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#2:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T041

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#1:A3` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#2:A2` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T042

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_AAA#2:A1` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAA#2:A2` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T043

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_AAA#2:A1` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAA#2:A2` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T044

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_AAA#1:A1` --[A]-- `V_AAA#2:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAA#2:A2` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T045

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_AAA#1:A1` --[A]-- `V_AAA#2:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAA#2:A2` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T046

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `144`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#2:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#2:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T047

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `144`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#2:A2` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T048

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 3, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `648`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#1:A3` --[A]-- `V_AAA#3:A1`
  - `V_AAA#2:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAA#2:A3` : `A`
  - `V_AAA#3:A2` : `A`
  - `V_AAA#3:A3` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T049

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 3, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `648`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#1:A3` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_AAA#2:A2` --[A]-- `V_AAA#3:A1`
- representative external ports:
  - `V_AAA#2:A3` : `A`
  - `V_AAA#3:A2` : `A`
  - `V_AAA#3:A3` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T050

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 3, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `648`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#2:A2` --[A]-- `V_AAA#3:A1`
  - `V_AAA#2:A3` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAA#3:A2` : `A`
  - `V_AAA#3:A3` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T051

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAA` x 3, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `1296`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#2:A2` --[A]-- `V_AAA#3:A1`
  - `V_AAA#3:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_AAA#3:A3` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T052

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAAA` x 1, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `8`
- automorphism order: `6`
- graph symmetry factor: `1/6`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_AAAA#1:A1` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAAA#1:A2` : `A`
  - `V_AAAA#1:A3` : `A`
  - `V_AAAA#1:A4` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T053

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAAA` x 1, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `8`
- automorphism order: `6`
- graph symmetry factor: `1/6`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_AAAA#1:A1` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAAA#1:A2` : `A`
  - `V_AAAA#1:A3` : `A`
  - `V_AAAA#1:A4` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T054

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAAA` x 1, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `24`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAAA#1:A1`
  - `V_AAAA#1:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAAA#1:A3` : `A`
  - `V_AAAA#1:A4` : `A`
  - `V_A_lambda_lambdabar#2:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T055

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_AAAA` x 1, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `24`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_AAAA#1:A1`
  - `V_AAAA#1:A2` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAAA#1:A3` : `A`
  - `V_AAAA#1:A4` : `A`
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T056

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_A_lambda_lambdabar` x 4
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `24`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
  - `V_A_lambda_lambdabar#3:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#4:lambda`
- representative external ports:
  - `V_A_lambda_lambdabar#2:A` : `A`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#4:A` : `A`
  - `V_A_lambda_lambdabar#4:lambdabar` : `lbar`

### T057

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_A_lambda_lambdabar` x 4
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `24`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
  - `V_A_lambda_lambdabar#3:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#4:lambda`
- representative external ports:
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#4:A` : `A`
  - `V_A_lambda_lambdabar#4:lambdabar` : `lbar`

### T058

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_A_lambda_lambdabar` x 4
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `24`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
  - `V_A_lambda_lambdabar#2:lambda` --[fermion]-- `V_A_lambda_lambdabar#3:lambdabar`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#4:lambda`
- representative external ports:
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#4:A` : `A`
  - `V_A_lambda_lambdabar#4:lambdabar` : `lbar`

### T059

- total explicit order: `g^4`
- insertion term: `O12_dlb_A`
- action vertices: `V_A_lambda_lambdabar` x 4
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `24`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf1_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f2_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
  - `V_A_lambda_lambdabar#2:lambda` --[fermion]-- `V_A_lambda_lambdabar#4:lambdabar`
  - `V_A_lambda_lambdabar#3:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#4:lambda`
- representative external ports:
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#4:A` : `A`

### T060

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 1, `V_AAAA` x 1, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `24`
- automorphism order: `6`
- graph symmetry factor: `1/6`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAAA#1:A1`
  - `V_AAA#1:A3` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAAA#1:A2` : `A`
  - `V_AAAA#1:A3` : `A`
  - `V_AAAA#1:A4` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T061

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 1, `V_AAAA` x 1, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAAA#1:A1`
  - `V_AAAA#1:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAAA#1:A3` : `A`
  - `V_AAAA#1:A4` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T062

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 1, `V_AAAA` x 1, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAAA#1:A1`
  - `V_AAA#1:A1` --[A]-- `V_AAAA#1:A2`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAAA#1:A3` : `A`
  - `V_AAAA#1:A4` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T063

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 1, `V_AAAA` x 1, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAAA#1:A1`
  - `V_AAA#1:A1` --[A]-- `V_AAAA#1:A2`
  - `V_AAAA#1:A3` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAA#1:A2` : `A`
  - `V_AAA#1:A3` : `A`
  - `V_AAAA#1:A4` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T064

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `18`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_AAA#1:A1` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
- representative external ports:
  - `V_AAA#1:A2` : `A`
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#3:lambdabar` : `lbar`

### T065

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `18`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_AAA#1:A1` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
  - `V_A_lambda_lambdabar#2:lambda` --[fermion]-- `V_A_lambda_lambdabar#3:lambdabar`
- representative external ports:
  - `V_AAA#1:A2` : `A`
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`
  - `V_A_lambda_lambdabar#3:A` : `A`

### T066

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `18`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_AAA#1:A1` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
- representative external ports:
  - `V_AAA#1:A2` : `A`
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#3:lambdabar` : `lbar`

### T067

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `18`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_AAA#1:A1` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
  - `V_A_lambda_lambdabar#2:lambda` --[fermion]-- `V_A_lambda_lambdabar#3:lambdabar`
- representative external ports:
  - `V_AAA#1:A2` : `A`
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`
  - `V_A_lambda_lambdabar#3:A` : `A`

### T068

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `18`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_AAA#1:A1` --[A]-- `V_A_lambda_lambdabar#3:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
- representative external ports:
  - `V_AAA#1:A2` : `A`
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#3:lambdabar` : `lbar`

### T069

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `18`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_AAA#1:A1` --[A]-- `V_A_lambda_lambdabar#3:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
  - `V_A_lambda_lambdabar#2:lambda` --[fermion]-- `V_A_lambda_lambdabar#3:lambdabar`
- representative external ports:
  - `V_AAA#1:A2` : `A`
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T070

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `36`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#2:A` : `A`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#3:lambdabar` : `lbar`

### T071

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `36`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#3:lambdabar` : `lbar`

### T072

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 1, `V_A_lambda_lambdabar` x 3
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `36`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
  - `V_A_lambda_lambdabar#2:lambda` --[fermion]-- `V_A_lambda_lambdabar#3:lambdabar`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`
  - `V_A_lambda_lambdabar#3:A` : `A`

### T073

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#1:A3` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#2:A2` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#2:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T074

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#1:A3` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#2:A2` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T075

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_AAA#2:A1` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAA#2:A2` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T076

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_AAA#2:A1` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAA#2:A2` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T077

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_AAA#1:A1` --[A]-- `V_AAA#2:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAA#2:A2` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T078

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `72`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_AAA#1:A1` --[A]-- `V_AAA#2:A1`
  - `V_AAA#1:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAA#2:A2` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T079

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `144`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#2:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#2:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T080

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 2, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `144`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#2:A2` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T081

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 3, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `648`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#1:A3` --[A]-- `V_AAA#3:A1`
  - `V_AAA#2:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAA#2:A3` : `A`
  - `V_AAA#3:A2` : `A`
  - `V_AAA#3:A3` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T082

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 3, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `648`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#1:A3` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_AAA#2:A2` --[A]-- `V_AAA#3:A1`
- representative external ports:
  - `V_AAA#2:A3` : `A`
  - `V_AAA#3:A2` : `A`
  - `V_AAA#3:A3` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T083

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 3, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `648`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#2:A2` --[A]-- `V_AAA#3:A1`
  - `V_AAA#2:A3` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAA#3:A2` : `A`
  - `V_AAA#3:A3` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T084

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAA` x 3, `V_A_lambda_lambdabar` x 1
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `1296`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAA#1:A1`
  - `V_AAA#1:A2` --[A]-- `V_AAA#2:A1`
  - `V_AAA#2:A2` --[A]-- `V_AAA#3:A1`
  - `V_AAA#3:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
- representative external ports:
  - `V_AAA#1:A3` : `A`
  - `V_AAA#2:A3` : `A`
  - `V_AAA#3:A3` : `A`
  - `V_A_lambda_lambdabar#1:lambdabar` : `lbar`

### T085

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAAA` x 1, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `8`
- automorphism order: `6`
- graph symmetry factor: `1/6`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_AAAA#1:A1` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAAA#1:A2` : `A`
  - `V_AAAA#1:A3` : `A`
  - `V_AAAA#1:A4` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T086

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAAA` x 1, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `8`
- automorphism order: `6`
- graph symmetry factor: `1/6`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_AAAA#1:A1` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAAA#1:A2` : `A`
  - `V_AAAA#1:A3` : `A`
  - `V_AAAA#1:A4` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T087

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAAA` x 1, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `24`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAAA#1:A1`
  - `V_AAAA#1:A2` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAAA#1:A3` : `A`
  - `V_AAAA#1:A4` : `A`
  - `V_A_lambda_lambdabar#2:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T088

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_AAAA` x 1, `V_A_lambda_lambdabar` x 2
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `24`
- automorphism order: `2`
- graph symmetry factor: `1/2`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_AAAA#1:A1`
  - `V_AAAA#1:A2` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
- representative external ports:
  - `V_AAAA#1:A3` : `A`
  - `V_AAAA#1:A4` : `A`
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`

### T089

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_A_lambda_lambdabar` x 4
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `24`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#1:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
  - `V_A_lambda_lambdabar#3:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#4:lambda`
- representative external ports:
  - `V_A_lambda_lambdabar#2:A` : `A`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#4:A` : `A`
  - `V_A_lambda_lambdabar#4:lambdabar` : `lbar`

### T090

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_A_lambda_lambdabar` x 4
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `24`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#2:lambda`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
  - `V_A_lambda_lambdabar#3:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#4:lambda`
- representative external ports:
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#4:A` : `A`
  - `V_A_lambda_lambdabar#4:lambdabar` : `lbar`

### T091

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_A_lambda_lambdabar` x 4
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `24`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
  - `V_A_lambda_lambdabar#2:lambda` --[fermion]-- `V_A_lambda_lambdabar#3:lambdabar`
  - `V_A_lambda_lambdabar#2:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#4:lambda`
- representative external ports:
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#4:A` : `A`
  - `V_A_lambda_lambdabar#4:lambdabar` : `lbar`

### T092

- total explicit order: `g^4`
- insertion term: `O21_A_dlb`
- action vertices: `V_A_lambda_lambdabar` x 4
- external fields: `['A', 'A', 'A', 'lbar']`
- raw Wick contraction multiplicity: `24`
- automorphism order: `1`
- graph symmetry factor: `1`
- representative internal contractions:
  - `O:Qf2_lambdabar` --[fermion]-- `V_A_lambda_lambdabar#1:lambda`
  - `O:f1_A` --[A]-- `V_A_lambda_lambdabar#2:A`
  - `V_A_lambda_lambdabar#1:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#3:lambda`
  - `V_A_lambda_lambdabar#2:lambda` --[fermion]-- `V_A_lambda_lambdabar#4:lambdabar`
  - `V_A_lambda_lambdabar#3:lambdabar` --[fermion]-- `V_A_lambda_lambdabar#4:lambda`
- representative external ports:
  - `V_A_lambda_lambdabar#1:A` : `A`
  - `V_A_lambda_lambdabar#2:lambdabar` : `lbar`
  - `V_A_lambda_lambdabar#3:A` : `A`
  - `V_A_lambda_lambdabar#4:A` : `A`
