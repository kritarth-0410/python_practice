n = int(input("enter number here: "))

for i in range(1, 11):
    print(n*i)

# again in while loop 

n = int(input("enter number here: "))

i = 1

while(i<11):
    print(f"{n} X {i} = {n * i}")
    i +=1