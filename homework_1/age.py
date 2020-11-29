year = input("Enter year: ")
if year[-2:] == "00":
    age = int(year) // 100
else:
    age = int(year) // 100 + 1
print(age)


