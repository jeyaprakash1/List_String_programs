# input: ['wish','you','a' ,'very' ,'happy', 'new','year']
# output:['hsiw','a','yppah','raey']

sen=input("enter a sentence ")
l=sen.split()
print(l)
i=0
l2=[]
while i<len(l):
    l2.append(l[i][::-1])
    i+=2
print(l2)
