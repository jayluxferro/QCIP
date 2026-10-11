"""
Import a quantum circuit from an OpenQASM file.

@author: Jay (@jayluxferro)
"""

from qiskit import qasm2 as qasm
import matplotlib.pyplot as plt

qc = qasm.load("out/single_coin_toss.qasm")

qc.draw("mpl")
plt.show()
