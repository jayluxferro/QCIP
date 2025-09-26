from qiskit import (
    qasm2 as qasm,
)  # use qasm3 for v3.0
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# Import quantum circuit from QASM file
qc = qasm.load("single_coin_toss.qasm")
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
