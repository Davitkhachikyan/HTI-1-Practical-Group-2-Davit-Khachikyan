symbol_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def rome_numbers(num):
    previous_symbol = 0
    current_symbol = 0
    result = 0
    for _ in range(len(num)):
        current_symbol = symbol_dict[num[_]]
        if current_symbol <= previous_symbol:
            result += current_symbol
        else:
            result += current_symbol - 2 * previous_symbol
        previous_symbol = current_symbol
    return result


user_input = input("Enter a roman symbol: ")
print(rome_numbers(user_input))
