import tkinter as tk
from tkinter import messagebox, simpledialog 
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
Order={}


def buy_item():
    Order.clear()
    item_code = Entry_item.get()
    qty = Entry_qty.get()

    if not item_code.isdigit() or not qty.isdigit():
        messagebox.showerror("Error", "Enter valid numbers!")
        
    item_code = int(item_code)
    qty = int(qty)

    if item_code in Menu:
        Order[item_code] = qty
        messagebox.showinfo("Success", "Order Added Successfully")
    else:
        messagebox.showerror("Error", "Item not found!")





def update_order():
    item_code = Entry_item.get()
    qty = Entry_qty.get()


    if not item_code.isdigit() or not qty.isdigit():
        messagebox.showerror("Error", "Enter valid numbers!")
        return


    item_code = int(item_code)
    qty = int(qty)


    if item_code in Menu:
        Order[item_code] = qty
        messagebox.showinfo("Success", "Item Added Successfully")
    else:
        messagebox.showerror("Error", "Item not found!")


def add_more():
    item_code = Entry_item.get()
    qty = Entry_qty.get()

    if not item_code.isdigit() or not qty.isdigit():
        messagebox.showerror("Error", "Enter valid numbers!")
        return

    item_code = int(item_code)
    qty = int(qty)


    if item_code in Menu:
        Order[item_code] += qty
        messagebox.showinfo("Success", "Order Added Successfully")
    else:
        Order[item_code]=qty
        messagebox.showerror("Error", "Item not found!")


def update_order():
    item_code = Entry_item.get()
    qty = Entry_qty.get()

    if not item_code.isdigit() or not qty.isdigit():
        messagebox.showerror("Error", "Enter valid numbers!")
        return

    item_code = int(item_code)
    qty = int(qty)


    if item_code in Menu:
        Order[item_code] -= qty
        messagebox.showinfo("Success", "Order Added Successfully")
    else:
        Order[item_code]=qty 
        messagebox.showerror("Error", "Item not found!")

        item_code = Entry_item.get()
        qty = Entry_qty.get()


    if not item_code.isdigit() or not qty.isdigit():
        messagebox.showerror("Error", "Enter valid numbers!")
        return

    item_code = int(item_code)
    qty = int(qty)


    if item_code in Menu:
        Order[item_code] += qty
        messagebox.showinfo("Success", "Order Added Successfully")
    else:
        Order[item_code]=qty
        messagebox.showerror("Error", "Item not found!")


def check_order(): 
    if not Order: 
        messagebox.showinfo("YOU HAVE ADDED NOTHING.. NOTHING.. NOTHING!!!😡")
    else:
        for Item_Code, qty in Order.items():
            messagebox.showinfo(Menu[Item_Code],"*", qty)

def leave_store(): 
    messagebox.showinfo("GOOD BYE!!!! TOO BAD U DIDN'T BUY ANYTHING! UR THE ONE MISSING OUT!")
    root.destroy 

def pay_order():
    Pay=simpledialog.askstring("Would you like to pay?").lower()
    if Pay=="yes":
        TypePay=simpledialog.askstring("Would you like to pay with cash, credit, or debit? : ").lower()
        
        if TypePay=="cash":
            messagebox.simpledialog("Thank U for ordering!")
            messagebox.simpledialog("You can give the money to the barista")
        
        elif TypePay== "Credit":
            CC=simpledialog.askinteger("Enter your credit card number: ")
            if len(CC)!=16:
                messagebox.showerror("Invalid Number!")
            else:
                messagebox.showinfo("Succesfully added to card!✅")
                messagebox.showinfo("Thank U for ordering!")
            
        elif TypePay=="debit":
            DC=simpledialog.askinteger("Enter your debit card number: ")
            if len(DC)!=16:
                messagebox.showerror("Invalid Number")
            else:
                messagebox.showinfo("Succesfully added to card!✅")
                messagebox.showinfo("Thank U for ordering!")
    

root=tk.Tk()
root.title("Mocha Magic Cafe☕")
root.config(bg="#bca7a7")
Menu=tk.Label(root,text="Menu!!🍽️🍴\n \n 101:Cappuccino ; $6, \n \n 102:Espresso ; $6 \n \n  103:Cheese Sandwich ; $8 \n \n  104:Veg Puff  ; $11 \n \n 105:Chocolate Muffin  ;  $7", font=("Berkshire Swash", 15 ), bg="#fef5f5")

Menu.pack() 

frame = tk.Frame(root, bg="#a98d90")
frame.pack(pady=15)

tk.Label(frame, text="Item code: ", font=("Bubblegum Sans", 13)).grid(row=0, column=0)
Entry_item=tk.Entry(frame)
Entry_item.grid(row=0, column=1)


tk.Label(frame, text="Quantity: ", font=("Bubblegum Sans", 13)).grid(row=1, column=0)
Entry_qty=tk.Entry(frame)
Entry_qty.grid(row=1,column=1)

btn_buy = tk.Button(root, text="Buy", width=20,command=buy_item) 
btn_buy.pack(pady=3)

btn_add = tk.Button(root, text="Add More", width=20, command= add_more) 
btn_add.pack(pady=3) 

btn_change = tk.Button(root, text="Change Order", width=20, command="case 3",command=update_order) 
btn_change.pack(pady=3)

# btn_cancel = tk.Button(root, text="Cancel Item", width=20, command="case 4")
# btn_cancel.pack(pady=3)

btn_show = tk.Button(root, text="Show Order", width=20,command="case 5", command=check_order)
btn_show.pack(pady=3)

btn_receipt = tk.Button(root, text="Receipt", width=20, command="case 6", command=pay_order)
btn_receipt.pack(pady=3)

btn_exit = tk.Button(root, text="Exit", width=20, command="case 7 ", command=leave_store) 
btn_exit.pack(pady=3)

#command=exit_app)

root.mainloop() 



