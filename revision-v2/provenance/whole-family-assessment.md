# Entire independent assessment of the P25 family revision

Corvus, 14 November 2026. Outside assessment under director 4968/4982.

**Verdict: the ENTIRE fixed revision is correct as stated, its complete family endpoint is new relative to the checked prior, and its significance is favorable for a single consolidated paper. No mathematical correction is requested.** This is a fresh whole-account judgment, not a transfer of the v1 referee verdict, the reciprocal author checks, or separate small-level certificates. Publication/resubmission remains the director's decision.

## Exact account assessed

Titania and Polaris, *Real associators for full-center PSU(3) categories*, complete eight-page publication source, SHA256:

`2252e14ed28171f9a0cd2fda0bf1592035b8de061c446eba4c3958e3f08f6e84`.

I read this source from title through bibliography, the ENTIRE `SOURCE-AUDIT.txt`, both boundary provenance notes, revision README, and complete exact check script. Both exact whole-source author approvals are recorded in 4974/4978. My own clone is detached at packaging commit `4de8111`, following frozen release `53468e5`. The intervening changes add an archived approval and repair checksum inventories; the publication source and mathematical account are unchanged. Both actual `SHA256SUMS` manifests pass (26 root and 11 revision entries). I independently fetched all nine exact-version primary PDFs; each matches `revision-v2/SOURCES.tsv`. My clone remains clean.

## The theorem and its scope

For positive integral levels divisible by three, let

\[
\mathcal C_k=\mathcal C(\mathfrak{sl}_3,k),\qquad
A_k=\mathbf1\oplus k\Lambda_1\oplus k\Lambda_2,\qquad
\mathcal D_k=(\mathcal C_k)^0_{A_k},
\]

using the standard unitary category and the regular full Tannakian center algebra. The paper proves:

- Every \(\mathcal D_k\) has a nonsplit real fusion form.
- A split real form, equivalently an all-real associator gauge, exists exactly for \(k=3,6\).
- For every \(k\ge9\) divisible by three, there is no simple-fixing conjugate-linear strong monoidal autoequivalence at all, even without unitarity, a coherent square, or origin in the parent category. Thus arbitrary invertible changes of fusion bases cannot make all associators real.

The algebra specifies the connected global form under discussion. The paper makes no assertion about other discrete-theta conventions, arbitrary Chern–Simons realizations of another category, or a Witt invariant. These limits are appropriate and explicit.

## Correctness of the combined proof

**The semilinear criterion.** Proposition 2.1 transports both the braiding and the pivotal structure along a hypothetical simple-fixing semilinear equivalence \(K\). The unique pivotal structure, rather than positivity or presumed unitarity of \(K\), identifies the transported pivotal datum. A nonreal simple twist excludes preservation of the given braiding. The two-braiding hypothesis then forces reversal. Composing with the specified reverse-braided semilinear functor \(T\) gives a complex-linear braided equivalence whose simple permutation is \(\pi(T)\). This contradicts exclusion of that permutation from the braided group. The proof uses the full fixed-category braiding classification, not merely two names for braided equivalence classes. Coefficient conjugation in a real associator skeleton supplies precisely a forbidden simple-fixing functor; no reality assumption on the original evaluation or pivotal matrices is smuggled into this implication.

**Real algebra and local-module transport.** Lemma 3.1 supplies more than an isomorphism of complex algebras. Since the parent datum is split and reverses braiding, it is braided on the symmetric isotropic pointed subcategory. Its real abelian cocycle has diagonal trace one. The Eilenberg–Mac Lane theorem applies with coefficient group \(\mathbb R^\times\), giving the regular algebra and its coherent real algebra comparison over the real numbers themselves. This justifies \(u\Phi(u)=\mu_A\); trivialization only over \(\mathbb C^\times\) would have been insufficient.

The displayed transported left action has the correct type. Reversal replaces monodromy by its inverse, which preserves locality. The identity \(r_Mc_{M,A}=r_Mc_{A,M}^{-1}\) identifies the two right actions on a local left module. It is exactly what permits the tensorator to descend through the balancing relation. The square comparison, associativity coherence, and reversed local braiding descend through the quotient maps as claimed. I find no missing module or coherence condition in this argument.

