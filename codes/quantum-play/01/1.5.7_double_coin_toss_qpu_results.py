"""
Retrieve and analyze a double-coin-toss QPU job.

@author: Jay (@jayluxferro)
"""

import matplotlib.pyplot as plt
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit.visualization import plot_histogram
from dotenv import load_dotenv
from os import getenv

load_dotenv()

service = QiskitRuntimeService(
    channel="ibm_quantum_platform", instance=getenv("CRN"), token=getenv("API_KEY")
)

job_id = input("Enter your job ID: ").strip().rstrip()
job = service.job(job_id)
result = job.result()[0].data.c0

iterations = result.num_shots
print(iterations)

counts = result.get_counts()
print(counts)

plot_histogram(counts)
plt.show()
