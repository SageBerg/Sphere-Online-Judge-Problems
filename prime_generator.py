import time
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n))):
        if float(n)/i == n/i:
            return False
    return True

def sieve_of_eratosthenes(n):
    primes = [True] * n
    for i in range(2, int(math.sqrt(n))):
        if primes[i]:
            j = i**2
            while j < n:
                primes[j] = False
                j += i

def print_primes(start, end):
    begin = time.time() 
    for i in range(start, end):
        is_prime(i)
    print "time taken: " + str(time.time() - begin)

cases = int(raw_input())

for _ in range(cases):
    case = raw_input().split()
    start = int(case[0])
    end   = int(case[1])
    print_primes(start, end)
