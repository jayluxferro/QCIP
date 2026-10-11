"""
Multi-qubit states, normalization, and an entanglement test.

An n-qubit state is a normalized vector in 2^n dimensions. A product state
|a>⊗|b> can be separated into independent single-qubit states; an entangled
state such as the Bell state |Φ+> = (|00> + |11>)/√2 cannot.

@author: Jay (@jayluxferro)
"""

import numpy as np

zero = np.array([1, 0])
one = np.array([0, 1])

# Two-qubit computational basis states.
basis = {
    "|00>": np.kron(zero, zero),
    "|01>": np.kron(zero, one),
    "|10>": np.kron(one, zero),
    "|11>": np.kron(one, one),
}
for name, vec in basis.items():
    print(f"{name} = {vec}")

# The Bell state |Φ+> is maximally entangled.
bell_phi_plus = (basis["|00>"] + basis["|11>"]) / np.sqrt(2)
print("\n|Φ+> =", bell_phi_plus)
print("norm(|Φ+>) =", float(np.linalg.norm(bell_phi_plus)))

# Entanglement test: reshape the 4-vector to a 2x2 matrix and check its rank.
# A product state reshapes to a rank-1 matrix; an entangled state has rank > 1.
print("\nrank(|Φ+> as 2x2) =", np.linalg.matrix_rank(bell_phi_plus.reshape(2, 2)))
print("rank(|00> as 2x2) =", np.linalg.matrix_rank(basis["|00>"].reshape(2, 2)))
print("(rank > 1 means the state is entangled)")
