"""
Double coin toss
"""

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator

q = QuantumRegister(2)
c = ClassicalRegister(2)

qc = QuantumCircuit(q, c)
qc.h(q[0])
qc.h(q[1])

# Measurement
qc.measure(q, c)

qc.draw("mpl", filename="double_coin_toss_circuit.jpg")
plt.show()

# Initialize simulator
sim = AerSimulator()

job = sim.run(qc, shots=2048)  # number of iterations
result = job.result()
iteration = result.results[0].shots
print(iteration)

# counts
counts = result.get_counts(qc)  # give us the counts for each basis

print(counts)
plot_histogram(counts)
plt.show()
