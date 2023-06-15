#program to input three numbers and sum them....
n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
n3=int(input("enter the third number:"))
sum1=n1+n2+n3
print("sum of all three numbers is",sum1)
if (n1!=n2 and n2!=n3 and n3!=n1):
    print("sum of non duplicate number is",sum1)

else:    
    if (n1==n2 and n2!=n3 and n3!=n1):
        sum2=n2+n3
        print("sum of non duplicate numbers is",sum2)
    
    if (n1!=n2 and n2==n3):
        sum2=n1+n2       
        print("sum of non duplicate numbers is",sum2)

    if (n3==n1 and n3!=n2):
        sum2=n1+n2        
        print("sum of non duplicate numbers is",sum2)
        
    if(n1==n2 and n2==n3 and n3==n1):
        sum1=n2+n3
        print("sum of non duplicate numbers is",sum1)
        
        
