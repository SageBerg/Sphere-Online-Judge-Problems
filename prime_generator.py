from time import time
from math import sqrt

def sieve_of_eratosthenes(n):
    primes = [True] * n
    for i in range(2, int(sqrt(n))):
        if primes[i]:
            j = i**2
            while j < n:
                primes[j] = False
                j += i

def print_primes(start, end):
    begin = time() 
    for i in range(start, end + 1):
        pass
    print "\ntime taken: " + str(time() - begin)

cases = int(raw_input())

for i in range(cases):
    case = raw_input().split()
    start = int(case[0])
    end   = int(case[1])
    print_primes(start, end)
    if i != cases -1:
        print
