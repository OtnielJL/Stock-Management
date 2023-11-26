import sys

#print menu
def menu():
    print("1.Add stock\n2.Remove stock\n3.Exit")

def printstock(stock):
    for el in stock:
        print(el,stock[el])
#initialize user credentials
username = "Ojay"
password = "Projectlog1"
yes = ["yes","y","yeah","ok"]
no= ["no","n","nah","nope"]
#intial stock
stock = {"Pepsi": 200, "Pringles":150,"Burgers":122,"Pizza": 271}

#requesting username
uname = input("Please insert username\n")

#username validation
while uname != username:
    uname = input("Incorrect username\n")

#initialise password tries to 5
tries = 5
pas = input("Please enter password\n")

#validate password
while pas != password:
    tries -= 1
    pas = input("Incorrect Password.You have"+ str(tries) +"tries left\n")
    #if user runs out of attempts program closes
    if tries == 0:
        pas = input("Password is incorrect you have"+ str(tries)+ "left\n")
        print("Account locked")
        sys.exit()
        
#select menu choce
choice = ""
while choice != "3":
    menu()
    choice = input()
    while choice != "1" and choice != "2" and choice != "3":
        choice = input("Please select a number from the menu\n")
    #adding an item
    if choice == "1":
        printstock(stock)
        item = input ("Please input which item you want to edit\n")
        if item in stock:
            quant =  input("Howmany of item do you want to add\n")
            while not quant.isnumeric() or int(quant) < 0:
                quant = input("Please choose a positive whole number\n")
            quant = int(quant)
            stock[item] += quant
            printstock(stock)
        #add new item
        else:
            addStock = input(item + "not in stock, do you wish to add it\n").lower()
            while not addStock in yes and not addStock in no:
                addStock = input("Please answer yes or no\n").lower()
            if addStock in yes:
                quant =  input("Howmany of item do you want to add\n")
                while not quant.isnumeric() or int(quant) < 0:
                     quant = input("Please choose a positive whole number\n")
                quant = int(quant)
                stock[item] = quant
                printstock(stock)
    #remove item
    elif choice =="2":
        printstock(stock)
        item = input ("Please input which item you want to edit\n")
        while not item in stock:
            item = input("Please only choose available items")
        quant =  input("Howmany of item do you want to remove\n")
        while not quant.isnumeric() or int(quant) < 0 or int(quant) > stock[item]:
            quant = input("Please choose a positive whole number\n")
            quant = int(quant)
            stock[item] -= quant
            printstock(stock)
            

            
        
        
        
