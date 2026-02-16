# Program to count vowels

a = input("Enter word : ")

count = 0
for v in a:
    if v in("aeiouAEIOU"):
         count += 1

print("No. of vowels: ", count)