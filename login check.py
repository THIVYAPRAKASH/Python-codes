name=input('enter the mail id:')
p=input('enter the password:')
if len(p)<5:
     print('.......Your password is weak........')

else:
     if p.isalpha():
         print('Consider including a number..')
     elif p.isnumeric():
          print('your password doesnt have any alhabets kindly include...')
     elif (p.isascii()):
          print('\nyour are secure !!')
          

