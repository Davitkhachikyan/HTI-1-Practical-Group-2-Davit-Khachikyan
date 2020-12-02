def lucky_number(number):
    sum1 = 0
    sum2 = 0
    for i in number[0:: 2]:
        sum1 += int(i)
    for i in number[1:: 2]:
        sum2 += int(i)
    if sum1 == sum2:
        return "Yes"
    else:
        return "No"


user_input = input("Enter a number")
print(lucky_number(user_input))
