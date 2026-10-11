"""
Linear algebra foundations for quantum computing.

Covers vectors, normalization, inner products, outer products, and matrix
action on vectors — the math underlying qubit states and quantum gates.

@author: Jay (@jayluxferro)
"""

import numpy as np


def norm(v: np.ndarray) -> float:
    """Euclidean norm (length) of a vector."""
    return float(np.linalg.norm(v))


# Computational basis states |0> and |1>.
zero = np.array([1, 0])
one = np.array([0, 1])

# Equal superposition |+> = (|0> + |1>)/sqrt(2).
plus = (zero + one) / np.sqrt(2)
print("|+> =", plus)

# A valid quantum state must be normalized.
print("norm(|+>) =", norm(plus))

# Inner product <0|+> gives the amplitude of |0> in |+>.
print("<0|+> =", np.vdot(zero, plus))

# Outer products |0><0| and |1><1| are projectors onto the basis states.
print("|0><0| =\n", np.outer(zero, zero))
print("|1><1| =\n", np.outer(one, one))

# A gate acts on a state by left multiplication. X flips |0> <-> |1>.
X = np.array([[0, 1], [1, 0]])
print("X|0> =", X @ zero)
print("X|1> =", X @ one)

# Hadamard creates a superposition from a basis state.
H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])
print("H|0> =", H @ zero)
print("H|1> =", H @ one)
