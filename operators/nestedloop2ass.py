num = int(input("Enter a Number:"))

for i in range(0, num):
    for j in range(0, i+1):
        print("*", end="")
    print()