"""
Single coin toss with a quantum circuit.

A coin toss is a 50-50 event. Applying a Hadamard gate puts a qubit into
the equal superposition |+> = (|0> + |1>)/sqrt(2), so measuring yields
|0> and |1> with equal probability.

@author: Jay (@jayluxferro)
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

q = QuantumRegister(1)
c = ClassicalRegister(1)

qc = QuantumCircuit(q, c)
qc.h(q[0])  # Hadamard -> equal superposition

qc.measure(q, c)

qc.draw("mpl")
plt.show()

simulator = AerSimulator()
qc = transpile(qc, simulator)  # optimize for the target backend
qc.draw("mpl")
plt.show()

job = simulator.run([qc], shots=1024)
results = job.result()
iterations = results.results[0].shots
print(f"Iterations: {iterations}")

counts = results.get_counts(qc)
print(f"Counts: {counts}")
plot_histogram(counts)
plt.show()

print("Probability of 0: ", counts["0"] / iterations)
print("Probability of 1: ", counts["1"] / iterations)
