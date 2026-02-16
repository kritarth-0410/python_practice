n = int(input("enter number here: "))

for i in range(2, n):
    if(n%i == 0):
        print("this is not prime number")
        break
else:
    print("this is prime number")