print("            WELCOME TO THE GAME")
print("          Rock-Paper-Scissors Game")
print("*********************************************")
print("Select any one of the following options:\n")
print("Rock\nPaper\nScissors\n")
print("NOTE: ENTER YOUR CHOICE AS SAME AS THE GIVEN OPTIONS")
print("*********************************************")

import random

i =0
j =0
while True:
    user_choice = input("Enter your choice: ")
    if (user_choice == "Rock" or user_choice == "Paper" or user_choice 
     == "Scissors"):
       computer_choice = random.choice(["Rock", "Paper", "Scissors"])
       print("Computer's choice:", computer_choice)
       if user_choice == computer_choice:
          print("It's a tie!")
       elif user_choice == "Rock" and computer_choice == "Scissors":
          print("You win!")
          print("your score is", i+1)
          i = i+1
       elif user_choice == "Paper" and computer_choice == "Rock":
          print("you win!")
          print("your score is", i+1)
          i = i+1
       elif user_choice == "Scissors" and computer_choice == "Paper":
          print("You win!")   
          print("your score is", i+1)
          i = i+1
       else:
          print("Computer wins!")
          print("Computer score is", j+1)
          j = j+1

       
       print("-----------------------------------------------------")
       play_again = input("Do you want to play again? (yes/no): ")
       print("-----------------------------------------------------")
       if play_again.lower() != "yes":
         break

    else:
      print("Invalid choice. Please enter Rock, Paper, or Scissors.")
      print("-----------------------------------------------------")

print("Thank you for playing!")
    