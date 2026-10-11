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
from os import getenv, makedirs

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
    channel=getenv("IBM_CHANNEL"), instance=getenv("IBM_INSTANCE"), token=getenv("IBM_QUANTUM_API_KEY")
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
job_id = job.job_id()
print(job_id)

# Store the job ID so the *_results.py script can retrieve it later.
makedirs("out", exist_ok=True)
with open("out/concurrent_coin_toss_job_id.txt", "w") as f:
    f.write(job_id)
