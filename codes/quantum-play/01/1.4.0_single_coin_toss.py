"""
Single coin toss
"""

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator

q = QuantumRegister(1)
c = ClassicalRegister(1)

qc = QuantumCircuit(q, c)
qc.h(q[0])

# measurement
qc.measure(q, c)

qc.draw("mpl", filename="single_coin_toss.jpg")  # text, latex, latex_source, and mpl
plt.show()

# initialize our simulator / backend
simulator = AerSimulator()

# run the circuit on the simulator
job = simulator.run(qc)

# get the results
results = job.result()
iterations = results.results[0].shots
print(iterations)  # number of iterations (shots)

# counts
counts = results.get_counts(qc)  # give us the counts for each basis

print(counts)
plot_histogram(counts)
plt.show()

print("Probability of 0: ", counts["0"] / iterations)
print("Probability of 1: ", counts["1"] / iterations)
