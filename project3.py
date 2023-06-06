#types of operators(part II):
print("6.")
print("-----------------BITWISE OPERATOR--------------")
print("~~~~~~~~~~  includes: &,|,^,>>,<< ~~~~~~~~~~")
print(' "&" denotes (AND)')#(ab)
print('\t''0 & 0:',0 & 0)#\t is for the space same as \n~~~~[\t is tab space while ;\n is new line space]
print('\t''1 & 0:',1 & 0)
print('\t''0 & 1:',0 & 1)
print('\t''1 & 1:',1 & 1)
print('\n')
print(' "|" denotes (OR)')#(a+b)
print('\t''0 | 0:',0 | 0)
print('\t''1 | 0:',1 | 0)
print('\t''0 | 1:',0 | 1)
print('\t''1 | 1:',1 | 1)
print('\n')
print(' "^" denotes (XOR)')#XOR is exclusive OR gate ....(a'b+b'a){combination of AND gate and OR gate}
print('\t''0 ^ 0:',0 ^ 0)
print('\t''1 ^ 0:',1 ^ 0)
print('\t''0 ^ 1:',0 ^ 1)
print('\t''1 ^ 1:',1 ^ 1)
print('\nLeft Shift: (<<) ')#left shift bitwise
a=12                             # 12:  32 16 8 4 2 1   (binary)
print('\n')                      #      0   0 '1 1 0 0'
print('value is:',a)
print('left shift by 2 :',a<<2)   # a<<2:    16 8 4 2 1
print('left shift by 6 :',a<<6)    #      '1  1 0 0' 0 
print('left shift by 17:',a<<17)

print('\nRight Shift: (>>) ')#right shift bitwise
a=20
print('value is:',a)
print('Right shift by 1 :',a>>2)
print('Right shift by 15 :',a>>15)
b=29978
print('\nvalue is:',b)
print('Right shift by 4 :',b>>4)
print('Right shift by 7 :',b>>7)
print("_______________________________________________________________________________________________")
print("\n7.")
print("-----------------IDENTITY OPERATOR--------------")
print("~~~~~~~~~~  includes: is,isnot,in ~~~~~~~~~~")
a="python"
print('\n')
print('is ,isnot:')
print("python")
print("java" is a)
print("java" is not a)
b="hello world today is lovely"
print('\n')
print(b)
print("world" is b)
print("nice" is b)
print(" lovely" is b)
print("tomorrow" is not b)
print('\n')
print('in:')
c=(1,3,6)
print(c)
print( 1 in c)
print(8 in c)
print(3 in c)
print("__________________________________________________________________________________________")

