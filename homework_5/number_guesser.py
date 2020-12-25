greet = input(" Think of a number between 1 and 999. Input 0 once you’re ready to play: ")


def number_guesser(first, last):
    mid = (last + first) // 2
    print(mid)
    command = input("Enter a sign: ")
    if command == "1":
        number_guesser(mid, last)
    elif command == "-1":
        number_guesser(first, mid)


number_guesser(1, 999)
