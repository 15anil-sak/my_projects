name='anil'
password=123456
x=str(input('enter your name:'))
y=str(input('enter your password:'))
if x==name and y==password:
    print('''
           1.deposite
          2.withdraw
          3.mini_statement
          4.exit
          ''')
    amount=5000
    option=int(input('enter your choice:'))
    if option==1:
        deposite=input('enter your money:')
        amount+=deposite
        print('total amount is:',amount)
    elif option==2:
        withdraw=input('enter money:',withdraw)
        amount-=withdraw
        print('your amount is:',amount)
    elif option==3:
        print(''' --------
              custmor name:anil
              total amount=amount
              --------------''')
    elif option ==4:
        print('exit')
else:
    print("given credits are not valid")

