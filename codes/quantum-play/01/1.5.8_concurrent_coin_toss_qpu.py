"""
Run single and double coin toss concurrently on an IBM Quantum backend.

Builds both circuits with a generator, transpiles them for the selected
backend, and submits them in one job (Assignment II).

@author: Jay (@jayluxferro)
"""

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from dotenv import load_dotenv
from os import getenv

load_dotenv()


def generate_coin_toss_circuit(coins: int) -> QuantumCircuit:
    q = QuantumRegister(coins)
    c = ClassicalRegister(coins)

    qc = QuantumCircuit(q, c)
    for coin in range(coins):
        qc.h(q[coin])  # 50-50 chance of occurrence
    qc.measure(q, c)
    return qc


service = QiskitRuntimeService(
    channel="ibm_quantum_platform", instance=getenv("CRN"), token=getenv("API_KEY")
)

backend = service.least_busy(operational=True, simulator=False)
sampler = Sampler(backend)

circuits = transpile(
    [generate_coin_toss_circuit(1), generate_coin_toss_circuit(2)], backend
)
for circuit in circuits:
    circuit.draw(output="mpl")
    plt.show()

job = sampler.run(circuits, shots=15000)
print(job.job_id())
