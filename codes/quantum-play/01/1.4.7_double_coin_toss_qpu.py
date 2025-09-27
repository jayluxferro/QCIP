"""
Double coin toss QPU
"""

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import matplotlib.pyplot as plt
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from dotenv import load_dotenv
from os import getenv

load_dotenv()

q = QuantumRegister(2)
c = ClassicalRegister(2)

qc = QuantumCircuit(q, c)

# Measurement
qc.measure(q, c)

qc.draw("mpl", filename="double_coin_toss_circuit.jpg")
plt.show()

# Run on QPU
service = QiskitRuntimeService(
    channel="ibm_quantum_platform", instance=getenv("CRN"), token=getenv("API_KEY")
)

backend = service.least_busy(operational=True, simulator=False)
simulator = Sampler(backend)

job = simulator.run([qc], shots=2000)
print(job.job_id())
