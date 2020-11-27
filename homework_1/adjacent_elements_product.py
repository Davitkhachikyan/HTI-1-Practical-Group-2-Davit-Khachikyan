num = input("Enter a number :").split()
int_list = []
multiplied = []
for i in num:
    int_list.append(int(i))
for j in range(len(int_list)-1):
    multiplied.append(int_list[j] * int_list[j + 1])
largest = multiplied[0]
for x in multiplied:
    if x > largest:
        largest = x
print(largest)
