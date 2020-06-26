import words
def game(word):
    shape = 5
    guessed_letter = []
    word_completion = ("-")*len(word)
    terminate = True
    print("lets play hangman game")
    print(words.hangman(shape))
    print("\n")
    #print(word)
    print(word_completion)
    while shape > 0 and terminate != False:
        
        guess = raw_input("Please enter a your guess: ").upper()
        #print(guess)
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letter:
                print("the letter is already guessed")
            
            elif guess in word:
                print("Gooooog JOB, ",guess," is in the word ")
                guessed_letter.append(guess)
                w_c = list(word_completion)

                result = [i for i,x in enumerate(word) if x == guess]
                for index in result:
                    w_c[index] = guess
                    word_completion = "".join(w_c)
                print(word_completion)
                if word_completion == word:
                    print("YOU WIN !!!!!",guess)
                    terminate = False
                    break

            else :
                print("wrong guess")
                shape -= 1
                print(words.hangman(shape))
                print(word_completion)
            

        elif len(guess) > 1 and guess.isalpha():
            if len(word) == len(guess):
                if guess == word:
                    print("YOU WIN !!!!!",guess)
                    terminate = False
                    break
                else:
                    shape -= 1
                    print(words.hangman(shape))
                    print(word_completion)
            else:
                    shape -= 1
                    print(words.hangman(shape))
                    print(word_completion)
                    

        else:
            print("Not valid Data.")
            print(words.hangman(shape))
            print("\n")
