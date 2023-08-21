#!/bin/env python3
# A game of Rock Papper Scissors

import random

while(True):
     player_one = input("Please enter rock(r), paper(p), scissors(s): ")
     player_two = random.randint(1,3)


if player_two == 1:
     player_two == "r"
 elif player_two == 2:
     player_two == "p"
 elif player_two == 3:
     player_two == "s"


if (player_one == player_two):
     print("It's a tie!")

 elif player_one =="r":
     if player_two == "s":
         print("Player_one wins! Rock beats Scissors"
                 else:
                 print("Player_two wins!")


 elif player_one == "p":
     if player_two == "r":
         print("Player_two wins! Paper beats Rock!")
                 else:
                 print("Player_one wins!")

 elif player_one =="s":
     if player_two =="p":
         print)"Player_one wins! Scissors beats Paper!")
                 else:
                 print("Player_two wins!")


print("Youe choice: " + player_one "\nplayer_two's choice: " + player_two + "\nThank you fore playing!")
print("Do you want to play again?  (Y/N)")
ans = input()
# if user input n or N then conditions is True
if ans == 'n' or ans == 'N':
    break


