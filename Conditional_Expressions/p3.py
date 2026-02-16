p1 = "make lot of money"
p2 = "buy now"
p3 = "click here"

comment = input("comment here")

if(p1 in comment or p2 in comment or p3 in comment):
    print("spam comment detected")

else:
    print("no spam comment identified")