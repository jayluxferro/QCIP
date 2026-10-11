"""
Visualize classical bits and qubit superpositions on the Bloch sphere.

@author: Jay (@jayluxferro)
"""

import numpy as np
from cmath import exp
from math import pi, sin, cos
from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt

np.set_printoptions(precision=3)

# Superposition with zero phase.
angles = {"theta": pi / 2, "phi": 0}

# (Optional) self-defined qubit angles.
# angles["theta"] = float(input("Theta:\n"))
# angles["phi"] = float(input("Phi:\n"))

# Bit and qubit states as Bloch-sphere angles.
bits = {
    "bit = 0": {"theta": 0, "phi": 0},
    "bit = 1": {"theta": pi, "phi": 0},
    "|0>": {"theta": 0, "phi": 0},
    "|1>": {"theta": pi, "phi": 0},
    "a|0> + b|1>": angles,
}

for bit in bits:
    bloch = [
        cos(bits[bit]["phi"]) * sin(bits[bit]["theta"]),
        sin(bits[bit]["phi"]) * sin(bits[bit]["theta"]),
        cos(bits[bit]["theta"]),
    ]

    plot_bloch_vector(bloch, title=bit)
    plt.show()

    # Build the corresponding state vector.
    a = cos(bits[bit]["theta"] / 2)
    b = exp(bits[bit]["phi"] * 1j) * sin(bits[bit]["theta"] / 2)
    state_vector = [a, b]
    print("State vector:", np.around(state_vector, decimals=3))
