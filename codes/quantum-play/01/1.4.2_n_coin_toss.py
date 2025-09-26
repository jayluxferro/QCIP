"""
'n' coin toss
"""

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator

n = int(input("Enter n: "))

q = QuantumRegister(n)
c = ClassicalRegister(n)

qc = QuantumCircuit(q, c)
for i in range(n):  # 0, 1
    qc.h(q[i])  # qc.h(q[0]) qc.h(q[1])

# Measurement
qc.measure(q, c)

qc.draw("mpl", filename=f"{n}_coin_toss_circuit.jpg")
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
