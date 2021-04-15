# input: Sun Mon Tues Wednes Thurs Fri Satur
# output: Tuesday wednesday Thurs

input= "Sun Mon Tues Wednes Thurs Fri Satur"
words=input.split()
words2=[]
for word in words:
    if len(word)=='s':
        words2.append(word+'day')
#print(words2)
out=' '.join(words2)
print(out)

# print 4 letter or above word only print

# if len(word)>=4:
