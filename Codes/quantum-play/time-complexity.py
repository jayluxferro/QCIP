#!/usr/bin/env python3

import matplotlib.pyplot as plt
import time

def test_function(n):
    return [i * 2 for i in range(n)]


input_sizes = [1000, 2000, 4000, 8000, 16000]
execution_time = []

for size in input_sizes:
    start_time = time.time()
    test_function(size)
    end_time = time.time()
    time_diff = end_time - start_time
    execution_time.append(time_diff)
    print(f"Size: {size}, Time: {time_diff} seconds")

plt.plot(input_sizes, execution_time)
plt.show()

