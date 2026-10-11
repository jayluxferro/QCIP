"""
Reversible logic: the Toffoli gate.

Classical gates like AND and XOR are irreversible (they destroy information).
The Toffoli (controlled-controlled-NOT) gate is reversible — applying it
twice restores the input — and is universal for reversible computation.

@author: Jay (@jayluxferro)
"""


def toffoli(a: int, b: int, c: int) -> tuple:
    """Flip the target c iff both controls a and b are 1."""
    return (a, b, c ^ (a & b))


print("Toffoli truth table (a, b, c) -> (a, b, c XOR (a AND b)):")
for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            print(f"  ({a},{b},{c}) -> {toffoli(a, b, c)}")

# Toffoli is its own inverse: applying it twice restores the input.
print("\nReversibility check (Toffoli twice == identity):")
for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            twice = toffoli(*toffoli(a, b, c))
            assert twice == (a, b, c), f"failed on {(a, b, c)}"
print("  all 8 cases reversible ✓")

# Toffoli computes AND when the target starts at 0.
print("\nToffoli as reversible AND (c=0):")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"  ({a},{b},0) -> target {toffoli(a, b, 0)[2]}  (= a AND b)")
