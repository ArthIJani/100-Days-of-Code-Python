#Step4
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']

word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
#TestingCode
print("Chosen_Word ",chosen_word)

#No. of Lives
lives = 6

display = []
word_length = len(chosen_word)
for _ in range(word_length):
  display += "_"
print(display)

end_of_game = False
while not end_of_game:
  guess = input("Guess a Letter ").lower()

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  #If guess is not a letter in chosen _word
  #Reduce Lives by 1
  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You Lose")
  
  #Join all the elements in the list and turn it into a string.
  print(f"{' '.join(display)}")

  #Check if user has got all letters.
  if "_" not in display:
    end_of_game = True
    print("You Win")

  #Print the ASCII art from stages that corresponds to the current number of 'lives' the user has remaining
  print(stages[lives])