"""
Double coin toss on a real IBM Quantum backend.

@author: Jay (@jayluxferro)
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
import matplotlib.pyplot as plt
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from dotenv import load_dotenv
from os import getenv, makedirs

load_dotenv()

q = QuantumRegister(2)
c = ClassicalRegister(2)

qc = QuantumCircuit(q, c)
qc.h(q[0])
qc.h(q[1])
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

job = sampler.run([qc], shots=2000)
job_id = job.job_id()
print(job_id)

# Store the job ID so the *_results.py script can retrieve it later.
makedirs("out", exist_ok=True)
with open("out/double_coin_toss_job_id.txt", "w") as f:
    f.write(job_id)
