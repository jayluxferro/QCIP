"""
Build and run multi-qubit circuits in Qiskit.

Contrasts an independent superposition (two Hadamards) with an entangled
state (Hadamard + CNOT).

@author: Jay (@jayluxferro)
"""

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


def run_and_plot(qc: QuantumCircuit, shots: int = 1024) -> None:
    sim = AerSimulator()
    counts = sim.run(qc, shots=shots).result().get_counts(qc)
    print(counts)
    plot_histogram(counts)
    plt.show()


q = QuantumRegister(2)
c = ClassicalRegister(2)

# Independent superposition: all four outcomes equally likely.
qc = QuantumCircuit(q, c)
qc.h(q[0])
qc.h(q[1])
qc.measure(q, c)
qc.draw("mpl")
plt.show()
run_and_plot(qc)

# Entangling circuit: H on q0 then CNOT -> Bell state |Φ+>.
qc = QuantumCircuit(q, c)
qc.h(q[0])
qc.cx(q[0], q[1])
qc.measure(q, c)
qc.draw("mpl")
plt.show()
run_and_plot(qc)
