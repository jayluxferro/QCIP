# Set versions variable to the current Qiskit versions
"""
@author: Jay (@jayluxferro)
"""

import qiskit
import qiskit_ibm_runtime

print(f'[+] Qiskit version: {qiskit.__version__}')
print(f'[+] Qiskit IBM runtime version: {qiskit_ibm_runtime.version.__version__}')