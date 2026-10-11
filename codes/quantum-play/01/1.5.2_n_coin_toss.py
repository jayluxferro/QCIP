"""
'n' coin toss with a quantum circuit.

Generalizes the coin toss to `n` coins (qubits), each in equal
superposition. There are 2^n equiprobable outcomes.

@author: Jay (@jayluxferro)
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

n = int(input("Enter n: "))

q = QuantumRegister(n)
c = ClassicalRegister(n)

qc = QuantumCircuit(q, c)
for i in range(n):
    qc.h(q[i])

qc.measure(q, c)

qc.draw("mpl")
plt.show()

sim = AerSimulator()
job = sim.run(qc, shots=2048)
result = job.result()
iterations = result.results[0].shots
print(iterations)

counts = result.get_counts(qc)
print(counts)
plot_histogram(counts)
plt.show()
