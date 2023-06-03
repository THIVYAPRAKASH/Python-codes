#types of operators in python:
print("TYPES OF OPERATORS IN PYTHON:")
print("\n1.")
print("-------------ARITHEMATIC OPERATOR---------------")
print("~~~~~~~~~~  includes: +,-,*,//,/,%  ~~~~~~~~~~")
a=15
b=20
print("the two numbers a,b is",a,b)
print("sum :",a+b)
print("subtarction:",a-b)
print("multiply:",a*b)
print("when a is divided by 3 remainder:",a%3)
print("when a is divided by 3 quotitent:",a/3)
print("when b is divided by 2 remainder:",b%2)
print("when b is divided by 2 quotitent:",b/2)
print("float division for a//3 & b//2:",a//3,",",b//2)
print("________________________________________________________________________________________________")

print("\n2.")
print("-----------------SHORTHAND OPERATOR--------------")
print("~~~~~~~~~~  includes: +=,-=,*=,**=,/=,%=,//=  ~~~~~~~~~~")
c=30
print("value of c is :",c)
c+=10
print("adding 10 to c:",c)
c=30
c-=10
print("subtracting 10 from c:",c)
c=30
c*=10
print("c multiplyed by 10:",c)
c=30
c**=10
print("c to power 10 :",c)
c=30
c/=10
print("c divided by 10:",c)
print("__________________________________________________________________________________________________")
print("\n3.")
print("-----------------RELATIONAL/COMPARISION OPERATOR--------------")
print("~~~~~~~~~~  includes:  < , > , <= , >= , == , =! ~~~~~~~~~~")
x=69
y=229
print("x=",x,"y=",y)
print("case 1: (x>y)")
print(x>y)
print("case 2: (x<y)")
print(x<y)
print("\nsimilarly.....")
w=121
e=115
r=99
print("\n","w=",w,"e=",e,"r=",r)
print("case(I):",(w>e),"//(w>e),","case(II):",(e<r),"//(e<r),","case(III):",(r>e),"(r>e),","case(IV):",(w<=r),"//(w<=r),","case(V):",(r>=e),"//(r>=e),","case(VI):",(r==w),"//(r==w),","case(VII):",(w!=r),"//(w!=r)")
print("________________________________________________________________________________________________")
print("\n4.")
print("-----------------LOGICAL OPERATOR--------------")#(AND : *)#(OR : +)
print("~~~~~~~~~~  includes: AND,OR,NOT ~~~~~~~~~~")#AND if one is false the output is false,#OR if one is true then the output is true
u=True
i=False
print("u:True","\t","v:False")
print("\n")
print(u and i,"(u and i)")
print(u or i,"(u or i) ")
print(not u,"(not u)")
print(not i,"(not i)")
print("________________________________________________________________________________________________")
print("\n5.")
print("-----------------LOGICAL COMPARISION OPERATOR--------------")
print("~~~~~~~~~~  includes: both logic and relational ~~~~~~~~~~")
a=10
b=20
c=30
print(not(b>c))

print((a>b)and(c<b))
print((b>c)or(a>b))
print((c>=b)and(b<a))
print(((b>c)or(a>b))and((a>b)and(c<b)))
print(((b>a)and(c>b))or((a>c)and(c<b)))
print("________________________________________________________________________________________________")









 




























