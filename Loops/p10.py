#Program to print the table

n = int(input("Enter Number: "))
product = 1
for i in range(1,11):
    product = n * i
    print(f"{i} X {n} = ", product)
