"""
Running multiple QCs
"""

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator


# Single coin toss
q1 = QuantumRegister(1)
c1 = ClassicalRegister(1)

qc1 = QuantumCircuit(q1, c1)
qc1.h(q1[0])
qc1.measure(q1, c1)
qc1.draw("mpl")
plt.show()

# Double coin toss
q2 = QuantumRegister(2)
c2 = ClassicalRegister(2)

qc2 = QuantumCircuit(q2, c2)
qc2.h(q2[0])
qc2.h(q2[1])
qc2.measure(q2, c2)
qc2.draw("mpl")
plt.show()

# initialize our simulator / backend
simulator = AerSimulator()

# run the circuit on the simulator
job = simulator.run([qc1, qc2], shots=2000)

# get the results
job_result = job.result()

# Extra info
print("Backend name: ", job_result.backend_name)  # backend name
print("Backend version: ", job_result.backend_version)  # backend version
print("Job Id: ", job_result.job_id)  # job id
print("Job status: ", job_result.success)  # whether the job was successful

# results
actual_results = job_result.results

# single coin toss
# print(actual_results[0])
qc1_data = actual_results[0].data
counts = qc1_data.counts
print(counts)
plot_histogram(counts)
plt.show()

# double coin toss
# print(actual_results[1])
qc2_data = actual_results[1].data
counts = qc2_data.counts
print(counts)
plot_histogram(counts)
plt.show()

# Extra info
print("Date: ", job_result.date)  # date
print("Execution status: ", job_result.status)  # completed ,etc
print("Metadata: ", job_result.metadata)
print("Memory (mb): ", job_result.metadata["max_memory_mb"])
print("Execution time: ", job_result.metadata["time_taken_execute"])
