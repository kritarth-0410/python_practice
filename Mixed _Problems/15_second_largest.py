l = [12,4,19,7,15]

largest = l[0]
second = l[0]

for i in l:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("largest", largest)
print("second largest", second)


smallest = l[0]
for i in l:
    if i<smallest:
        smallest = i
    print(smallest)