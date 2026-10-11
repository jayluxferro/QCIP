"""
Prepare and measure the GHZ state (|000> + |111>)/√2.

The GHZ state generalizes the Bell pair to three (or more) qubits: a single
Hadamard plus a chain of CNOT gates entangles all qubits.

@author: Jay (@jayluxferro)
"""

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

n = 3
qc = QuantumCircuit(n, n)
qc.h(0)
for i in range(1, n):
    qc.cx(0, i)
qc.measure(range(n), range(n))

qc.draw("mpl")
plt.show()

sim = AerSimulator()
counts = sim.run(qc, shots=2048).result().get_counts(qc)
print(counts)
plot_histogram(counts)
plt.show()
