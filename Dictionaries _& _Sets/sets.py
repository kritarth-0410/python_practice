# s = set()    use to create empty set 
# print(s, type(s))


s1 = {2 ,23, 434, 5,5 ,65}
s2 = {43,534,2,5,65,45}
print(s1 - s2)
print(s2 - s1)
print(s1.union(s2))
print(s1.intersection(s2))