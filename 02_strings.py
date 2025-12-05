# a="jamid"
# a='jamid' 
a= '''jamid'''
name= "jamid is my name"
nameshort=len(name)     # for len
print(nameshort)

nameshort=name[0:5]     #for slices      -ve indicies from backwards
print(nameshort)

character1=name[2]      #for onr single element
print(character1)

slice=name[-7:-1]           # ending index is not included
slice=name[:5]                 #automatically takes 0
slice=name[2:]                 #automatically takes upper value of str
print(slice)


#slicing with skipping

word="amazing"
skip=word[1:6:2]                #skip/jump by 2
print(skip)

aqib="hello my name is aqib"
skip=aqib[0:15:4]
print(skip)






