list=[1,2,5,7,2,3]
max=list[0]
for i in list:
    if i >= max:
        max=i
print(max)


list1=[1,2,2,3,4,5,6,6]
count=0
for i in list1:
    if i%2==0:
        count+=1
print(count)


list2=[1,2,2,3,4,5,6,6]
sum=0
for i in list2:
    sum+=i
print(sum)

#reverse list
list3=[1,2,2,3,4,5,6,6]
nl=[]
ll=len(list3)
for i in range(ll,0,-1):
    nl.append(list[ll-1])
    ll-=1
print(nl)

#copy elements
list4=[1,2,2,3,4,5,6,6]
nl1=[]
ml1=[]
for i in list:
    nl.append(i)
print(nl1)
ml1.extend(list)
print(ml1)


##nested lists

mat1=[[1,2,3,4],[1,2,3,4],[1,2,3,6]]
mat2=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
list5=[]
m=0
for i in mat1:
    n=0
    for j in range(0,4):
        
        list5.append(mat1[m][n] + mat2[m][n])
        n+=1
    m=m+1
print(list5)

    
