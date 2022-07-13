
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


logo = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       """




#Step5
import random

#If words are stored in different File
  #import hangman_words
  #chosen_word = random.choice(hangman_words.word_list)
chosen_word = random.choice(word_list)

#Logo
#If Logo is stored in different file
#from hangman_art import logo
print(logo)

#TestingCode
#print("Chosen_Word ",chosen_word)

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

  if guess in display:
    print(f"You've  already guessed {guess}")

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  #If guess is not a letter in chosen _word
  #Reduce Lives by 1
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life")
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

  #For stages stored in different file 
  #from hangman_art import stages
  print(stages[lives])
