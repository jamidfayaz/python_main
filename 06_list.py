friends=["jamid","aqib","403",1,"anayat"]
print(friends[0])
friends[0]="fayaz"              #lists are mutable unlike strings ,we can change value of lists
print(friends[0])
print(friends[0:2])              #start end
print(friends[0:5:2])           # start end space


##### list methods
friends[0]="fayaz"
friends.append("yousuf")
print(friends)


####list methods
L=[1,2,3,4,7,6]
L2=[7,8]
L.sort()            #for sorting type is imp ie similar type 
L.reverse()
L.insert(3,66)       # 3rd position pr 66 insert
L.pop(2)
L.remove(7)
L.extend(L2)   #adds multiple elements or list to another
print(L)

print(sum(L))

