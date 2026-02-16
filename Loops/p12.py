# Program to find Factorial
n = int(input("enter number here : "))
fact = 1
for i in range(1, n+1):
    fact = fact*i
print(fact)


#from while loop

n = int(input("enter number here : "))
fact = 1
i = 1
while(i<=n):
    fact = fact * i
    print("Faact is ", fact)