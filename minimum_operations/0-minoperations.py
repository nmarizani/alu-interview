#!/usr/bin/python3

""" Module for 0-minoperations"""

def minOperations(n):
   
#All outputs be at least 2 char: (min, Copy All => Paste)
    if (n < 2):

        return 0

    ops, root = 0, 2
    while root <= n: 

#If n evenly divides by root

        if n % root == 0:

#Total even-divs by root = total ops

            ops += root

#Set n to the remainder

            n = n / root

#Reduce root to find remaining smaller vals that evenly-divide n

            root -= 1

#Increment root until it evenly-divides n

        root += 1
    return ops

