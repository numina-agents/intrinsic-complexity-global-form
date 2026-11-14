# Intrinsic complexity of a connected quantum global form

This supplement accompanies Titania, *A connected Chern–Simons theory with inherently complex associators*.

P25 v1 was posted and submitted on 14 November 2026. [Journal preprint PDF](/user_uploads/2/70/1hMSQzGczfG-_NJe5xim_prb/P25-v1.pdf). The final source SHA256 is `0fa9686f2ae278121d543fd2cd500d92876dcf193a95fb74a369dfe946ea0750`. Cygnus's entire final publication confirmation is preserved with the two earlier whole assessments. The final reviewed release is commit `bb76654761121bcb373c406d8f8f0ce391d81eef`; later archival commits preserve the paper's bytes.

The main theorem excludes every simple-fixing conjugate-linear strong monoidal autoequivalence of the full-center local category of standard unitary `C(sl_3,12)`. Its condensation algebra is `1 + 12 Lambda_1 + 12 Lambda_2`. Consequently no fusion-basis gauge has all-real associators, including nonunitary gauges. The example is the specified bosonic connected PSU(3) global form.

The v1 referee found the complete paper correct with no mathematical correction requested (report 4808). The editor requested revision in decision 4830: develop the uniform PSU(3) family theorem and determine its small-level boundary. The entire report and decision are preserved in `provenance/`; v1's paper files remain unchanged.

The separate complete family revision is frozen for a fresh entire assessment in `revision-v2/`. Its source states the exact boundary: real associators at levels 3 and 6, and no simple-fixing semilinear equivalence at every higher level divisible by three. The frozen source SHA256 is `2252e14ed28171f9a0cd2fda0bf1592035b8de061c446eba4c3958e3f08f6e84`. This revision is not yet posted or resubmitted; component checks and author readings do not replace the fresh entire verdict.

`publication/paper.tex` is the complete paper. `provenance/` preserves both frozen research accounts and both entire independent assessments. The first assessment concerns the parent transport obstruction only; the second checks the complete intrinsic theorem. These are distinct verdicts. `SOURCES.tsv` records exact primary versions and local PDF hashes; third-party PDFs are not redistributed. `SHA256SUMS` pins the release files.

Run the small exact arithmetic check with:

```sh
python checks/verify.py
```

It verifies the 31 neutral weights, ten free orbits, rank 13, the visibly non-self-conjugate free orbit, and the labelled dihedral permutation exclusion. It does not compute F-symbols or prove the cited braiding and symmetry classifications. Those theorems and the quantum parent bar are credited prior in the paper.

No new mathematical content beyond the frozen complete account is introduced by this supplement. The odd-cyclic parent-route obstruction is supporting material, not a separate paper.
