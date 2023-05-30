#binary       and    hexademical:
#binary: 0&1~(2^n)         hexadecimal:0-9,A,B,C,D,E~(16^n)
#Bit length:8

# using bin():
print("************BINARY************")

print(bin(3345))
print(bin(829))
print(bin(123))
print(bin(88771))
print(bin(23))

# using hex():
print("************HEXADECIMAL**********")

print(hex(778))
print(hex(3323))
print(hex(11223))
print(hex(909))
print(hex(8891789))


#using type():\\ informs about the data type:
print("-----------DATA TYPES-------------")

a=25
print(type(a))
b=3.5
print(type(b))
c=True
print(type(c))
d="hello"
print(type(d))
e=['p','y','t','h','o','n']
print(type(e))
f=(23,45,67,55)
print(type(f))
g={1,2,3,4}
print(type(g))
h={"employee":"kavin","age":30}
print(type(h))


#Python is 100% object oriented programming language(OOPS)......(in py objects are the variables)
#/*py is highly efficient for memeroy spacing than other language*/

#using the id():
print("...........address of an variable...............")
A=12    #here A just refers the address of 12....were 12 is stored
B=18    #here b just refers the address of 12....were 18 is stored
print(A)
print(id(A))
print("address of 12 is",id(12))
print(B)
print(id(18))
print("address of 18 is",id(18))
c=12   #here no new space/id will be created....c will jusr refer the already existing address of 12
print(id(c))
print("address of c is",id(12))

#*thus its clear python is ideal in memory spacing or adressing compared to other language*



           
       
