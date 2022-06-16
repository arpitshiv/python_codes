from random import *
list_of_word=('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#HANGMANPICS=HANGMANPICS.reverse()
print('''_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/       ''')

choosen_word=choice(list_of_word)
display=[]
word_len=len(choosen_word)
lives=5
for letter in range(word_len):
    display+="_"
print(display)
end_game=False
while not end_game:
    guess=input("guess a letter ").lower()
    for position in range(word_len):
       letter=choosen_word[position]
       if guess==choosen_word[position]:
           display[position]=letter
    print(display)
    if guess not in choosen_word:
            lives-=1
            if lives==0:
                end_game=True
                print("you lose")
    if "_" not in display:
        end_game=True
        print("you won")
    
    print(HANGMANPICS[-lives])
