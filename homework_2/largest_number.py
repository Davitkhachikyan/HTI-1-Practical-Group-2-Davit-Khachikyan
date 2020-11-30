def largest_number(number):
    digit1 = ""
    digit2 = ""
    for i in number:
        digit1 += i
    lst = list(digit1)
    lst.sort(reverse=True)
    for i in lst:
        digit2 += i
    if int(digit2) > int(digit1):
        return "Yes"
    else:
        return "No"


user_input = input("Enter a digit: ")
print(largest_number(user_input))
