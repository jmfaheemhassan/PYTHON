list =[10,20,30,40,50]
print(type(list))

tuple=tuple(list)
print(type(tuple))



#nesting of tuple in a list 

lst=[(1,2,3),(4,5,6),(7,8,9)]
print(lst)

lst.append(("tuple",))
print(lst)

lst.remove((1,2,3))
print(lst)


#nesting list in a tuple
tup=(["fahim","hasan"],["python","java"])
print(tup)
tup[0].append("programming")
print(tup)
tup[1].remove("java")
print(tup)