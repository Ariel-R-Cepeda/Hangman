import random

class Hangman:

  def __init__(self):
    
    #accessing the file of words and choosing the secret word
    with open('words.csv') as f:
      words = list(f)
    words_list = [word[:-1]] for word in words if word == word.lower() and len(word)>4 and '-' and "'" not in word
    self.secret = random.choice(words_list)

    #setup
    self.mistakes = 0
    self.structure = ["  |--------|","  |        ","  |       ","  |        ","  |          ","  |      ","  |","-----"]
    self.pieces = ["O","/","|","\ ","^","/ ","\ ","°   ","°"]
    self.sequence = [1,3,1,2,2]
    self.wrong_letters = None
    self.game_over = False
    self.current_state = draw()

  #really doesn't matter
  def __repr__(self):
    return "It's hangman lmao"
  
  #makes and adds to the gallows
  def draw(self):
    for i,v in enumerate(self.sequence, start=1):
      for k in range(v):
        self.structure[i] += next(self.pieces)
        yield '\n'.join(self.structure)

  #Guessing a letter
  def guess(self):
    progress = ['_' for letter in secret]
    guess = input("Guess a letter:")
    if guess in self.secret:
      for idx,letter in enumerate(self.secret):
        if letter == guess:
         progress[idx] = guess
    else:
      self.mistakes += 1
      self.wrong_letters += guess + ' '
      if self.mistakes == 9:
        self.game_over = True
      
  
  def play(self)
    
    #ascii title screen
    print("  o         o")
    print(" <|>       <|>")
    print(" < >       < >")
    print("  |         |      o__ __o/  \o__ __o     o__ __o/  \o__ __o__ __o      o__ __o/  \o__ __o  ")
    print("  o__/_ _\__o     /v     |    |     |>   /v     |    |     |     |>    /v     |    |     |> ")
    print("  |         |    />     / \  / \   / \  />     / \  / \   / \   / \   />     / \  / \   / \ ")
    print(" <o>       <o>   \      \o/  \o/   \o/  \      \o/  \o/   \o/   \o/   \      \o/  \o/   \o/ ")
    print("  |         |     o      |    |     |    o      |    |     |     |     o      |    |     |  ")
    print(" / \       / \    <\__  / \  / \   / \   <\__  < >  / \   / \   / \    <\__  / \  / \   / \ ")
    print("                                                |")
    print("                                        o__     o")
    print("                                        <\__ __/>")

    #actual game
    while not self.game_over:
      print(f'{9 - self.mistakes} tries left)
      print(self.current_state)
      print(self.wrong_letters)
      guess()
    if '_' not in progress:
      return('Congrats you won.')
    if self.game_over:
      return(f'You lost! The word was {self.secret}')
