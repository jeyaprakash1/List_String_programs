# input: Sun Mon Tue Wednes Thurs Fri Satur
#output: Sunday Monay Turesday Wednesday Thursday Friday Saturday

input= "Sun Mon Tue Wednes Thurs Fri Satur"
words=input.split()
words2=[]
for word in words:
    words2.append(word+'day')
#print(words2)
out=' '.join(words2)
print(out)


