#import the python functions we'll need for the code

from random import *
import sys

#some variables, so we can keep score of the games played, and they are updated each round

player_score = 0
computer_score = 0

#actual game starts here, with a while loop to let us continually play the game until we decide otherwise

def start():
    print("Let's play Hangman")
    while game():
        pass
    scores()

#game rules are decided here, as welll to setup for the word and keeping track of tries and incorrect answers

def game():
    dictionary = ['gnu','linux','ubuntu']
    word = choice(dictionary)
    word_length = len(word)
    clue = word_length*['_']
    tries = 6
    letters_tried = ''

    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score

    #human input for the game, takes the letter and converts into something the code can use.
    def guess_letter():
        print()
        letter = input("take a guess at our mystery word:")
        letter.strip()
        letter.lower()
        print()
        return letter

    #allows you to select whether or not you wish to play again
    def play_again():
        answer = input('would you like to play again ? [y/n]')
        if answer in ('y','Y'):
            return answer
        else:
            print('thanks for playing !!!')
            sys.exit()

            #upon quitting game, scores are given for the duration o play session
    def scores():
        global player_score, computer_score
        print('HIGH SCORES')
        print('Player: ',player_score)
        print('Computer: ',computer_score)

        if __name__ == '__main__':
            start()

    while(letters_wrong != tries)and (''.join(clue)!=word):
        letter = guess_letter()
        if len(letter)==1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print("you've already picked ", letter)
            else:
                letters_tried = letters_tried + letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong +=1
                    print("Sorry"+ letter +"isn't what we are looking for")
                else:
                    print('congratulation,', letter,'is correct')
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print('Choose another')

        print(''.join(clue))
        print('Guesses: ', letters_tried)


        if letters_wrong == tries:
            print('Game over !! the word was ', word)
            computer+=1
            break
        if ''.join(clue)==word:
            print('You win')
            player_score +=1
            break
        return play_again()

start()
