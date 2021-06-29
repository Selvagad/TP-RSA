#!/usr/bin/env python
# -*- coding: utf-8 -*-

import primesieve
import random


def generatePrimeNumber():
    return primesieve.n_primes(1, random.randint(1000000000, 10000000000-1))[0]

# Take a number and make a decomposition with only prime numbers
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Multiply the first prime numbers to get a product of the last by all the other ones
def get2PrimeFactors(n):
    a = 1
    res = []
    facteurs = prime_factors(n)
    if (len(facteurs) > 2):
        for i in range(len(facteurs)):
            if i != len(facteurs)-1:
                a = a * facteurs[i]
        res.append(a)
        res.append(facteurs[-1])
        return res
    else:
        return facteurs


def findFirstED(n_prime):
    i = 0
    in_progress = True
    while in_progress:
        i += 1
        temp = 1 + (i * n_prime)
        try:
            e, d = get2PrimeFactors(temp)
        except:
            pass
        if e == d:
            pass
        else:
            in_progress = False
            return e,d


p = primesieve.n_primes(1, random.randint(1000000000, 10000000000-1))[0]
q = primesieve.n_primes(1, random.randint(1000000000, 10000000000-1))[0]
n = p*q
n_prim = (p-1)*(q-1)
e, d = findFirstED(n_prim)
print("p=", p)
print("q=", q)
print("n=", n)
print("n\'=", n_prim)
print("e=", e)
print("d=", d)