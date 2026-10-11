"""
Bell inequality (CHSH) violation.

Local hidden-variable theories bound |S| <= 2. A maximally entangled state
measured in suitably rotated bases reaches |S| = 2√2 ≈ 2.828, violating the
bound and ruling out local realism.

@author: Jay (@jayluxferro)
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def chsh_circuit(theta: float, phi: float) -> QuantumCircuit:
    """Bell pair |Φ+> measured in bases rotated by theta (q0) and phi (q1)."""
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.ry(theta, 0)
    qc.ry(phi, 1)
    qc.measure([0, 1], [0, 1])
    return qc


def correlation(theta: float, phi: float, sim: AerSimulator, shots: int = 8192) -> float:
    """E(theta, phi) = P(00) + P(11) - P(01) - P(10)."""
    qc = chsh_circuit(theta, phi)
    counts = sim.run(qc, shots=shots).result().get_counts(qc)
    total = sum(counts.values())
    return (
        counts.get("00", 0) + counts.get("11", 0)
        - counts.get("01", 0) - counts.get("10", 0)
    ) / total


sim = AerSimulator()

# Measurement settings: Alice in {0, π/2}, Bob in {π/4, 3π/4}.
a = [0, np.pi / 2]
b = [np.pi / 4, 3 * np.pi / 4]

results = {}
for theta in a:
    for phi in b:
        e = correlation(theta, phi, sim)
        results[(theta, phi)] = e
        print(f"E(theta={theta:.3f}, phi={phi:.3f}) = {e:+.3f}")

# CHSH combination: S = E(a,b) - E(a,b') + E(a',b) + E(a',b').
s = (
    results[(a[0], b[0])] - results[(a[0], b[1])]
    + results[(a[1], b[0])] + results[(a[1], b[1])]
)

print(f"\nS = {s:.3f}")
print("Local-realist bound: |S| <= 2")
print(f"Quantum prediction:  |S| = 2√2 ≈ {2 * np.sqrt(2):.3f}")
print(f"Violation: {abs(s) > 2}")