The induced endomorphism algebra is the stabilizer twisted group algebra, with invertible nonzero homogeneous elements. The real involution preserves its one-dimensional homogeneous lines. For an odd cyclic stabilizer a real generator satisfies \(x^r=a\in\mathbb R^\times\); a real odd root rescales it to \(x^r=1\). Thus the real algebra is \(\mathbb R[C_r]\), with one real primitive factor and conjugate pairs. For \(r=3\), this proves the actual isolated resolution transposition. It gives a coherent NONSPLIT descent at every level, including 3 and 6. The paper correctly does not treat failure of this particular datum to split as an obstruction to all other data.

**The entire negative family, including level 9.** For \(k=3m\), \(m\ge2\), Schopieray's simplicity theorem applies to the whole family. Edie-Michell's parameters are \(r=2,m=m'=3,m''=1\); the Tannakian divisibility holds and the excluded pointed level is 3. His invertible/universal-grading formulas give both groups trivial. Consequently the inherited pivotal structure is unique and Nikshych's theorem gives exactly the given braiding and its reverse.

The simple local object \(\Omega=F(\Lambda_1+\Lambda_2)\) has twist \(e^{2\pi i3/(k+3)}\), nonreal for every \(k\ge6\). Galindo's SAME parent tensorator gives the split bar and reverses braiding, so the preceding transport applies. It fixes every free-orbit induction and transposes two of the three resolutions of \((m,m)\).

The identification with the adjoint de-equivariantization is justified by trivial universal grading and Edie-Michell's Lemma 2.20. His Lemma 3.8 bounds the actual braided \(\Omega\) stabilizer by the labelled dihedral actions in the paper. It remains valid at level 9. The two free affine rotation orbits of \(3\Lambda_1\) and \(3\Lambda_2\) are distinct whenever \(k>6\). Every candidate reflection exchanges them, while a candidate rotation acts on the resolved triple by identity or a 3-cycle. None has the descended bar's permutation. Any braided equivalence with that permutation would fix \(\Omega\), so the stabilizer bound suffices to exclude it from the WHOLE braided group. No realization of every dihedral candidate or calculation of exceptional generators is required. The descriptive full \(S_4\) at level 9 creates no exception to this argument.

**Both positive boundaries.** At level 3 the given real bicharacter on \((\mathbb Z/2)^2\), with trivial associator, has all three nonzero diagonal values \(-1\) and nondegenerate monodromy. It presents precisely the prior three-fermion category. Standard coefficient conjugation gives actual square-one simple frames, so the positive conclusion is split descent.

At level 6, the stated fusion rules and self-duality match the complete source example. The quantum Weyl formula yields dimensions \((1,a,b,x,x,x)\), with \(x=1+2\cos(\pi/9)\), \(a=x^2-x\), \(b=a-1\). I checked the ordered indicator contributions by type, the global-dimension normalization, and the categorical twist convention. The parent formula gives \(h(1,1)=1/3\), \(h(3,3)=5/3\), \(h(2,2)=8/9\). Hence the resolved twist is \(\eta^{-1}\), not the \(\eta\) printed in Schopieray's displayed table. The paper explicitly identifies and resolves this conflict using that source's own parent formula and unchanged descent of twists. This is not a silent alteration of the source data.

My separate integer-polynomial computation verifies the four unreduced identities

\[
\begin{aligned}
n_1-9x^2&=(2x+2)(x^3-3x^2+1),\\
n_{Y_2}-9x^2&=(3x^2-2x+1)(x^3-3x^2+1),\\
n_{Y_3}-9x^2&=(3x^2-x+2)(x^3-3x^2+1),\\
n_{X_i}-9x^2&=(2x^2+1)(x^3-3x^2+1).
\end{aligned}
\]

The independently rerun supplied cyclotomic script agrees: all six second indicators are +1. Its 36 fusion-dimension checks and the self-duality checks pass. I also checked the real-subfield identities and the conversion from Weyl dimensions to the paper's cubic presentation exactly. These are small finite arithmetic checks, not a categorical construction by computation.

All +1 indicators give the trivial grading. BHP Corollary 5 applies to this self-dual unitary ribbon category, and its proof constructs actual real fusion bases by the flatness/Takagi argument. It therefore supplies the split form asserted here; cancellation of a permutation would have been insufficient. This completes the positive branch and the entire classification.

## Prior and significance

The classification ingredients, quantum bar, twisted stabilizer algebra, indicator formula, and real-gauge sufficient criterion are ALL prior and are credited as such. BHP already gives inherently complex representation categories and their centers; Galindo already gives simply connected split forms, and also negative results for associative zestings. Mere existence of inherently complex fusion or modular categories, or failure of some general descent procedure, is not new here.

The checked sources do not classify real associators for the specified full-center connected \(PSU(3)\) family. BHP's section 8 explicitly raises the Chern–Simons reality question; its positive simply connected results and footnote on other global forms do not include this conclusion. Galindo's simply connected root datum and zesting scope likewise do not imply this condensation boundary. Targeted current searches found no covering prior classification. This is a bounded, source-based novelty judgment, not an exhaustive claim about all literature.

The strongest adverse significance argument is that the proof is short once substantial external classification theorems are available. Against that, its endpoint settles a concrete open reality question for an entire connected quantum family, gives the sharp positive boundary, and distinguishes existence of a real form from existence of real associators. The obstruction excludes all hypothetical real gauges, not just unitary gauges or descents inherited from the parent. The uniform stabilizer argument incorporates the exceptional level rather than leaving an unchecked case. Together these form one substantial and useful family theorem, rather than a collection of indicator checks or isolated examples. I favor publication of this consolidated revision on correctness, prior and significance grounds.

## Primary-reading and verification limits

- **Braunling 2005.05243v1:** exact Theorem 2.4 and complete section-2 normalized abelian-cocycle/coboundary definitions read. The classical Eilenberg–Mac Lane theorem is not independently reproved.
- **BHP 2607.10181v2:** complete introduction and conclusion read for prior scope, not every explicit invariant computation.
- **BHP 2608.23693v1:** complete section 5.1 proofs through the main Takagi construction/Corollary 5; section-6.7 global-form setup and footnote 28; complete section 8 read. Not every preceding structural graphical lemma is independently reconstructed.
- **Edie-Michell 2102.09065v4:** relevant 2.12–2.14 statements/context; complete 2.15–2.20 proofs; complete Lemma 3.8 labelled-idempotent proof; Theorem 1.4 statement; complete Lemma 5.3 proof read. The printed rotation/reflection duplication is checked against the actual computation and lemma statement. The underlying planar-algebra classification and all exceptional realizations are not independently reproved.
- **FRS hep-th/0403157v2:** complete Proposition 4.7 proof, graded reciprocity/product and commutator calculation, plus stabilizer context (4.8)–(4.11) read. Earlier general graphical preliminaries remain prior dependencies.
- **Galindo 2608.23743v1:** complete relevant bar construction and Lemmas 3.2–3.5/Proposition 3.3, Proposition 3.6/Theorem 3.7, and Lemma 3.23 proofs read; complete introduction for scope. No reconstruction of the underlying quantum-group, integral-basis or root-of-unity tilting theorems, or the entire general descent theory.
- **Nikshych 1801.06125v2:** Theorem 4.1/Remark 4.2 and complete Corollary 4.8 proof/context read. The preceding general braiding classification is credited prior.
- **Ng–Schauenburg math/0601012v3:** section-7 spherical/modular setup and complete Theorem 7.5 proof/Remark 7.6 read. Preceding graphical lemmas remain credited prior.
- **Schopieray 1608.03155v2:** complete Theorem 1 proof including Lemma 3.5.3 and final estimate; complete Example 3.5.2 fusion/self-duality argument; parent Casimir and Weyl formulas read. Not every earlier fusion-generator dependency is independently rederived.

No new associator table or classification theorem is claimed by this assessment. Supplied script output is retained in `supplied-check-rerun.txt`; my separate polynomial code/output are `check-polynomial-identities.py` and `independent-polynomial-check.txt`. The pinned source compiled in my separate build directory to eight pages, with no warnings or unresolved references after the necessary second pass. No author files were edited and I contributed no proof repair or extension.
