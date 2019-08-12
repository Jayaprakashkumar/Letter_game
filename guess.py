from game import *
from stringDatabase import *


class GuessClass(object):

    def __init__(self):
        self.arr_list = []

    def main_class(self):
        for count in range(1, 101):
            n = GameClass.random_gen(GameInpOut.length)
            current_string = GameInpOut.input_file[n]

            print(current_string)
            temp_string = current_string
            total_freq = GameInpOut.frequency[temp_string[0]] + GameInpOut.frequency[temp_string[1]] + \
                         GameInpOut.frequency[temp_string[2]] + GameInpOut.frequency[temp_string[3]]
            result_string = "----"
            guess_count = 0
            guess_letter = 0
            my_dict = GameClass.dict_obj(count, current_string)

            while True:
                print("\n** The great guessing game **")
                print("Current Guess:", result_string)
                print("g = Guess", end='')
                print("  t = Tell Me", end='')
                print("  l = For a letter", end='')
                print("  q = Quit the game")
                choices = input()

                if choices == "g":
                    print("Guess the correct answer")
                    guess_str = input()

                    if guess_str.casefold() == current_string.casefold():
                        print("Genius!! Found the word\n")
                        my_dict['status'] = "Success"
                        if my_dict['missLetter'] > 0:
                            my_dict['score'] = round(total_freq / guess_letter, 2)
                        else:
                            my_dict['score'] = total_freq

                        self.arr_list.append(my_dict)
                        break
                    else:
                        print("Bad Guess!! Try Again\n")
                        guess_count = guess_count + 1
                        my_dict['badGuess'] = guess_count

                elif choices == "l":
                    print("Enter a  letter:")
                    input_char = input()
                    res_list = list(result_string)
                    guess_letter = guess_letter + 1
                    my_dict['missLetter'] = guess_letter
                    for index, val in enumerate(temp_string):
                        if val.casefold() == input_char.casefold():
                            res_list[index] = val
                            total_freq = total_freq - GameInpOut.frequency[val]

                    result_string = "".join(res_list)
                    print(result_string)

                elif choices == "t":
                    print("The correct Answer", current_string)
                    print("You LOST!! Try Again..\n")
                    my_dict['score'] = -total_freq
                    my_dict['status'] = "Give up"
                    self.arr_list.append(my_dict)
                    break

                elif choices == "q":
                    print("Quit the program\n")
                    my_dict['score'] = -total_freq
                    self.arr_list.append(my_dict)
                    GameClass.result_table()
                    GameClass.output(self.arr_list)
                    return


the_guess = GuessClass()
the_guess.main_class()


