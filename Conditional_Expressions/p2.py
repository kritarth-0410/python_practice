p = int(input("enter marks : "))
c = int(input("enter marks : "))
m = int(input("enter marks : "))

total_percentage = (100*(p+c+m))/300

if(total_percentage>=40 and p>33 and c>33 and m>33):
    print("PASSED : ", total_percentage)
 
else:
    print("ESSENTIAL REPEAT !!", total_percentage )

