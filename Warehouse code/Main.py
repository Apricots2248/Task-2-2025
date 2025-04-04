import os
import csv

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_terminal()
    print('-----------------------------')
    print('Welcome to the warehouse')
    print('-----------------------------')
    print('Please enter desired location')
    print('1. Edit Warehouse')
    print('2. Veiw Warehouse')
    print('3. Exit')
    choice = input('(1,2,3): ')
    if choice == '1':
        clear_terminal()
        edit_warehouse()
    elif choice == '2':
        clear_terminal()
        pass
    elif choice == '3':
        clear_terminal()
        print('Bye')
    else:
        clear_terminal()
        print('you have inputed an incorrect value')
        y = input('return or exit (an incorrect input will result in exit) R/E: ').capitalize()
        if y == 'R':
            main()
        else:
            clear_terminal()
            print('Bye')


class product:
    def __init__(self, product_name, sku, price, amt):
        self.product_name = product_name
        self.sku = sku
        self.price = price
        self.amt = amt
    def Return_product(self):
        return f"{self.product_name}, Sku: {self.sku}, Price: {self.price}, Quantity: {self.amt}"

class warehouse:
    def __init__(self, row, column):
        self.row = row
        self.column = column
    
class Location:
    def __init__(self, row, column):
        self.row = row
        self.column = column



def edit_warehouse():
    print('-- In which way will you be editing the warehouse --')
    print('1. Add Item')
    print('2. Remove Item')
    print('3. Edit Item properties')
    print('4. Return to menu')
    x = input('(1,2,3,4): ')
    if x == '1':
        clear_terminal()
        add_item()
    elif x == '2':
        clear_terminal()
        pass
    elif x == '3':
        clear_terminal()
        pass
    elif x == '4':
        main()
    else:
        clear_terminal()
        print('An incorrect value was inputted')
        print('try again')
        print(' ')
        edit_warehouse()

def add_item():
    print('To add products you will need enter the products Name, SKU, Price, Quantity')
    name = (input('Name: '))
    sku = (input('SKU: '))

    while True:
        Unformatted_price = input('Price: ')
        if Unformatted_price.isdigit():
            price = f'${Unformatted_price}'
            break
        else:
            clear_terminal()
            print('ivalid input please try again')
            print('Name: ', (name))
            print('SKU: ',  (sku))

    while True:
        amt = input('Quantity: ')
        if amt.isdigit():
            break
        else:
            clear_terminal()
            print('ivalid input please try again')
            print('Name: ', (name))
            print('SKU: ', (sku))
            print('Price: ', (price))

    print(name, sku, price, amt)




main()