list1 = set(['Blue', 'Black', 'Green', 'Red', 'Orange'])
list2 = set(['Red', 'Brown', 'Orange', 'Pink'])

diff = list1.difference(list2)
print(diff)


s1=input("Enter first string: ")
s2=input("Enter second string: ")
print(s2[0]+s1[1:]," ",s1[0]+s2[1:])
