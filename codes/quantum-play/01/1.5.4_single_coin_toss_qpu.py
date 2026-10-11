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
from os import getenv

load_dotenv()

q = QuantumRegister(1)
c = ClassicalRegister(1)

qc = QuantumCircuit(q, c)
qc.h(q[0])
qc.measure(q, c)

qc.draw("mpl")
plt.show()

service = QiskitRuntimeService(
    channel="ibm_quantum_platform", instance=getenv("CRN"), token=getenv("API_KEY")
)

backend = service.least_busy(operational=True, simulator=False)

# Transpile the circuit for the target backend's basis gates and coupling map.
qc = transpile(qc, backend)
qc.draw("mpl")
plt.show()

sampler = Sampler(backend)

job = sampler.run([qc], shots=1024)
print(job.job_id())
