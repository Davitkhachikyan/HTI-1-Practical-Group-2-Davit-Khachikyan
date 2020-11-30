def summery(number):
    total = 0
    for i in number:
        total += int(i)
    if total < 10:
        return total
    else:
        return summery(str(total))


user_output = input("Enter a number: ")
print(summery(user_output))
