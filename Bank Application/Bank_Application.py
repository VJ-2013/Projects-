import time
import random
import re
def bankApplication():
    while True:
        Sender_Detailn=input("Name: ")
        time.sleep(2)
        try:
            print("Phone number with hypens (xxx-xxx-xxxx)")
            Sender_Detailp=str(input("Phone Number:"))
            if not re.fullmatch(r"\d{3}-\d{3}-\d{4}",Sender_Detailp):
                raise ValueError("Phone number must be in PROPER FORMAT!!✖️") 
            Balance=round(random.uniform(2,1000000000000),2)
            print("Hello", Sender_Detailn)
            print("Checking your Balance....")
            time.sleep(2)
            print("Your Balance is $$", Balance, "💵")
            Receiver_Detailn=input("Who would you like to send money to?")
            Receiver_Detailp=str(input(f"What is {Receiver_Detailn}'s phone number: "))
            if not re.fullmatch(r"\d{3}-\d{3}-\d{4}",Receiver_Detailp):
                raise ValueError("Phone number must be in PROPER FORMAT!!✖️")
            TBalance=round(random.uniform(2,1000000000000),2)
            print(Receiver_Detailn,"Has $$",TBalance)
            Transfer=float(input(f"How much money would you like to transfer to {Receiver_Detailn}: "))
            if Transfer<=0:
                raise ValueError("U have to send at LEAST ONE DOLLAR!!!!!💲")
            if Transfer>Balance:
                raise ValueError("You cannot send more money than U havee!!💰")
            time.sleep(2)
            print("Transferring.....")
            time.sleep(3)
            print("Transaction Complete✅")
            Balance=Balance-Transfer
            TBalance=TBalance+Transfer
            Receipt=input("Would U like a receipt?: ").lower()
            if Receipt=="yes":
                print("Your new balance is $",Balance)
                print(Receiver_Detailn,"'s Balance is",TBalance)
            else:
                print("OKKKK HAVE A NICE DAY ")
                break
        except ValueError as e:
            print(e)
       
bankApplication()Label=tk.Label(root,text="Tic Tac Toe", font=("Send Flowers",60))
    
