from time import time


word_size = int(input("Enter word size in bits (e.g., 8, 16, 32, 64): "))

start_time = time()
for i in range(2**word_size):
    print(bin(i)[2:].zfill(word_size))

end_time = time()

print("Time taken to compute 2^%d: %.6f seconds\n" % (word_size, end_time - start_time))
