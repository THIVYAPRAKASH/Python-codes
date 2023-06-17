#program to display the area and perimeter of the circle:

print('what you want to find ...select: \t \n1.for perimeter\n2.for area')
choice=int(input('enter the choice (1 or 2):'))

if(choice == 1 or 2):            
    if choice==1:                
        r=float(input('enter the radius:'))        
        if(r>0):            
            name='PERIMETRE OF CIRCLE'
            print(name.center(50,'*'))
            p=2*3.14*r
            print('the perimeter of the circle is',p)    

    if choice==2:                
        r=float(input('enter the radius:'))     
        if (r>0):          
            name='AREA OF CIRCLE'
            print(name.center(30,'*'))
            p=3.14*r*r
            print('the area of the circle is',p)
          
else:    
 name='invalid choice'
 print(name.center(50,'#'))
    
   
