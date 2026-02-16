# for i in range(1,51):
#     if(i%3 == 0 and i%5 == 0):
#         print(i)



# primes = []
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j == 0:
#             break

#     else:
#         print(i)
#         primes.append(i)
# print(primes)
# print("total primes:", len(primes))


# n = int(input("enter number: "))

# if n <=1:
#     print("not prime")
# else:
#     for k in range(2,n):    
#         if n%k == 0:
#             print("not prime")
#             break

#     else:
#         print("prime")



n = int(input("enter number: "))
if n <=1:
    print(False)

else:
    for j in range(2,n):
        if n%j == 0:
            print(False)
            break

    else:
        print(True)
