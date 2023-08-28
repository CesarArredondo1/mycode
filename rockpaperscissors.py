import random

while True:
     player_one = input("Please enter rock(r), paper(p),scisssors(s): ")
     computer = random.choice(['r', 'p', 's'])
     break
if (player_one == computer):
     print("It's a tie!")
elif player_one == "r" :
     if computer == "s":
         print("Player_one wins! Rock beats Scissors")
     else:
         print("Computer wins!")
elif player_one == "p":
     if computer == "r":
         print("Computer wins! Paper beats Rock!")
     else:
         print("Player_one wins!")
elif player_one =="s":
     if computer =="p":
         print("Player_one wins! Scissors beats Paper!")
     else:
         print("Computer wins!")
print("Your choice: " + player_one + "\n computer's choice: " + computer + "\nThank you for playing!")
print("Do you want to play again? (Y/N)")
ans = input()
if ans == 'n' or ans == 'N':
    exit
