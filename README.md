# Intrinsic complexity of a connected quantum global form

This supplement accompanies Titania, *A connected Chern–Simons theory with inherently complex associators*.

The main theorem excludes every simple-fixing conjugate-linear strong monoidal autoequivalence of the full-center local category of standard unitary `C(sl_3,12)`. Its condensation algebra is `1 + 12 Lambda_1 + 12 Lambda_2`. Consequently no fusion-basis gauge has all-real associators, including nonunitary gauges. The example is the specified bosonic connected PSU(3) global form.

`publication/paper.tex` is the complete paper. `provenance/` preserves both frozen research accounts and both entire independent assessments. The first assessment concerns the parent transport obstruction only; the second checks the complete intrinsic theorem. These are distinct verdicts. `SOURCES.tsv` records exact primary versions and local PDF hashes; third-party PDFs are not redistributed. `SHA256SUMS` pins the release files.

Run the small exact arithmetic check with:

```sh
python checks/verify.py
```

It verifies the 31 neutral weights, ten free orbits, rank 13, the visibly non-self-conjugate free orbit, and the labelled dihedral permutation exclusion. It does not compute F-symbols or prove the cited braiding and symmetry classifications. Those theorems and the quantum parent bar are credited prior in the paper.

No new mathematical content beyond the frozen complete account is introduced by this supplement. The odd-cyclic parent-route obstruction is supporting material, not a separate paper.
