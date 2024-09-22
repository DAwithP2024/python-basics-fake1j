# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_categories():
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")
    category_input = input("Select a category by number: ")
    if not category_input.isdigit():
        print("Please enter a valid number.")
        return None
    category_index = int(category_input) - 1
    if category_index < 0 or category_index >= len(products):
        print("Invalid category selection.")
        return None
    return category_index


def display_products(products_list):
    for index, (product, price) in enumerate(products_list, start=1):
        print(f"{index}. {product} - ${price}")
        
def display_sorted_products(products_list, sort_order):
    sorted_list = sorted(products_list, key=lambda x: x[1], reverse=(sort_order == "desc"))
    display_products(sorted_list)
    return sorted_list

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    total_cost = 0
    for product, price, quantity in cart:
        cost = price * quantity
        total_cost += cost
        print(f"{product} - ${price} x {quantity} = ${cost}")
    print(f"Total cost: ${total_cost}")
    return total_cost


def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for product, price, quantity in cart:
        print(f"{quantity} x {product} - ${price} = ${price * quantity}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted upon delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" in email 

def main():
    name = input("Enter your name (First Last): ")
    while not validate_name(name):
        print("Invalid name. Please enter your first and last name.")
        name = input("Enter your name (First Last): ")

    email = input("Enter your email: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address.")
        email = input("Enter your email: ")

    display_categories()
    category_count = len(products)
    category_index = int(input("Select a category by number: ")) - 1
    while category_index < 0 or category_index >= category_count:
        print("Invalid selection. Please choose a valid category.")
        category_index = int(input("Select a category by number: ")) - 1

    selected_category = list(products.keys())[category_index]
    products_list = products[selected_category]
    
    cart = []
    while True:
        display_products(products_list)
        print("Options:")
        print("1. Select a product to buy")
        print("2. Sort the products by price")
        print("3. Go back to categories")
        print("4. Finish shopping")
        
        action_choice = int(input("Choose an option: "))
        if action_choice == 1:
            product_choice = int(input("Select a product by number: ")) - 1
            if 0 <= product_choice < len(products_list):
                quantity = input("Enter quantity: ")
                while not quantity.isdigit() or int(quantity) <= 0:
                    print("Invalid quantity. Please enter a number greater than 0.")
                    quantity = input("Enter quantity: ")
                add_to_cart(cart, products_list[product_choice], int(quantity))
            else:
                print("Invalid product selection.")
        
        elif action_choice == 2:
            sort_order = input("Sort ascending (1) or descending (2)? ")
            if sort_order == '1':
                display_sorted_products(products_list, "asc")
            elif sort_order == '2':
                display_sorted_products(products_list, "desc")
            else:
                print("Invalid choice.")
        
        elif action_choice == 3:
            display_categories()
            category_index = int(input("Select a category by number: ")) - 1
            while category_index < 0 or category_index >= category_count:
                print("Invalid selection. Please choose a valid category.")
                category_index = int(input("Select a category by number: ")) - 1
            selected_category = list(products.keys())[category_index]
            products_list = products[selected_category]
        
        elif action_choice == 4:
            if cart:
                total_cost = display_cart(cart)
                address = input("Enter delivery address: ")
                generate_receipt(name, email, cart, total_cost, address)
            else:
                print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
