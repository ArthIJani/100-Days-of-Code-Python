
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

word_list = [
'abruptly','absurd','abyss','affix','askew','avenue','awkward','axiom','azure','bagpipes','bandwagon','banjo','bayou','beekeeper','bikini','blitz','blizzard','boggle',
  'bookworm','boxcar','boxful','buckaroo','buffalo','buffoon','buxom','buzzard','buzzing','buzzwords','caliph','cobweb','cockiness','croquet','crypt','curacao','cycle',
  'daiquiri','dirndl','disavow','dizzying','duplex','dwarves','embezzle','equip','espionage','euouae','exodus','faking','fishhook','fixable','fjord','flapjack','flopping',
  'fluffiness','flyby','foxglove','frazzled','frizzled','fuchsia','funny','gabby','galaxy','galvanize','gazebo','giaour','gizmo','glowworm','glyph','gnarly','gnostic',
  'gossip','grogginess','haiku','haphazard','hyphen','iatrogenic','icebox','injury','ivory','ivy','jackpot','jaundice','jawbreaker','jaywalk','jazziest','jazzy','jelly',
  'jigsaw','jinx','jiujitsu','jockey','jogging','joking','jovial','joyful','juicy','jukebox','jumbo','kayak','kazoo','keyhole','khaki','kilobyte','kiosk','kitsch',
  'kiwifruit','klutz','knapsack','larynx','lengths','lucky','luxury','lymph','marquis','matrix','megahertz','microwave','mnemonic','mystify','naphtha','nightclub','nowadays',
  'numbskull','nymph','onyx','ovary','oxidize','oxygen','pajama','peekaboo','phlegm','pixel','pizazz','pneumonia','polka','pshaw','psyche','puppy','puzzling','quartz','queue',
  'quips','quixotic','quiz','quizzes','quorum','razzmatazz','rhubarb','rhythm','rickshaw','schnapps','scratch','shiv','snazzy','sphinx','spritz','squawk','staff','strength',
  'strengths','stretch','stronghold','stymied','subway','swivel','syndrome','thriftless','thumbscrew','topaz','transcript','transgress','transplant','triphthong',
  'twelfth','twelfths','unknown','unworthy','unzip','uptown','vaporize','vixen','vodka','voodoo','vortex','voyeurism','walkway','waltz','wave','wavy','waxy','wellspring',
  'wheezy','whiskey','whizzing','whomever','wimpy','witchcraft','wizard','woozy','wristwatch','wyvern','xylophone','yachtsman','yippee','yoked','youthful','yummy',
  'zephyr','zigzag','zigzagging','zilch','zipper','zodiac','zombie',
]


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
