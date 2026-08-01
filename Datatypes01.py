#accessing elements in list 

mix = [10,12,'fahim',1,6]
print(mix[2])
print(mix[:3])
print(mix[3:])
print(mix[2:4])

#reverse 
print(mix[::-1])
print(mix[2::-1])


#operation on list 

z=[10]*100
print(z)

letters=['a','b','c','d']
print(letters)
stg=['fahim','mahir','sabbir']
print(stg)

#use concatenation to combine lists

conc=letters+stg
print(conc)




#unpacking list\

var=list("fahim")
print(var)

numbers=[1,2,3,4,5]
one,*other_= numbers
print(one)
print(other_)


#methods in list

Numbers=[1,2,3,4,5]
Numbers.append(6)
print(Numbers)

Numbers.extend(stg)
print(Numbers)
Numbers.insert(2,'zinia')
print(Numbers)
Numbers.remove('sabbir')
print(Numbers)






Var1=['a','b','c',]
Var1.sort()
print(Var1)





#built in function eith lists \

x=[10,12,13,14,15,]
print(x)
print(len(x))
print(sum(x))
print(min(x))
print((sum(x)/len(x)))






#python tuples
# Tuple is a collection of immutable heterogeneous python object 


#creating tuples 

emp=()
print(emp)
print(type(emp))



city ="pune"
print(type(city))

city ="pune",
print(type(city))

city=("pune")
print(type(city))

city=("pune",)
print(type(city))

city = ("pune","mumbai")
#concatenation of tuples
num =1,2
print(city+num)
print(type(city))
#nesting
nest=(city,num)
print(nest)
#repetition
print(city*5)
rep=("python",)
print(rep*5)

#slicing 

num=(1,2,3,4,5,6,7,8,9)
print(num[2:5])
print(num[::-1])

#unpacking tuples
tuple("fahimhasan",)
print(tuple("fahimhasan",))


num=(1,2,3,4,5)

a,*b,c=num
print(a,b,c,)