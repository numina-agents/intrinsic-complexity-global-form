"""Exact finite checks used in the paper; no categorical classification is computed."""
from itertools import permutations

def rotate(t):
    return t[2], t[0], t[1]

def orbit(t):
    return frozenset((t, rotate(t), rotate(rotate(t))))

neutral = {(12-a-b, a, b) for a in range(13) for b in range(13-a)
           if (a+2*b) % 3 == 0}
assert len(neutral) == 31
fixed = {t for t in neutral if rotate(t) == t}
assert fixed == {(4, 4, 4)}
free = {orbit(t) for t in neutral - fixed}
assert len(free) == 10 and all(len(o) == 3 for o in free)
assert len(free) + 3 == 13
v, vd = orbit((9, 3, 0)), orbit((9, 0, 3))
assert v in free and vd in free and v.isdisjoint(vd)

# Recorded labelled actions from Edie-Michell, not a computation of EqBr.
free_order = sorted(free, key=lambda o: sorted(o))
labels = list(range(13))
rotation = tuple(list(range(10)) + [11, 12, 10])
reflection = tuple(
    [free_order.index(orbit((t[0], t[2], t[1])))
     for o in free_order for t in [min(o)]] + [10, 12, 11])

def compose(a, b):
    return tuple(a[b[i]] for i in labels)

ident = tuple(labels)
rotations = (ident, rotation, compose(rotation, rotation))
dihedral = set(rotations) | {compose(r, reflection) for r in rotations}
assert len(dihedral) == 6
for p in permutations(range(3)):
    if sum(p[j] != j for j in range(3)) == 2:
        isolated = tuple(list(range(10)) + [10+j for j in p])
        assert isolated not in dihedral
print("31 neutral weights; 10 free orbits; rank 13; all isolated transpositions excluded.")
