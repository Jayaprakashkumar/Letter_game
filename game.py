import random


class GameClass:

    @staticmethod
    def random_gen(length):
        return random.randint(0,length)

    @staticmethod
    def dict_obj(num,name):
        obj = {
                "id": num,
                "word": name,
                "status": "Gave up",
                "badGuess": 0,
                "missLetter": 0,
                "score": 0
            }
        return obj

    @staticmethod
    def result_table():
        print("Game\t\t", end='')
        print("Word\t\t", end='')
        print("Status\t\t", end='')
        print("Bad Guesses\t\t", end='')
        print("Missed Letters\t\t", end='')
        print("Score\t\t", end='')
        print("\n")
        print("----\t\t", end='')
        print("----\t\t", end='')
        print("------\t\t", end='')
        print("-----------\t\t", end='')
        print("--------------\t\t", end='')
        print("-----\t\t", end='')
        print("\n")

    @staticmethod
    def output(arr_list):
        for lis in arr_list:
            print(lis['id'], "\t\t\t", end='')
            print(lis['word'], "\t\t", end='')
            print(lis['status'], "\t", end='')
            print(lis['badGuess'], "\t\t\t\t", end='')
            print(lis['missLetter'], "\t\t\t\t\t", end='')
            print('%.2f' % round(lis['score'], 2))
            print("\n")

