import os
import csv

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def Return():
    x = input('do you wish to return to the main program or end program R/E: ').capitalize()
    if x == 'R':
        main()
    else:
        clear_terminal()
        print('invalid input')
        Return()

WAREHOUSE_ROWS = 6
WAREHOUSE_COLS = 6

def initialize_warehouse():
    return [[None for _ in range(WAREHOUSE_COLS)] for _ in range(WAREHOUSE_ROWS)]

def save_grid_to_csv(grid):
    with open('warehouse_grid.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for r in range(WAREHOUSE_ROWS):
            for c in range(WAREHOUSE_COLS):
                product = grid[r][c]
                if product is not None:
                    writer.writerow([r, c] + product.to_csv_row())

def load_grid_from_csv():
    grid = initialize_warehouse()
    if os.path.exists('warehouse_grid.csv'):
        with open('warehouse_grid.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 6:
                    r = int(row[0])
                    c = int(row[1])
                    product = Product(row[2], row[3], row[4], row[5], r, c)
                    grid[r][c] = product
                else:
                    print(f"⚠️ Skipping invalid row: {row}")
    return grid

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
        view_warehouse()
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


class Product:
    def __init__(self, product_name, sku, price, amt, row=None, col=None):
        self.product_name = product_name
        self.sku = sku
        self.price = price
        self.amt = amt
        self.row = row
        self.col = col

    def to_csv_row(self):
        return [self.product_name, self.sku, self.price, self.amt, self.row, self.col]

    @staticmethod
    def from_csv_row(row):
        return Product(row[0], row[1], row[2], row[3], row[4], row[5])

    def return_product(self):
        return f"{self.product_name}, Sku: {self.sku}, Price: {self.price}, Quantity: {self.amt}, Location: ({self.row}, {self.col})"


class warehouse:
    def __init__(self, row, column):
        self.row = row
        self.column = column
    
class Location:
    def __init__(self, row, column):
        self.row = row
        self.column = column

def load_products():
    products = []
    if os.path.exists('warehouse_data.csv'):
        with open('warehouse_data.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    products.append(Product.from_csv_row(row))
    return products

def save_products(products):
    with open('warehouse_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for product in products:
            writer.writerow(product.to_csv_row())

def view_warehouse_():
    grid = load_grid_from_csv()
    for row in grid:
        for product in row:
            if product is None:
                print("Empty", end=" | ")
            else:
                print(f"{product.product_name}", end=" | ")
        print()

def view_warehouse():
    view_warehouse_()
    print('---')
    choice = input('do you wish to view a specific items details Y/N: ').capitalize()
    if choice == 'Y':
        view_item()
    elif choice == 'N':
        Return()
    else:
        clear_terminal()
        print('----')
        print('invalid input')
        print('----')
        view_warehouse()

def view_item():
    clear_terminal()
    grid = load_grid_from_csv()  
    print("--- Current Warehouse ---")
    view_warehouse_()

    while True:
        try:
            row = int(input("Enter the row (0-5) of the product to view details: "))
            col = int(input("Enter the column (0-5) of the product to view details: "))
            if not (0 <= row < WAREHOUSE_ROWS and 0 <= col < WAREHOUSE_COLS):
                print("Invalid row or column. Please enter values between 0 and 5.")
                continue
            product = grid[row][col]
            if product is None:
                print("There is no product at that location.")
            else:
                clear_terminal()
                print("\n--- Product Details ---")
                print(f"Name: {product.product_name}")
                print(f"SKU: {product.sku}")
                print(f"Price: {product.price}")
                print(f"Quantity: {product.amt}")
                break
        except ValueError:
            print("Invalid input. Please enter valid row and column numbers.")
    Return()


def edit_warehouse():
    grid = load_grid_from_csv()
    print('-- In which way will you be editing the warehouse --')
    print('1. Add Item')
    print('2. Remove Item')
    print('3. Edit Item properties')
    print('4. Return to menu')
    x = input('(1,2,3,4): ')
    if x == '1':
        clear_terminal()
        add_item(grid)
        save_grid_to_csv(grid)
    elif x == '2':
        clear_terminal()
        remove_item()
    elif x == '3':
        clear_terminal()
        edit_item()
    elif x == '4':
        main()
    else:
        clear_terminal()
        print('An incorrect value was inputted')
        print('try again')
        print(' ')
        edit_warehouse()

def add_item(grid):
    print('To add products you will need to enter the product\'s Name, SKU, Price, Quantity')
    name = input('Name: ')
    sku = input('SKU: ')

    while True:
        Unformatted_price = input('Price: ')
        if Unformatted_price.isdigit():
            price = f'${Unformatted_price}'
            break
        else:
            clear_terminal()
            print('Invalid input, please try again.')

    while True:
        amt = input('Quantity: ')
        if amt.isdigit():
            if int(amt) <= 25:
                break
            else:
                clear_terminal()
                print('Please enter a number less than or equal to 25.')
        else:
            clear_terminal()
            print('Invalid input, please enter a number.')

    while True:
        try:
            row = int(input('Row (0-5): '))
            col = int(input('Column (0-5): '))
            if not (0 <= row < WAREHOUSE_ROWS and 0 <= col < WAREHOUSE_COLS):
                print('Row and column must be between 0 and 5.')
                continue
            if grid[row][col] is not None:
                print('That spot is taken. Choose another.')
            else:
                break
        except ValueError:
            print('Enter valid numbers.')
        except IndexError:
            print('Index out of range, please provide valid row and column between 0 and 5.')

    product = Product(name, sku, price, amt, row, col)
    grid[row][col] = product

    save_grid_to_csv(grid)

    clear_terminal()
    print('---new warehouse---')
    view_warehouse_()
    Return()

def remove_item():
    grid = load_grid_from_csv()  
    print("--- Current Warehouse ---")
    view_warehouse_()  

    while True:
        try:
            row = int(input("Enter the row (0-5) of the item to remove: "))
            col = int(input("Enter the column (0-5) of the item to remove: "))
            if not (0 <= row < WAREHOUSE_ROWS and 0 <= col < WAREHOUSE_COLS):
                print("Invalid row or column. Please enter values between 0 and 5.")
                continue
            if grid[row][col] is None:
                print("There is no product in that location.")
            else:
                print(f"Removing item: {grid[row][col].return_product()}")
                grid[row][col] = None
                save_grid_to_csv(grid) 
                clear_terminal()
                print("Item removed successfully.")
                break
        except ValueError:
            print("Invalid input. Please enter valid row and column numbers.")
    Return()


def edit_item():
    grid = load_grid_from_csv()  
    print("--- Current Warehouse ---")
    view_warehouse_()  

   
    while True:
        try:
            row = int(input("Enter the row (0-5) of the item to edit: "))
            col = int(input("Enter the column (0-5) of the item to edit: "))
            if not (0 <= row < WAREHOUSE_ROWS and 0 <= col < WAREHOUSE_COLS):
                print("Invalid row or column. Please enter values between 0 and 5.")
                continue
            product = grid[row][col]
            if product is None:
                print("There is no product at that location.")
            else:
                clear_terminal()
                print(f"Editing product: {product.return_product()}")

                new_name = input(f"New Name (current: {product.product_name}): ") or product.product_name
                new_price = input(f"New Price (current: {product.price}): ") or product.price
                while True:
                    new_amt = input(f"New Quantity (current: {product.amt}): ")
                    if new_amt == "":
                        new_amt = product.amt
                        break
                    elif new_amt.isdigit() and int(new_amt) <= 25:
                        new_amt = int(new_amt)
                        break
                    else:
                        print("Invalid quantity. Please enter a number up to 25.")

                product.product_name = new_name
                product.price = new_price
                product.amt = new_amt

                save_grid_to_csv(grid)
                clear_terminal()
                print("Product updated successfully.")
                break
        except ValueError:
            print("Invalid input. Please enter valid row and column numbers.")
    Return()


main()