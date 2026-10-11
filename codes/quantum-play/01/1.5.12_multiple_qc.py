"""
Run multiple quantum circuits in a single simulator job.

Builds single and double coin-toss circuits, runs them together on the
AerSimulator, and reports counts plus job metadata (backend, time,
memory).

@author: Jay (@jayluxferro)
"""

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


def hex_to_bin_results_convert(results: dict, padding: int = 1) -> dict:
    """Convert hex-encoded result keys to zero-padded binary keys."""
    return {
        bin(int(key, 16))[2:].zfill(padding): value for key, value in results.items()
    }


def generate_coin_toss_circuit(coins: int) -> QuantumCircuit:
    q = QuantumRegister(coins)
    c = ClassicalRegister(coins)
    qc = QuantumCircuit(q, c)
    for coin in range(coins):
        qc.h(q[coin])  # 50-50 chance of occurrence
    qc.measure(q, c)
    return qc


qc_single = generate_coin_toss_circuit(1)
qc_double = generate_coin_toss_circuit(2)

qc_single.draw("mpl")
plt.show()
qc_double.draw("mpl")
plt.show()

simulator = AerSimulator()
job = simulator.run([qc_single, qc_double], shots=15000)
job_result = job.result()

print("Backend name: ", job_result.backend_name)
print("Backend version: ", job_result.backend_version)
print("Job Id: ", job_result.job_id)
print("Job successful: ", job_result.success)

# Single coin toss
single_counts = job_result.results[0].data.counts
print(single_counts)
plot_histogram(hex_to_bin_results_convert(single_counts), title="Single Coin Toss")
plt.show()

# Double coin toss
double_counts = job_result.results[1].data.counts
print(double_counts)
plot_histogram(hex_to_bin_results_convert(double_counts, padding=2), title="Double Coin Toss")
plt.show()

print("Date: ", job_result.date)
print("Execution status: ", job_result.status)
print("Memory (mb): ", job_result.metadata["max_memory_mb"])
print("Execution time: ", job_result.metadata["time_taken_execute"])
