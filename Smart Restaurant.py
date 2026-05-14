# Smart Restaurant POS System
# Python Console Project

menu = {
    1: {"name": "Burger", "price": 120},
    2: {"name": "Pizza", "price": 200},
    3: {"name": "Pasta", "price": 150},
    4: {"name": "Fries", "price": 60},
    5: {"name": "Cola", "price": 40}
}

cart = []

def show_menu():
    print("\n========== MENU ==========")
    for key, item in menu.items():
        print(f"{key}. {item['name']} - {item['price']} EGP")
    print("==========================")

def add_to_cart():
    show_menu()

    try:
        choice = int(input("Enter item number: "))
        quantity = int(input("Enter quantity: "))

        if choice in menu:
            item = menu[choice]

            total_price = item["price"] * quantity

            cart.append({
                "name": item["name"],
                "quantity": quantity,
                "total": total_price
            })

            print(f"{quantity} x {item['name']} added successfully!")

        else:
            print("Invalid item number!")

    except:
        print("Invalid input!")

def show_bill():
    print("\n========== BILL ==========")

    grand_total = 0

    if len(cart) == 0:
        print("Cart is empty!")
        return

    for item in cart:
        print(f"{item['name']} x {item['quantity']} = {item['total']} EGP")
        grand_total += item["total"]

    tax = grand_total * 0.14
    final_total = grand_total + tax

    print("--------------------------")
    print(f"Subtotal : {grand_total} EGP")
    print(f"Tax 14%  : {tax:.2f} EGP")
    print(f"Total    : {final_total:.2f} EGP")
    print("==========================")

def main():
    while True:
        print("\n===== SMART RESTAURANT POS =====")
        print("1. Show Menu")
        print("2. Add Order")
        print("3. Show Bill")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            show_menu()

        elif choice == "2":
            add_to_cart()

        elif choice == "3":
            show_bill()

        elif choice == "4":
            print("System Closed.")
            break

        else:
            print("Invalid choice!")

main()