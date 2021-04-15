# input: ['how','do','you','do']
# output:['woh','do','uoy','do'] 
#      and
# output:woh do uoy do

sen=input("enter a sentence ")
l=sen.split()
print(l)
i=0
l2=[]
while i<len(l):
    if i%2==0:
        l2.append(l[i][::-1])
    else:
        l2.append(l[i])
    i+=1
print(l2)

output =' '.join(l2) # join is a string function
print(output) 
