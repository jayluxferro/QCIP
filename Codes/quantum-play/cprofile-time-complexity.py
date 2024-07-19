#!/usr/bin/env python3


import cProfile

def test_function(n):
    return [i ** 2 for i in range(n)]

cProfile.run('test_function(5000)')
