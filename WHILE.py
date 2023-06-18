print('\t\t*******AMAZON*********')
n=input('\nAre you in a mood for a shopping(Yes/No)...?')
if(n=='Yes'): 
    x=1
    while(x<4):
        u=input('Enter you product=')
        x+=1
    Y=input('\nDo You Wanna Continue..!')
    if(Y=='yes'):       
        i=1
        while(i<5):
            u=input('Enter you product :')
            i+=1
        p=input('\nDo You Still Wanna Continue...?')
        if(p=='no'):
            print('~~~~~Thanks For Shopping~~~~~~')
        else:
             d=0
             while(d<100):
                    h=input('Well Pick Another One Product=')
                    r=input('Do You Want to Continue..(yes/no):')
                    if(r=='yes'):                        
                        d+=1
                    else:
                        print('\n....THANK_YOU....')
                        break;                             
    else:
        print('\nTHANKS COME AGAIN')                
else:
    print('\t~~~~~~ EXIT ~~~~~~~~')


