#string functions:
print("~~~~~~~~~~~STRING FUNCTIONS~~~~~~~~~~~~")#total 47 built in function for string


name='thivya_prakash'
print("slicing of string:")
print('\n',name)
print('\n',type(name))
print(name[1:6])        # [start: stop]
print(name[2:8])
print(name[1:10:2])     # [start: stop: (step) ]
print(name[4:11:3])
print(name[::-1])


# note: ' , " , "' they all same but ('''  ''') is used incase of multiple line...
#if not (' ') , (" ") is same for single line

print("\n string inbuilt functions ")
name='thivyaa'
print(name)
print(type(name))


c=name.capitalize()# 1.capitalize().....change the first letter into capital
print(c)


print(name.center(40,"~")) # 2.center()......display the str in center and with fill symbol


print(name.count('a'))  # 3.count().............returns the no of char in  given string the specified char presents 



b=name.encode()    # 4.encode().......str is changed into bytes
print(b)
print(type(b))# str is converted into byte
print(name.encode(encoding='utf-8'))
print(name.encode(encoding='utf-16'))
print(name.encode(encoding='utf-32'))

print(b.decode('utf-8'))  # 5.decode().....it can be done for bytes only (can be done after encode)



name1='PRAKASH'
print(name1.lower())  # 6.lower()....change the str into lowercase

name2='prakash'
print(name2.upper())  # 7.upper().....change the str into uppercase

name3='ThIvyAPraKAsh'
print(name3.swapcase())# 8.swapcase()...swaps lower case to upper and vice versa

name4='Straße'
print(name4.casefold()) # 9.casefold()....aggressive lowercase(for other lang..like german) either way output is just lowercase



name='python'
print(name.startswith('p')) # 10.startswith()
print(name.startswith('o'))

print(name.endswith('y'))  #  11.endswith()
print(name.endswith('n'))


print(name.find('o'))
print(name.find('n'))   #  12.find()
print(name.find('z'))
print(name.find('l'))



print(name.index('py'))  # 13.index()
print(name.index('o'))
print(name.index('th'))



data="     FOOTBALL"       # 14.lstrip()........remove the space in left side
print(data.lstrip())

data1="VOLLEYBALL       "      # 15.rstrip()......remove the space in right side
print(data1.rstrip())

data2="      SPORTS           "    # 16.strip().....remove space from eithersides
print(data2.strip())



info="science"
print(info.ljust(15,"~"))# 17.ljust()

print(info.rjust(20,"~"))# 18.rjust()


name='python'
name1='.py'
print(name.join(name1))    # 19.join()....joins two str..(ab)*c=(c*a)*(c*b)
name='bless'
name1='MTP'
print(name.join(name1))


info='prakash'
print(info.replace('pr','ak'))   # 20.replace().....replace the str with other str in given data
print(info.replace('ash','zxw'))


opp={"m":"p"}
str.maketrans(opp)               # 21.maketrans()...dict key into unicode...
{109: 'p'}
m1="Amma" # Amma to Appa
print(m1.translate(str.maketrans(opp)))
n={'G':'M','O':'A','A':'T','T':'E'}
str.maketrans(n)
{71: 'M', 79: 'A', 65: 'T', 84: 'E'}
data='GOAT'  # GOAT TO MATE
data.translate(str.maketrans(n))# 22.translate().....maketrans() must be created for translate function


print('\n')
print(' ^^^^^^^ is functions^^^^^^^')  # 23.is()...has its own inbulit functions
name='data_science'
print('case I:')
print('\n',name)
print('\n')
print(name.isalnum())
print(name.isalpha())
print(name.isascii())
print(name.isdecimal())
print(name.isdigit())
print(name.isidentifier())
print(name.islower())
print(name.isnumeric())
print(name.isprintable())
print(name.isspace())
print(name.istitle())
print(name.capitalize().istitle())
print(name.isupper())
print('\n')

name='12Abcs'
print('case II:')
print('\n',name)
print('\n')
print(name.isalnum())
print(name.isalpha())
print(name.isascii())
print(name.isdecimal())
print(name.isdigit())
print(name.isidentifier())
print(name.islower())
print(name.isnumeric())
print(name.isprintable())
print(name.isspace())
print(name.istitle())
print(name.capitalize().istitle())
print(name.isupper())

























