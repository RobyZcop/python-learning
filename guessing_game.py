
import random
logo = """
   ___                         _                   ___                           
  / _ \ _   _   ___  ___  ___ (_) _ __    __ _    / _ \  __ _  _ __ ___    ___   
 / /_\/| | | | / _ \/ __|/ __|| || '_ \  / _` |  / /_\/ / _` || '_ ` _ \  / _ \  
/ /_\\ | |_| ||  __/\__ \\__ \| || | | || (_| | / /_\\ | (_| || | | | | ||  __/  
\____/  \__,_| \___||___/|___/|_||_| |_| \__, | \____/  \__,_||_| |_| |_| \___|  
                                         |___/                                   
"""

def play_game(attempts):
  
  final_number = random.randint(1,100)
  print(f"  Psst, the solution is {final_number} ")
  while attempts != 0:
      print(f"You have {attempts} attempts remaining to guess the number")
      guess = int(input("Make a guess: "))

      if guess != final_number:
          attempts -= 1

      if guess < final_number:
          print("Too low.")
          print("Guess again.")
      elif guess > final_number:
          print("Too high.")
          print("Guess again.")
      elif guess == final_number:
          print(f"You got it! The answer was {final_number}")

  if attempts == 0:
      print("You've run out of guesses, you lose.")
        
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if game_level == "easy":
    play_game(10)
else:
    play_game(5)
