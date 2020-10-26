'''
Created by Vedant Christian
Created on 11 / 10 / 2019
'''

import math

userinput = int(input("Upto what number do you want the Pythagorean Triplets ?"))

def pythagorean_triplet(n):
  for b in range(n):
    for a in range(1, b):
        c = math.sqrt( a * a + b * b)
        if c % 1 == 0:
            print(a, b, int(c))
            
pythagorean_triplet(userinput)
