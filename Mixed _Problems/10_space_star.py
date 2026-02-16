# Program to print space and star together

# for i in range(1,6):
#     for sp in range(5-i):
#         print(" ", end = "")

#     for st in range(i):
#         print("*", end = "")

#     print()



# Next 

for i in range(1,6):
    for j in range(1,i+1):
        print("*", end="")
    print()
for k in range(4,0,-1):
    for x in range(1,k+1):
        print("*", end="")
    print()


    # With ONE Loop
 
for i in range(1,10):
    if i<=5:
        stars = i
    else:
        stars = 10-i

    for j in range(stars):
        print("*", end = "")
    print()