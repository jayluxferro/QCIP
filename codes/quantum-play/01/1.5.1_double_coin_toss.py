"""
Double coin toss with a quantum circuit.

Two qubits, each put into an equal superposition with a Hadamard gate,
so the four outcomes |00>, |01>, |10>, |11> are (near-)equally likely.

@author: Jay (@jayluxferro)
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

q = QuantumRegister(2)
c = ClassicalRegister(2)

qc = QuantumCircuit(q, c)
qc.h(q[0])
qc.h(q[1])

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
