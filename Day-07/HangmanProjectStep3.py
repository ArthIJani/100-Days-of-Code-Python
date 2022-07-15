#Step3
import random
word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
print("Chosen_Word ",chosen_word)

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
    #print(f"Current position: {position}\nCurrent letter: {letter}\nGuessed letter: {guess}")
    if letter == guess:
      display[position] = letter

  print(display)

  if "_" not in display:
    end_of_game = True
    print("You Win")