"""
Tensor products of qubit states (Kronecker product).

The tensor product combines independent quantum systems: the state of two
independent qubits is the tensor product of their individual states. Gates
acting on a subset of qubits are tensor products of single-qubit gates with
the identity.

@author: Jay (@jayluxferro)
"""

import numpy as np

zero = np.array([1, 0])
one = np.array([0, 1])

# Two-qubit basis states are tensor products of single-qubit basis states.
ket_00 = np.kron(zero, zero)
ket_01 = np.kron(zero, one)
ket_10 = np.kron(one, zero)
ket_11 = np.kron(one, one)

print("|00> =", ket_00)
print("|01> =", ket_01)
print("|10> =", ket_10)
print("|11> =", ket_11)

# |++> = |+> ⊗ |+> is the uniform superposition over two qubits.
plus = (zero + one) / np.sqrt(2)
ket_pp = np.kron(plus, plus)
print("|++> =", ket_pp)

# A gate on the first qubit only is X ⊗ I (act on qubit 0, identity on qubit 1).
X = np.array([[0, 1], [1, 0]])
I = np.eye(2)
X_on_first = np.kron(X, I)
print("X ⊗ I =\n", X_on_first)
print("(X ⊗ I)|00> =", X_on_first @ ket_00)  # flips the first qubit -> |10>
