def total():
    a = segment_length(x1, y1, x2, y2)
    b = segment_length(x2, y2, x3, y3)
    return 2 * (a + b)


def segment_length(x1, y1, x2, y2):
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return d


user_input = input("Enter coordinates: ").split()
lst = [float(i) for i in user_input]
print(lst)
x1 = lst[0]
y1 = lst[1]
x2 = lst[2]
y2 = lst[3]
x3 = lst[4]
y3 = lst[5]
x4 = lst[6]
y4 = lst[7]

print(total())
