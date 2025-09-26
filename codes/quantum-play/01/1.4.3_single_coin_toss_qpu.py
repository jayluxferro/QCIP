from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import matplotlib.pyplot as plt
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from dotenv import load_dotenv
from os import getenv

# Load environment variables from the .env file
load_dotenv()

q = QuantumRegister(1)
c = ClassicalRegister(1)


qc = QuantumCircuit(q, c)
# qc.h(q[0])

# measurement
qc.measure(q, c)

qc.draw("mpl", filename="single_coin_toss.jpg")  # text, latex, latex_source, and mpl
plt.show()

# Run on QPU
service = QiskitRuntimeService(
    channel="ibm_quantum_platform", instance=getenv("CRN"), token=getenv("API_KEY")
)

backend = service.least_busy(operational=True, simulator=False)
simulator = Sampler(backend)

job = simulator.run([qc], shots=1024)
print(job.job_id())
