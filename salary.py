# for the salary excluding the travel expenses
name=input('enter the name:')
if name.isalpha():    
    b=input('enter the id no:')    
    if len(b)>3 and len(b)<15: 
        s=int(input('enter the basic salary:'))        
        if (s>1000):
            t=int(input('travel expenses:'))            
            if (t>10000 and t<100):
              print('enter a valid travel expense')              
            else:
              n=s-t
              print('\n-----------------------------------------')
              print('your name:',name.upper())
              print('your id :',b.upper())
              print('your average salary',s)
              print('the salary after expense reduction is',n,'$')              
        else:
            print('*****You have enter a invalid salary check again*****')
    else:
       print('wrong id...!')
else:
    print('invald name...check again')




