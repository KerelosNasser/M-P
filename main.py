f = int(input("Enter the first number: "))
s = int(input("Enter the second number: "))

if f > s:
    print(f, "is bigger than", s)
elif s > f: 
    print(s, "is bigger than", f)
else:
    print("Both are equal")