"""
Single coin toss on a real IBM Quantum backend.

Submits a single-qubit Hadamard circuit to the least-busy operational
QPU via the Qiskit Runtime SamplerV2. Credentials are read from .env.

@author: Jay (@jayluxferro)
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
import matplotlib.pyplot as plt
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from dotenv import load_dotenv
from os import getenv, makedirs

load_dotenv()

q = QuantumRegister(1)
c = ClassicalRegister(1)

qc = QuantumCircuit(q, c)
qc.h(q[0])
qc.measure(q, c)

qc.draw("mpl")
plt.show()

service = QiskitRuntimeService(
    channel=getenv("IBM_CHANNEL"), instance=getenv("IBM_INSTANCE"), token=getenv("IBM_QUANTUM_API_KEY")
)

backend = service.least_busy(operational=True, simulator=False)

# Transpile the circuit for the target backend's basis gates and coupling map.
qc = transpile(qc, backend)
qc.draw("mpl")
plt.show()

sampler = Sampler(backend)

job = sampler.run([qc], shots=1024)
job_id = job.job_id()
print(job_id)

# Store the job ID so the *_results.py script can retrieve it later.
makedirs("out", exist_ok=True)
with open("out/single_coin_toss_job_id.txt", "w") as f:
    f.write(job_id)
