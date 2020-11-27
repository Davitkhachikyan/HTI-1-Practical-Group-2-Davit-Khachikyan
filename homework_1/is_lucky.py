number = input("Enter a number")
half_len_number = len(number) // 2
list1 = number[: half_len_number]
list2 = number[- half_len_number:]
temp1 = 0
temp2 = 0
for i in list1:
    temp1 += int(i)
for j in list2:
    temp2 += int(j)
if temp1 == temp2:
    print("Yes")
else:
    print("No")