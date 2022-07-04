import random

#Step 1 
word_list = ["the","of","and","a","to","in","is","you","that","it","he","was","for","on","are","as","with","his","they","I","at","be","this","have","from","or","one","had","by","word","but","not","what","all","were","we","when","your","can","said","there","use","an","each","which","she","do","how","their","if","will","up","other","about","out","many","then","them","these","so","some","her","would","make","like","him","into","time","has","look","two","more","write","go","see","number","no","way","could","people","my","than","first","water","been","call","who","oil","its","now","find","long","down","day","did","get","come","made","may","part"]

stages = ['''
  *---*
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  *---*
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  *---*
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  *---*
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  *---*
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  *---*
  |   |
  O   |
      |
      |
      |
=========
''', '''
  *---*
  |   |
      |
      |
      |
      |
=========
''']

random_word = random.choice(word_list)
display_count = []
used_letters = []
lives = 6

for letter in random_word:
    display_count.append('_')

display_count_ui = " ".join(display_count) 


while '_' in display_count and lives > 0:
    print("________________________\n________________________")
    print(stages[lives])
    print(f"{display_count_ui}\n")
    guess = input("Guess a letter: ").lower()
    if guess in used_letters:
        print("\n\nThis letter was already guessed")
    else:
        i = 0
        for letter in random_word:
            if guess == letter:
                display_count[i] = guess
                used_letters.append(guess)
            i += 1     
        if guess not in random_word:
            lives -= 1
    display_count_ui = " ".join(display_count) 

if lives > 0:
    print('You win!')
else:
    print('Game Over')
    

