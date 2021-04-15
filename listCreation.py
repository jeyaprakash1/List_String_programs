# List creation 1

groceryList=[]
print(type(groceryList))
print(groceryList)
print(len(groceryList))

# List creation 2

marklist=[100,89,90,98]
print(marklist)
print(len(marklist))

# String into list

name = 'prakash'
l=list(name)
print(l)

# List creation 4

l= list(range(5))
print(l)

# List creation 5

s='happy new year'
list= s.split()
print(list)
for x in list:
    print(x)
    
# List access and Slicing

l=[1,2.6,'hello',True]
print(l[0])
print(l[-1])
print(l[0:3])
print(l[3:0:-1])

# List is mutable

l=[1,2.6,'hello',True]
print(id(l))
l[0]=77
print(l)
print(id(l))











