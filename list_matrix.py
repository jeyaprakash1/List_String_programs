# Sum of diagonal elements in Matrix

l1=[[1,2,3],
    [4,5,6],
    [7,8,9]]
sum=0
for i in range(len(l1)):
    l2=l1
    for j in range(len(l2)):
        if i==j:
            sum=sum+l1[i][j]
            #print(l1[i][j],end="")
print(sum)
