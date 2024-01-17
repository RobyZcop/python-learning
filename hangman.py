# From this small project I learn the while loop logic and how to use it. It is important if we set a var = False that in the loop change otherwise the while loop will be infinite.
# Then I learned about modules

import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#Create list to keep track of guessed letters
user_guessed = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    
    if guess in display:
      print(f"You have already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    #Check if user is wrong.
    if guess not in chosen_word:
       
        print(f"You guessed {guess}, that's not in the word. You lose a life. ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])
