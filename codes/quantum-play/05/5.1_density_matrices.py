"""
Density matrices, mixed states, and purity.

A pure state has a rank-1 density matrix ρ = |ψ><ψ| with purity Tr(ρ²) = 1.
A mixed state is a probabilistic mixture of pure states; its purity is < 1.
For a single qubit, the Bloch vector r = (⟨X⟩, ⟨Y⟩, ⟨Z⟩) has |r| = 1 for a
pure state and |r| < 1 for a mixed state (inside the Bloch ball).

@author: Jay (@jayluxferro)
"""

import numpy as np

zero = np.array([1, 0])
one = np.array([0, 1])

# Pure state |+>.
plus = (zero + one) / np.sqrt(2)
rho_pure = np.outer(plus, plus)
print("rho_|+> =\n", rho_pure)
print("purity Tr(rho^2) =", float(np.trace(rho_pure @ rho_pure)))

# Mixed state: 50% |0>, 50% |1>.
rho_mixed = 0.5 * np.outer(zero, zero) + 0.5 * np.outer(one, one)
print("\nrho_mixed =\n", rho_mixed)
print("purity Tr(rho^2) =", float(np.trace(rho_mixed @ rho_mixed)))

# Pauli matrices.
X = np.array([[0, 1], [1, 0]])
Y = np.array([[0, -1j], [1j, 0]])
Z = np.array([[1, 0], [0, -1]])

print("\nBloch vectors:")
for name, rho in [("|+> (pure)", rho_pure), ("50/50 (mixed)", rho_mixed)]:
    r = np.array([
        np.trace(rho @ X).real,
        np.trace(rho @ Y).real,
        np.trace(rho @ Z).real,
    ])
    print(f"{name}: r = {np.round(r, 3)}, |r| = {np.linalg.norm(r):.3f}  (1 = pure, <1 = mixed)")
