# Incorporate the random library
import random

keep_playing = "Y"
while keep_playing == "Y" or keep_playing == "y":

  # Print Title
  print("Let's Play Rock Paper Scissors!")

  # Specify the three options
  options = ["r", "p", "s"]

  # Computer Selection
  computer_choice = random.choice(options)

  # User Selection
  user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")
  print(f"Computer chose {computer_choice}")
  
  # Run Conditionals
  if user_choice == 'r':
    if computer_choice == 'p':
      print('Computer Wins!')
    elif computer_choice == 's':
      print('You win!!')
    else:
      print("It's a draw")
  elif user_choice == 'p':
    if computer_choice == 's':
      print('Computer Wins!')
    elif computer_choice == 'r':
      print('You win!!')
    else:
      print("It's a draw")
  elif user_choice == 's':
    if computer_choice == 'r':
      print('Computer Wins!')
    elif computer_choice == 'p':
      print('You win!!')
    else:
      print("It's a draw")
  else: 
    print("Invalid choice")
  
  keep_playing = input("Do you wish to keep playing (Y/N)?")