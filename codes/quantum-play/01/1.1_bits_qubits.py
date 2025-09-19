from math import sqrt, pow
import numpy as np


def test_for_normalization(a, b):
    assert round(pow(a, 2) + pow(b, 2), 1) == 1.0


alpha = sqrt(1 / 2)
beta = sqrt(1 / 2)

# test for normalization
test_for_normalization(alpha, beta)

# setup bits and qubits
bits = {
    "0": np.array([1, 0]),
    "1": np.array([0, 1]),
    "|0>": np.array([1, 0]),
    "|1>": np.array([0, 1]),
    "a|0> + b|1>": np.array([alpha, beta]),
}

# print the vectors
for b in bits:
    print(b, ": ", bits[b])  # prints the key : value of the key

# measurement of bits and qubits
for b in bits:
    key = b
    value = bits[b]
    print(key, ": ", value)  # prints the key : value of the key
    zero_measurement_value = value[0]
    one_measurement_value = value[1]
    prob_zero_measurement = pow(zero_measurement_value, 2)
    prob_one_measurement = pow(one_measurement_value, 2)
    print("zero measurement: ", prob_zero_measurement)
    print("one measurement: ", prob_one_measurement)
    print("------------")
