userLimit= int(input("Limit: "))
for i in range (1, userLimit+1):
    if ((i % 5 == 0) & (i % 3 == 0)):
        print("FizzBuzz!")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)