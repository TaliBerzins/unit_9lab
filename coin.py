import random
""" Coin.py
Tali Berzins
To represent a single tossable coin
03/14/2026
"""
class Coin:

    def __init__(self):
     if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
     else:
            self.__sideup = 'Tails' 

    def toss():
     num = random.randint(0,1)
     if(num == 0):
     sideup == "Heads"
       

