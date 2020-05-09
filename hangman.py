import random
import re


class Hangman:
    supported_letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    words_list = ['python', 'java', 'kotlin', 'javascript']

    def __init__(self):
        self.random_word = random.choice(self.words_list)
        self.hint = "-" * len(self.random_word)
        self.hint_list = list(self.hint)
        self.lives = 8
        self.already_chosen = set()
        print("H A N G M A N")
        self.__menu()

    def __check_letter(self, letter):
        matches = [m.start() for m in re.finditer(letter, self.random_word)]
        if matches:
            for match in matches:
                self.hint_list[match] = letter
            tmp = ""
            for ele in self.hint_list:
                tmp += ele
            self.hint = tmp
            return True
        else:
            return False

    def __menu(self):
        a = input('Type "play" to play the game, "exit" to quit:')
        if a == "play":
            self.__play()
        elif a == "exit":
            exit(0)
        else:
            self.__menu()

    def __play(self):
        while True:
            if self.hint == self.random_word:
                print(self.random_word)
                print("You guessed the word!")
                print("You survived!")
                break
            if self.lives == 0:
                print("You are hanged!")
                break

            input_letter = input(f"\n{self.hint}\nInput a letter:")

            if input_letter in self.already_chosen:
                print("You already typed this letter")
            elif len(input_letter) != 1:
                print("You should print a single letter")
            elif input_letter not in self.supported_letters:
                print("It is not an ASCII lowercase letter.")
            else:
                letter_exist = self.__check_letter(input_letter)
                self.already_chosen.add(input_letter)

                if letter_exist:
                    print()
                else:
                    print("No such letter in the word")
                    self.lives -= 1


Hangman()
