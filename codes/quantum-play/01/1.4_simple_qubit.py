"""
Build and measure a simple single-qubit circuit.

Applies an X gate to flip |0> to |1>, measures, and runs on the
AerSimulator to confirm the outcome.

@author: Jay (@jayluxferro)
"""

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

q = QuantumRegister(1)
c = ClassicalRegister(1)

qc = QuantumCircuit(q, c)
qc.x(q[0])  # flip from |0> to |1>

qc.measure(q, c)

qc.draw("mpl")
plt.show()

# Initialize simulator and run the circuit.
simulator = AerSimulator()
job = simulator.run(qc)

results = job.result()
iterations = results.results[0].shots
print(iterations)

counts = results.get_counts(qc)
print(counts)
plot_histogram(counts)
plt.show()

print("Probability of 1: ", counts["1"] / iterations)
