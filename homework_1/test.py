S = input("enter word")
s = input("enter word")
if s == S[0:len(s)]:
    print("Prefix")
elif s == S[-len(s):]:
    print("Suffix")
elif s == S[0:len(s)] and s == S[-len(s):]:
    print("both")
else:
    print("neither")