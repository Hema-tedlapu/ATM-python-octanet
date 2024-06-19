print("Please insert your CARD")

print("*************************************************")



password = 9898

pin = int(input("Enter your ATM PIN : "))

print("*************************************************")



balance = 1000

if pin==password:
    while True:
        print("""
             1 == balance
             2 == withdraw balance
             3 == deposit balance
             4 == exit
         """)

        print("*************************************************")

        try:
              
           option = int(input("Please enter your choice : "))

           print("*************************************************")
        except:
            
           print("Please enter valid option")

           print("*************************************************")



        if option == 1:
        
            print("your current balance is :",balance)

            print("*************************************************")



    
        if option == 2:
            
        
            withdraw_amount = int(input("Enter your Withdrawal amount : "))

            print("*************************************************")

            balance = balance-withdraw_amount

            print( withdraw_amount , "is debited from your account ")

            print("*************************************************")

            print("Your updated balance is : " , balance)

            print("*************************************************")

        if option == 3:
        
            deposit_amount = int(input("Enter your Deposited amount : "))

            print("*************************************************")

            balance = balance+deposit_amount

            print( deposit_amount ,"is credited from your account ")

            print("*************************************************")

            print("Your updated balance is : " , balance)

            print("*************************************************")
            
        if option == 4:
            break
       
else:
    print("Wrong pin please try again !")
