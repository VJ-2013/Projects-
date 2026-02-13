import time
print("Welcome to the Mocha Magic Cafe\n")
time.sleep(1)
Menu={
    101:"Cappuccino ; $6",
    102:"Espresso ; $6",
    103:"Cheese Sandwich ; $8",
    104:"Veg Puff  ; $11",
    105:"Chocolate Muffin  ;  $7",
}
print("       MENU\n101: Cappuccino ; $6\n102: Espresso ; $6\n103: Cheese Sandwich ; $8\n104: Veg Puff  ; $11\n105: Chocolate Muffin  ;  $7")
time.sleep(3)
Order={}
while True:
    print("\nchoose an action")
    print("1 - Buy")
    print("2 - Change Order")
    print("3 - Add More Items ")
    print("4 - Cancel Order")
    print("5 - Show Order")
    print("6 - Receipt")
    print("7 - Order")
    print("8 - Exit\n")
    time.sleep(3)
    ActionStr=input("Please enter your action: ").strip()
    Action=int(ActionStr)
    match Action:
        case 1:
            print("\nPlacing A new Order☕")
            Order.clear()
            Item_Code=int(input("Enter the item code: "))
            time.sleep(1)
            if Item_Code in Menu:
                Quantity=int(input("How Many: "))
                Order[Item_Code]=Quantity
                print("Succesfully added \n", Order)
            else:
                print("OUT OF STOCK🚫\n")
        case 2:
            print("\nUpdate Your Existing order")
            Update_Ques=input("Would You like to change your order? ").lower()
            if Update_Ques=="yes":
                Order.clear()
                Item_Code=int(input("Enter the item code: "))
                if Item_Code in Menu:
                    Quantity=int(input("How Many: "))
                    Order[Item_Code]=Quantity
                    print("Successfully Updated Order!✅")
                else:
                    print("Was not found")
            else:
                print("WHY DID YOU CLICK 2 THEN!!!😡")
        case 3:
            print("\nAdd More Items🛒")
            Add_Question=input("Would You like to add more items: ").lower()
            if Add_Question=="yes":
                Item_Code=int(input("Enter the item code: "))
                if Item_Code in Menu:
                    Quantity=int(input("How Many: "))
                    if Item_Code in Order:
                        Order[Item_Code]+=Quantity
                    else:
                         Order[Item_Code]=Quantity
                    print("Successfully Updated Order!✅")
                else:
                    print("Was not found")
            else:
                print("WHY DID YOU CLICK 3 THEN!!!😡")
        case 4:
            Update_question=int(input("Enter the item code of what you would like to cancel: "))
            if Update_question in Order:
                 Order.pop(Update_question)
                 Item_Code=int(input("Please enter your new item code"))
                 if Item_Code in Menu:
                    Quantity=int(input("How Many?: "))
                    Order[Item_Code]=Quantity
                    print("Succesfully Added", Item_Code, "*", Quantity)
                 else:
                    print("Item OUT OF STOCK")
        case 5:
            print("\nChecking Your Order....")
            time.sleep(1)
            if not Order:
                print("Your current order is empty")
            else:
                for Item_Code,Quantity in Order.items():
                    print(Menu[Item_Code],"*",Quantity)
        case 7:
            print("\nExiting System......")
            break
        case 8:
            OrderAsk=input("Would you like to pay?").lower()
            if OrderAsk=="yes":
                TypePay=input("Would you like to pay with cash, credit, or debit? : ").lower()
                match TypePay:
                    case "cash":
                        print("Thank U for ordering!")
                        print("You can give the money to the barista")
                    case "credit":
                        CC=int(input("Enter your credit card number: "))
                        if len(CC)!=16:
                            print("Invalid Number")
                        else:
                            print("processing transaction.....")
                            time.sleep(1)
                            print("Succesfully added to card!✅")
                            print("Thank U for ordering!")
                    case "debit":
                        DC=int(input("Enter your debit card number: "))
                        if len(DC)!=16:
                            print("Invalid Number")
                        else:
                            print("processing transaction.....")
                            time.sleep(1)
                            print("Succesfully added to card!✅")
                            print("Thank U for ordering!")
        case _:
            print("Bye Bye👋")


