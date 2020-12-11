def missing_number(numbers):
    if numbers[0] != 1:
        return 1
    else:
        for i in range(len(numbers) - 1):
            if numbers[i] - numbers[i + 1] != -1:
                return (numbers[i] + numbers[i + 1]) // 2
        else:
            return numbers[-1] + 1


user_input = [int(i) for i in input("Enter numbers: ").split()]
user_input.sort()
print(missing_number(user_input))
