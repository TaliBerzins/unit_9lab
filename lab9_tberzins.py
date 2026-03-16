from player import Player
""" lab9.py
Tali Berzins
To run a game loop for rolling dice
03/14/2026
"""
def main():
  player1 = Player("Player 1") 
  player2 = Player("Player 2")
  print("Player 1 has " + str(player1.get_wallet()) + " coins.")
  print("Player 2 has " + str(player2.get_wallet()) + " coins.")
# Creating loop to run coin toss until player types n for no
  while(input("Do you want to toss the coins? (y/n)\n").upper() == "Y"):
    player1.toss_coin()
    player2.toss_coin()

    #Calling coin side method for each player
    print("Player 1 tossed " + player1.get_coin_side())
    print("Player 2 tossed " + player2.get_coin_side())

    #Determining who wins and adding coins based off of winner
    if(player1.get_coin_side() == player2.get_coin_side()):
      print("...It's a Match! Player 1 wins a coin.\n")
      player1.win_coin()
      player2.lose_coin()
      print("Player 1 has " + str(player1.get_wallet()) + " coins.")
      print("Player 2 has " + str(player2.get_wallet()) + " coins.\n")

    else:
      print("...No Match! Player 2 wins a coin.\n")
      player2.win_coin()
      player1.lose_coin()
      print("Player 1 has " + str(player1.get_wallet()) + " coins.")
      print("Player 2 has " + str(player2.get_wallet()) + " coins.\n")

#Printing final score and determining final winner once games is finished
  print("--- Final Score ---")
  print("Player 1: " + str(player1.get_wallet()) + " coins.")
  print("Player 2: " + str(player2.get_wallet()) + " coins.\n")
  if player1.get_wallet()>(player2.get_wallet()):
    print("Player 1 wins!")
  elif player1.get_wallet()<(player2.get_wallet()):
        print("Player 2 wins!")
  else:
     print("It's a draw!")






main()

