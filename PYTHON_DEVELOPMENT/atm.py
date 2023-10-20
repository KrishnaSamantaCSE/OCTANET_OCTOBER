name=input("Enter the USER ID:")
pin=int(input("Enter the 4 digit PIN:"))
def ATM(name,pin):
    name1=['Krish2594', 'Sujit8907', 'Jagannanth4309', 'Sovan6879', 'Soam8072']
    pinno=[9768, 4532, 2137, 3589,5123]
    for i in range(0,len(name1)):
        if(name==name1[i] and pin==pinno[i]):
            print("!!!YESSS ATM functionality is unlocked!!!!!!Now you can perform the following operations!!!")
            def Transaction_History():
                transactionall=['Entry 1:\nAccount Holder: Krishna Samanta\nAccount Number: 987654321\nTransaction Date: 2023-10-01\nTransaction Type: Credit (Deposit)\nTransaction Description: Salary Deposit\nTransaction Amount: 3,500.00\nAccount Balance: 5,000.00\nEntry 2:\nAccount Holder: Krishna Samanta\nAccount Number: 987654321\nTransaction Date: 2023-10-05\nTransaction Type: Debit (Withdrawal)\nTransaction Description: Grocery Shopping at Supermart\nTransaction Amount: 75.45\nAccount Balance: 4,924.55','Entry 1:\nAccount Holder: Sujit Mahapatra\nAccount Number: 234567890\nTransaction Date: 2023-10-15\nTransaction Type: Debit (Withdrawal)\nTransaction Description: ATM Withdrawal - ABC Bank\nTransaction Amount: 100.00\nAccount Balance: 1,250.00\nEntry 2:\nAccount Holder: Sujit Mahapatra\nAccount Number: 234567890\nTransaction Date: 2023-10-15\nTransaction Type: Credit (Deposit)\nTransaction Description: Interest Credit\nTransaction Amount: 25.00\nAccount Balance: 1,275.00',
                'Entry 1:\nAccount Holder: Jagannanth Das\nAccount Number: 567890123\nTransaction Date: 2023-10-20\nTransaction Type: Debit (Withdrawal)\nTransaction Description: Restaurant Dinner at La Maison\nTransaction Amount: 85.00\nAccount Balance: 1,190.00\nEntry 2:\nAccount Holder: Jagannanth Das\nAccount Number: 567890123\nTransaction Date: 2023-10-22\nTransaction Type: Credit (Deposit)\nTransaction Description: Transfer from Checking Account\nTransaction Amount: 500.00\nAccount Balance: 1,690.00',
                'Entry 1:\nAccount Holder: Sovan Samanta\nAccount Number: 789012345\nTransaction Date: 2023-10-25\nTransaction Type: Debit (Withdrawal)\nTransaction Description: Internet Bill Payment\nTransaction Amount: 60.00\nAccount Balance: 1,630.00\nEntry 2:\nAccount Holder: Sovan Samanta\nAccount Number: 789012345\nTransaction Date: 2023-10-28\nTransaction Type: Credit (Deposit)\nTransaction Description: Reimbursement Credit\nTransaction Amount: 150.00\nAccount Balance: 1,780.00',
                'Entry 1:\nAccount Holder: Soamprakash Khatua\nAccount Number: 123450987\nTransaction Date: 2023-10-30\nTransaction Type: Debit (Withdrawal)\nTransaction Description: Mobile Phone Bill Payment\nTransaction Amount: 50.00\nAccount Balance: 1,730.00\nEntry 2:\nAccount Holder: Soamprakash Khatua\nAccount Number: 123450987\nTransaction Date: 2023-10-31\nTransaction Type: Credit (Deposit)\nTransaction Description: Investment Dividend\nTransaction Amount: 75.50\nAccount Balance: 1805.50']

                transactioncredited=['Entry 1:\nAccount Holder: Krishna Samanta\nAccount Number: 987654321\nTransaction Date: 2023-10-01\nTransaction Type: Credit (Deposit)\nTransaction Description: Salary Deposit\nTransaction Amount: 3,500.00\nAccount Balance: 5,000.00','Entry 1:\nAccount Holder: Sujit Mahapatra\nAccount Number: 234567890\nTransaction Date: 2023-10-15\nTransaction Type: Credit (Deposit)\nTransaction Description: Interest Credit\nTransaction Amount: 25.00\nAccount Balance: 1,275.00','Entry 1:\nAccount Holder: Jagannanth Das\nAccount Number: 567890123\nTransaction Date: 2023-10-22\nTransaction Type: Credit (Deposit)\nTransaction Description: Transfer from Checking Account\nTransaction Amount: 500.00\nAccount Balance: 1,690.00','Entry 1:\nAccount Holder: Sovan Samanta\nAccount Number: 789012345\nTransaction Date: 2023-10-28\nTransaction Type: Credit (Deposit)\nTransaction Description: Reimbursement Credit\nTransaction Amount: 150.00\nAccount Balance: 1,780.00','Entry 1:\nAccount Holder: Soamprakash Khatua\nAccount Number: 123450987\nTransaction Date: 2023-10-31\nTransaction Type: Credit (Deposit)\nTransaction Description: Investment Dividend\nTransaction Amount: 75.50\nAccount Balance: 1805.50']
                transactiondebited=['Entry 1:\nAccount Holder: Krishna Samanta\nAccount Number: 987654321\nTransaction Date: 2023-10-05\nTransaction Type: Debit (Withdrawal)\nTransaction Description: Grocery Shopping at Supermart\nTransaction Amount: 75.45\nAccount Balance: 4,924.55','Entry 1:\nAccount Holder: Sujit Mahapatra\nAccount Number: 234567890\nTransaction Date: 2023-10-1\nTransaction Type: Debit (Withdrawal)\nTransaction Description: ATM Withdrawal - ABC Bank\nTransaction Amount: 100.00\nAccount Balance: 1,250','Entry 1:\nAccount Holder: Jagannanth Das\nAccount Number: 567890123\nTransaction Date: 2023-10-20\nTransaction Type: Debit (Withdrawal)\nTransaction Description: Restaurant Dinner at La Maison\nTransaction Amount: 85.00\nAccount Balance: 1,190.00','Entry 1:\nAccount Holder: Sovan Samanta\nAccount Number: 789012345\nTransaction Date: 2023-10-25\nTransaction Type: Debit (Withdrawal)\nTransaction Description: Internet Bill Payment\nTransaction Amount: 60.00\nAccount Balance: 1,630.00','Entry 1:\nAccount Holder: Soamprakash Khatua\nAccount Number: 123450987\nTransaction Date: 2023-10-30\nTransaction Type: Debit (Withdrawal)\nTransaction Description: Mobile Phone Bill Payment\nTransaction Amount: 50.00\nAccount Balance: 1,730']
                while(1):
                    ch=int(input("1.All\n2.Credited\n3.Debited\n4.Exit\nEnter your choice for checking transaction history:"))
                    if(ch==1):
                        print("Last 2 Transactions:!!!!!")
                        print(transactionall[i])
                    elif(ch==2):
                        print("Last 1 Transaction:!!!!!")
                        print(transactioncredited[i])
                    elif(ch==3):
                        print("Last 1 Transaction:!!!!!")
                        print(transactiondebited[i])
                    elif(ch==4):
                        exit(0)
                    else:
                        print("!!!OOPS Default Option!!!Choose the Correct Option")
                        Transaction_History()
            balance=[4924.55,1275.00,690.00,1780.00,1805.50]    
            def Deposit():
                amnt_deposit=float(input("Enter the Deposit amount:"))
                balance[i]=balance[i]+amnt_deposit
                print("!!!MONEY DEPOSIT IS SUCCESSFULLY DONE!!!")
                print("Now Closing Balance is:",(balance[i]))
            def Withdraw():
                amnt_withdraw=float(input("Enter the Withdraw amount:"))
                if(amnt_withdraw>balance[i]):
                    print("Account Balance is:",balance[i])
                    print("!!!OOPS YOUR BALANCE IS LOWER THAN THE WITHDRAW AMOUNT!!!")
                    print("If you want to deposit then press 1 otherwise press 2")
                    cho=int(input("1.Deposit\n2.Exit\nEnter your option:"))
                    if(cho==1):
                        Deposit()
                    else:
                        exit(0)
                elif(amnt_withdraw==balance[i]):
                    print("Account Balance is:",balance[i])
                    print("!!!OOPS YOUR ACCOUNT BALANCE SHOULD NOT BE ZERO(0)!!!")
                    print("If you want to deposit then press 1 otherwise press 2")
                    cho=int(input("1.Deposit\n2.Exit\nEnter your option:"))
                    if(cho==1):
                        Deposit()
                    else:
                        exit(0)
                else:
                    print("Account Balance is:",balance[i])
                    print("!!!MONEY WITHDRAWAL IS SUCCESSFULLY DONE!!!")
                    print("!!!YAY MONEY RECEIVED BY YOU!!!")
                    balance[i]=balance[i]-amnt_withdraw
                    print("Now Closing Balance is:",(balance[i]))
            def Transfer():
                transfer_name=input("Enter the transferred account holder name:")
                transfer_amount=float(input("Enter the transferred amount:"))
                if(transfer_amount>balance[i]):
                    print("Account Balance is:",balance[i])
                    print("!!!OOPS YOUR BALANCE IS LOWER THAN THE WITHDRAW AMOUNT!!!")
                    print("If you want to deposit then press 1 otherwise press 2")
                    cho=int(input("1.Deposit\n2.Exit\nEnter your option:"))
                    if(cho==1):
                        Deposit()
                    else:
                        exit(0)
                elif(transfer_amount==balance[i]):
                    print("Account Balance is:",balance[i])
                    print("!!!OOPS YOUR ACCOUNT BALANCE SHOULD NOT BE ZERO(0)!!!")
                    print("If you want to deposit then press 1 otherwise press 2")
                    cho=int(input("1.Deposit\n2.Exit\nEnter your option:"))
                    if(cho==1):
                        Deposit()
                    else:
                        exit(0)
                else:
                    print("Account Balance is:",balance[i])
                    print("!!!MONEY TRANSFER IS SUCCESSFULLY DONE!!!")
                    print("!!!YAY MONEY RECEIVED BY",transfer_name,"!!!")
                    balance[i]=balance[i]-transfer_amount
                    print("Now Closing Balance is:",(balance[i]))
            while(1):
                choose=int(input("1.Transaction History\n2.Withdraw\n3.Deposit\n4.Transfer\n5.Quit\nEnter your operation number:"))
                if(choose==1):
                    Transaction_History()
                elif(choose==2):
                    Withdraw()
                elif(choose==3):
                    Deposit()
                elif(choose==4):
                    Transfer()
                elif(choose==5):
                    exit(0)
                else:
                    print("!!!OOPS Default Option!!!Choose the Correct Option")
                    ATM(name,pin)
            break
    else:
        print("!!!OOPS Authentication Failed!!!")
M=ATM(name,pin)