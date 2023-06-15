#program to find the multiples of a number(the divisor )out of the given five numbers:
n1=float(input('enter the first number :'))
n2=float(input('enter the second number:'))
n3=float(input('enter the third number:'))
n4=float(input('enter the fourth number:'))
n5=float(input('enter the fifth number:'))

d=float(input('enter the divisor :'))

if (d>0 and n1>0 and n2>0 and n3>0) :
    if (d!=0 and n1!=0):
        r=n1%d
        if (r==0):
            print('number',n1,'is divisble by',d)
    if (d!=0 and n2!=0):
        r=n2%d
        if(r==0):
            print('number',n2,'is divisible by',d)
    if (d!=0 and n3!=0):
        r=n3%d
        if(r==0):
            print('number',n3,'is divisible by',d)
    if (d!=0 and n4!=0):
        r=n4%d
        if(r==0):
            print('number',n4,'is divisible by',d)
    if (d!=0 and n5!=0):
        r=n5%d
        if(r==0):
            print('number',n5,'is divible by',d)
        
else:
    print('....enter a valid number...')
                                 


                         
