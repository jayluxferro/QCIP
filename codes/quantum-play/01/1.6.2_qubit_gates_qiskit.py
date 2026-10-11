"""
Quantum gates in Qiskit and their effect on qubit states.

Demonstrates single-qubit (X, H) and multi-qubit (CX, Toffoli) gates
on the AerSimulator.

@author: Jay (@jayluxferro)
"""

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from numpy import sqrt


def run_and_plot(qc: QuantumCircuit, shots: int = 1024) -> None:
    sim = AerSimulator()
    qc = transpile(qc, sim)
    qc.draw("mpl")
    plt.show()
    job = sim.run(qc, shots=shots)
    counts = job.result().get_counts(qc)
    plot_histogram(counts)
    plt.show()


# Single-qubit gate: X flips |0> to |1>.
qc = QuantumCircuit(1, 1)
qc.x(0)
qc.measure(0, 0)
run_and_plot(qc)

# Single-qubit gate: H on the superposition (|0> - |1>)/sqrt(2).
qc = QuantumCircuit(1, 1)
qc.initialize([1 / sqrt(2), -1 / sqrt(2)], [0])
qc.h(0)
qc.measure(0, 0)
run_and_plot(qc, shots=8192)

# Multi-qubit gate: CX (CNOT).
qc = QuantumCircuit(2, 2)
qc.initialize([0, 1], [0])
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])
run_and_plot(qc)

# Multi-qubit gate: Toffoli (relative-phase CCX) with three qubits.
q = QuantumRegister(3)
c = ClassicalRegister(1)
qc = QuantumCircuit(q, c)
qc.initialize([0, 1], [q[2]])
qc.rccx(q[0], q[1], q[2])
qc.measure(q[2], c)
run_and_plot(qc)
