"""
Quantum phase estimation.

Estimates the phase φ of an eigenvector of a unitary U (where U|ψ> =
e^(2πiφ)|ψ>). Here we estimate the phase of the single-qubit phase gate
acting on |1>, using three counting qubits.

@author: Jay (@jayluxferro)
"""

import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


def phase_estimation(n_count: int, phi: float) -> QuantumCircuit:
    """Estimate the phase phi using n_count counting qubits and one target."""
    qc = QuantumCircuit(n_count + 1, n_count)

    qc.x(n_count)  # target |1> is an eigenvector of the phase gate
    qc.h(range(n_count))

    # Apply controlled-U^(2^k), where U = phase gate with angle 2πφ.
    for k in range(n_count):
        qc.cp(2 * np.pi * phi * (2**k), k, n_count)

    # Inverse QFT on the counting qubits.
    qc.compose(QFT(n_count).inverse().decompose(), range(n_count), inplace=True)
    qc.measure(range(n_count), range(n_count))
    return qc


n_count = 3
phi = 3 / 8  # 0.375 = 0.011 in binary, exactly representable with 3 bits

qc = phase_estimation(n_count, phi)
qc.draw("mpl")
plt.show()

sim = AerSimulator()
counts = sim.run(qc, shots=2048).result().get_counts(qc)
print(counts)
plot_histogram(counts)
plt.show()

# The measured integer, divided by 2^n_count, recovers the phase.
outcome = max(counts, key=counts.get)
estimated = int(outcome, 2) / 2**n_count
print(f"True phase: {phi}")
print(f"Measured binary: {outcome} -> estimated phase: {estimated}")
print(f"Exact: {abs(estimated - phi) < 1e-9}")
