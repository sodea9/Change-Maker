price = 0
deposit = 0
payDue = 0
stock = 0
change = 0
out_of_change = False
price_valid = False

#tracks change to return to user
quarterBack = 0 #Football!
dimeBack = 0
nickelBack = 0 #look at this photograph

#initial stock
nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0

#intro message/stock
print("Welcome to the vending machine change maker program")
print("Change maker initialized.")
print("Stock contains:")
print(f'   {nickels} nickels')
print(f'   {dimes} dimes')
print(f'   {quarters} quarters')
print(f'   {ones} ones')
print(f'   {fives} fives')

#takes first input
price = input("\nEnter the purchase price (xx.xx) or `q' to quit: ")

#main program loop
while (price != 'q'):
    #checks price validity
    while (price_valid == False):
        #first checks if valid float formatting
        try:
            price = float(price)
            #then checks if negative or not divisible by 5
            if ((int(round(price * 100) % 5)) != 0 or price < 0):
                print("Illegal price: Must be a non-negative multiple of 5 cents.")
            else:
                price_valid = True
                continue
        except:
            print("Invalid purchase price. Try again")
        price = input("\nEnter the purchase price (xx.xx) or `q' to quit: ")
    #quits program if q
        if (price == 'q'):
            price_valid = True
    if (price == 'q'):
        continue

    #deposit option menu
    print("\nMenu for deposits:")
    print("  'n' - deposit a nickel")
    print("  'd' - deposit a dime")
    print("  'q' - deposit a quarter")
    print("  'o' - deposit a one dollar bill")
    print("  'f' - deposit a five dollar bill")
    print("  'c' - cancel the purchase\n")

    #converts to int of number of cents
    payDue = int(round(price * 100))

    while (payDue > 0):
        if (payDue // 100 == 0):
            print(f"Payment due: {payDue % 100} cents")
        else:
            print(f'Payment due: {payDue // 100} dollars and {payDue % 100} cents')

        deposit = input("Indicate your deposit: ")
        if (deposit not in ('n', 'd', 'q', 'o', 'f', 'c')):
            print("Illegal selection: ", deposit)
        elif (deposit == 'f'):
            payDue -= 500
            fives += 1
        elif (deposit == 'o'):
            payDue -= 100
            ones += 1
        elif (deposit == 'q'):
            payDue -= 25
            quarters += 1
        elif (deposit == 'd'):
            payDue -= 10
            dimes += 1
        elif (deposit == 'n'):
            payDue -= 5
            nickels += 1
        #assigns change if they underpay
        elif (deposit == 'c'):
            change = int(round(price * 100)) - payDue
            payDue = 0

    #assigns change if they overpay
    if (payDue < 0):
        change = -payDue

    #makes change
    while (change > 0):
        if (change - 25 >= 0 and quarters > 0):
            change -= 25
            quarters -=1
            quarterBack += 1
        elif (change - 10 >= 0 and dimes > 0):
            change -= 10
            dimes -= 1
            dimeBack += 1
        elif (change - 5 >= 0 and nickels > 0):
            change -= 5
            nickels -= 1
            nickelBack += 1
        else:
            out_of_change = True
            break

    print("\nPlease take the change below.")
    if (quarterBack == 0 and dimeBack == 0 and nickelBack == 0):
        print("  No change due")
    else:
        if (quarterBack > 0):
            print("  ", quarterBack, "quarters")
        if (dimeBack > 0):
            print("  ", dimeBack, "dimes")
        if (nickelBack > 0):
            print("  ", nickelBack, "nickels")
    #only prints if machine is out of change
    if (out_of_change):
        print("Machine is out of change.")
        print("See store manager for remaining refund.")
        print(f"Amount due is: {change // 100} dollars and {change % 100} cents")

    #resets change counter variables (and price validity)
    quarterBack = 0
    dimeBack = 0
    nickelBack = 0
    change = 0
    out_of_change = False
    price_valid = False
    
    print("\nStock contains:")
    print(f'   {nickels} nickels')
    print(f'   {dimes} dimes')
    print(f'   {quarters} quarters')
    print(f'   {ones} ones')
    print(f'   {fives} fives')

    price = input("\nEnter the purchase price (xx.xx) or `q' to quit: ")

stock = (500 * fives) + (100 * ones) + (25 * quarters) + (10 * dimes) + (5 * nickels)
if (stock // 100 == 0):
    print(f'\n{stock % 100} cents')
else:
    print(f'\nTotal: {stock // 100} dollars and {stock % 100} cents')