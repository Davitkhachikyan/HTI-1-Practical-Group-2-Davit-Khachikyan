import random

with open("/home/davo/testfile", "r+", encoding="utf - 8") as f:
    guess_word = random.choice([line for line in f]).strip()


def find_index(word, value):
    start = -1
    indexes = []
    while True:
        try:
            ind = word.index(value, start + 1)
            indexes.append(ind)
            start = ind
        except ValueError:
            break
    return indexes


def hangman(word):
    guess_limit = 5
    output = "-" * (len(word))

    while guess_limit != 0:
        print(output)
        user_input = input(f"Guess the word. {guess_limit} mistakes left: ").lower()
        print(f"Guess a letter: {user_input.upper()}")
        if user_input in word:
            temp_position_list = find_index(word, user_input)
            for pos in temp_position_list:
                temp = list(output)
                temp[pos] = user_input
                output = "".join(temp)
        else:
            guess_limit -= 1
        if guess_limit == 0:
            print("You lost the game")
        elif word == output:
            print("You won the game")
            break


hangman(guess_word)
