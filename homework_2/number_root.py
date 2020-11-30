def summery(number):
    sum = 0
    for i in number:
        sum += int(i)
    if sum < 10:
        return sum
    else:
        return summery(str(sum))


print(summery("12341"))
