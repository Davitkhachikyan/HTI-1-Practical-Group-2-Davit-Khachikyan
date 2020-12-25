def is_palindrome(word):
    while len(word) != 0:
        if word[0] == word[-1]:
            word = word[1:-1]
            is_palindrome(word)
        else:
            return "No"
    return "Yes"


user_input = input("Enter a text")
print(is_palindrome(user_input))
