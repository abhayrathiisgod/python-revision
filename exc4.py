#list in pythonn

# everything works on 0-based indexing
countries = ['united kingdom' ,'Nepal','India','Gotham']
print(countries)
print(countries[3])
print(countries[3][2])
countries[3]='hanuman nagar'
#last 2 elements
print(countries[1:])
print(countries[1:4])
print(countries[-2])
print(len(countries))
# CAPITAL TTTT
temp = ['apple',1,True,'banana']
print(type(countries[1]))
# using list constructor
countries = list(('Nigeria',34,False))
#list methodss
list1 = [1,2,3,4,5]
list2 =['banana','apples','mango','oranges','mango']
list1.extend(list2)
print(list1)
list2.append('cheryy')
print(list2)
#in between
list2.insert(2,'bananananna')
print(list2)
list2.remove('cheryy')
#list2.clear()
print(list2.index('mango'))
print(list2.count('mango'))
list1.sort()
list2.reverse()
print(list2)
list3 = list2.copy()
list2.pop()
print(list3)
