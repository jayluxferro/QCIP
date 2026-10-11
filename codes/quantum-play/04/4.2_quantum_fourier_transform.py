"""
Quantum Fourier Transform.

The QFT is the quantum analogue of the discrete Fourier transform and is the
core of phase estimation and Shor's algorithm.

@author: Jay (@jayluxferro)
"""

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

n = 4
qc = QuantumCircuit(n, n)
qc.x(0)  # input state |1> (binary 0001)
qc.barrier()
qc.compose(QFT(n).decompose(), range(n), inplace=True)
qc.measure(range(n), range(n))

qc.draw("mpl")
plt.show()

sim = AerSimulator()
counts = sim.run(qc, shots=2048).result().get_counts(qc)
print(counts)
plot_histogram(counts)
plt.show()
