import random
""" Coin.py
Tali Berzins
To represent a single tossable coin
03/14/2026
"""
class Coin:
    """Handles defining the side of the coin for each toss and returning that value
    
    Attributes:
      __sideup : private string value
   """
 #Initializer method
    def __init__(self):
       """Sets up the starting side randomly"""
       if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
       else:
            self.__sideup = 'Tails'
            

  #Coin toss method 
    def toss(self):
     """For each coin toss side is defined to either heads or tails"""
     if(random.randint(0,1)) == 0:
       self.__sideup = 'Heads'
     else:
       self.__sideup = 'Tails'

    
    def get_sideup(self):
       """Returns the sideup variable"""
       return self.__sideup
       

