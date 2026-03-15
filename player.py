from coin import Coin
""" player.py
Tali Berzins
To define the player class of the coin tossing game
03/14/2026
"""

class Player:

    def __init__(self, name):
        """Initalizes players name, wallet, and coin instance"""
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()
    
    def toss_coin(self):
        """Calls instance to toss coin"""
        self.__coin.toss()

    def get_coin_side(self):
        """Calls coin class and instance to return the side of the coin"""
        return self.__coin.get_sideup()
    
    def win_coin(self):
        """Adds one to wallet if they win"""
        self.__wallet+=1
    
    def lose_coin(self):
        """Subtracts one from wallet if they win"""
        self.__wallet-=1
    
    def get_wallet(self):
        """Returns the wallets value"""
        return self.__wallet
    
    def get_name(self):
        """Returns the name of the instance"""
        return self.__name

