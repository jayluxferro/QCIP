"""
Find all factors of a given number (classical).

@author: Jay (@jayluxferro)
"""


def factors_of_number(n: int) -> list:
    """Return the factors of a given number."""
    if n < 1:
        return []

    factors = []
    for i in range(1, n + 1):
        print(f"Checking if {i} is a factor of {n}...")
        if n % i == 0:
            print(f"{i} is a factor of {n}.")
            factors.append(i)
            print(", ".join(str(x) for x in factors))
            print()

    return factors


input_number = int(input("Enter a number to find its factors: "))

factors = factors_of_number(input_number)
print(f"The factors of {input_number} are: {factors}")
