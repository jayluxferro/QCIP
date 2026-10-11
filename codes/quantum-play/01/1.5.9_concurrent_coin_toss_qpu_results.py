"""
Retrieve and analyze a concurrent single + double coin-toss QPU job.

@author: Jay (@jayluxferro)
"""

import matplotlib.pyplot as plt
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit.visualization import plot_histogram
from dotenv import load_dotenv
from os import getenv, path

load_dotenv()

service = QiskitRuntimeService(
    channel=getenv("IBM_CHANNEL"), instance=getenv("IBM_INSTANCE"), token=getenv("IBM_QUANTUM_API_KEY")
)

job_id_file = "out/concurrent_coin_toss_job_id.txt"
if path.exists(job_id_file):
    with open(job_id_file) as f:
        job_id = f.read().strip()
    print(f"Using stored job ID: {job_id}")
else:
    job_id = input("Enter your job ID: ").strip().rstrip()
job = service.job(job_id)
job_result = job.result()

# Single coin toss
single = job_result[0].data.c0.get_counts()
print(single)

# Double coin toss
double = job_result[1].data.c1.get_counts()
print(double)

plot_histogram(single, title="Single Coin Toss")
plt.show()

plot_histogram(double, title="Double Coin Toss")
plt.show()
