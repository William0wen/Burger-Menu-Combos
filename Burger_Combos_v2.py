# Burger combos V2 - 23/03/2023
# Create menu interface so the user can choose different options

# Print the full menu, including total prices.
def print_menu():
    print("---------------------------")
    print("******* MENU *******")
    for combo_id, combo_info in combos.items():
        print(f"\nCombo ID: {combo_id}")
        total_combo_price = 0

        for key in combo_info:
            print(f"{key}: ${combo_info[key]}")
            # Add price to total price
            total_combo_price += combo_info[key]

        print(f"Total: ${round(total_combo_price, 2)}")
    print("---------------------------")


# Add a new item to the menu
def add_item():
    print("add_item")


# Edit an existing menu item
def edit_item():
    print("edit_item")


# Delete existing menu item
def delete_item():
    print("del_item")


# List of combos, with nested lists showing individual items
combos = {
    "VALUE":
        {"Beef burger": 5.69,
         "Fries": 1.00,
         "Fizzy drink": 1.00},
    "CHEEZY":
        {"Cheeseburger": 6.69,
         "Fries": 1.00,
         "Fizzy drink": 1.00},
    "SUPER":
        {"Cheeseburger": 6.69,
         "Large fries": 2.00,
         "Smoothie": 2.00}
}
choice = ""

# Main
print_menu()

# Main menu loop
while choice != "Z":
    choice = input("\n\nWhat would you like to do?"
                   "\nAdd menu item (A)"
                   "\nEdit menu item (E)"
                   "\nDelete menu item (D)"
                   "\nPrint menu (P)"
                   "\nExit (Z)"
                   "\n  >>> ").upper()

    if choice == "A":
        add_item()

    elif choice == "E":
        edit_item()

    elif choice == "D":
        delete_item()

    elif choice == "P":
        print_menu()

    elif choice == "Z":
        print("\n*** Thank you for using this program ***")






