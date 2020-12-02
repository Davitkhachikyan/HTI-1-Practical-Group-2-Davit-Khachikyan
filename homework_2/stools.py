
def stools(height):
    int_list = []
    summery = 0
    for i in height:
        int_list.append(int(i))
    max_height = max(int_list)
    for i in int_list:
        x = max_height - i
        summery += x
    return summery


user_input = input("Enter heights: ").split()
print(stools(user_input))