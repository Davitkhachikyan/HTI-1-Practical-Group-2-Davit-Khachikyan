def char_count(text):
    dictionary = {}
    for i in text:
        dictionary[i] = dictionary.get(i, 0)+1
    return dictionary


user_input = input("Enter a text: ")
print(char_count(user_input))
