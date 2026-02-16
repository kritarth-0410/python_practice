# Program to check word

# a = input("Enter word: ")
# if a == a[::-1]:
#     print("It is reversible: ", a)

# else:
#     print("It is not reversible: ", a)


a = input("Enter word: ")
rev = "" 
for i in a:
    rev = i + rev

if a == rev:
    print("reversible")

else:
    print("not reversible")