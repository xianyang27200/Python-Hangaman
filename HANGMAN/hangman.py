import random
from Play import game
from DB import list_words 
def gamedoc():
    '''
    
     we are guessing the word. The user needs to guess letters,
Give the user no more than 6 attempts for guessing wrong letter. 
    '''
print(gamedoc.__doc__)

def get_word():
    choosen = str(random.choice(list_words))
    choice = choosen[3:-3]
    return choice.upper()

def main():
    word = get_word()
    game(word)
    
    if raw_input("PLAY AGAIN (Y/N): ").upper() == 'Y':
        word = get_word()
        game(word)
if __name__ == "__main__":
          main()




        