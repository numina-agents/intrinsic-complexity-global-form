"""Exact small verification for the standard unitary full-center sl3 level 6.

Fusion rules: Schopieray, arXiv:1608.03155v2, Example 3.5.2.
Dimensions/twists are descended from the parent's quantum Weyl/Casimir formulas.
Indicator formula: Ng--Schauenburg, math/0601012, Theorem 7.5, n=2.
No floating point recognition is used. q is a primitive 18th root with Phi18(q)=0.
"""
from fractions import Fraction as Q

ZERO = (Q(0),) * 6
ONE = (Q(1),) + (Q(0),) * 5


def scalar(n):
    return (Q(n),) + (Q(0),) * 5


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def mul(a, b):
    c = [Q(0)] * 11
    for i in range(6):
        for j in range(6):
            c[i + j] += a[i] * b[j]
    # q^6 = q^3 - 1.
    for i in range(10, 5, -1):
        c[i - 3] += c[i]
        c[i - 6] -= c[i]
    return tuple(c[:6])


def power(a, n):
    if n < 0:
        return power(inv(a), -n)
    b = ONE
    while n:
        if n & 1:
            b = mul(b, a)
        a = mul(a, a)
        n //= 2
    return b


def inv(a):
    columns = [mul(a, tuple(Q(i == j) for i in range(6))) for j in range(6)]
    rows = [[columns[j][i] for j in range(6)] + [Q(i == 0)] for i in range(6)]
    for j in range(6):
        pivot = next(i for i in range(j, 6) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        u = rows[j][j]
        rows[j] = [x / u for x in rows[j]]
        for i in range(6):
            if i != j:
                u = rows[i][j]
                rows[i] = [x - u * y for x, y in zip(rows[i], rows[j])]
    answer = tuple(rows[i][6] for i in range(6))
    assert mul(a, answer) == ONE
    return answer


def total(xs):
    answer = ZERO
    for x in xs:
        answer = add(answer, x)
    return answer


q = (Q(0), Q(1), Q(0), Q(0), Q(0), Q(0))
assert power(q, 18) == ONE and power(q, 9) == scalar(-1)


def qi(n):
    return total(power(q, j % 18) for j in range(n - 1, -n, -2))


# Labels: 1, Y2=F(1,1), Y3=F(3,3), X0, X1, X2.
d = [ONE, mul(qi(2), qi(4)), mul(power(qi(4), 2), inv(qi(2)))]
resolved_dim = mul(power(qi(3), 3), inv(mul(scalar(3), qi(2))))
d += [resolved_dim] * 3

N = [[[0] * 6 for _ in range(6)] for _ in range(6)]


def product(i, j, terms):
    for label, multiplicity in terms.items():
        N[i][j][label] = N[j][i][label] = multiplicity


for i in range(6):
    product(0, i, {i: 1})
product(1, 1, {0: 1, 1: 2, 2: 2, 3: 1, 4: 1, 5: 1})
product(1, 2, {1: 2, 2: 1, 3: 1, 4: 1, 5: 1})
product(2, 2, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
for i in range(3, 6):
    product(1, i, {1: 1, 2: 1, **{j: 1 for j in range(3, 6) if j != i}})
    product(2, i, {1: 1, 2: 1, i: 1})
    product(i, i, {0: 1, 2: 1, i: 1})
    for j in range(i + 1, 6):
        k = 12 - i - j
        product(i, j, {1: 1, k: 1})

for i in range(6):
    for j in range(6):
        assert mul(d[i], d[j]) == total(mul(scalar(N[i][j][k]), d[k]) for k in range(6))
        assert N[i][j][0] == (i == j)

global_dim = total(mul(x, x) for x in d)


def indicators(exponents):
    theta = [power(q, n) for n in exponents]
    answer = []
    for k in range(6):
        numerator = total(
            mul(scalar(N[i][j][k]), mul(mul(d[i], d[j]), power(q, (2 * (exponents[i] - exponents[j])) % 18)))
            for i in range(6) for j in range(6)
        )
        answer.append(mul(numerator, inv(global_dim)))
    return answer


nu = indicators([0, 6, 12, 16, 16, 16])
print('Basis: 1,q,q^2,q^3,q^4,q^5; Phi18(q)=q^6-q^3+1')
print('Exact dimensions:', d)
print('Global dimension:', global_dim)
print('Standard parent-descended second indicators:', nu)
assert nu == [ONE] * 6
print('All six second indicators are +1; BHP Corollary 5 applies.')

# Source-table audit only: the displayed +1/9 resolved twist conflicts with
# the same paper's parent Casimir formula, which gives 8/9 at (2,2).
table_nu = indicators([0, 6, 12, 2, 2, 2])
print('Indicators from the displayed +1/9 resolved twist:', table_nu)
print('That table satisfies the required +/-1 condition:', all(x in (ONE, scalar(-1)) for x in table_nu))
