# Burger combos V4 - 28/03/2023
# Allows the user to edit existing combos on the menu

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
    global combos
    # Create new combo key
    combo_id = input("\nCreate a new combo ID: ").upper()
    combos[combo_id] = {}
    # Adds 3 items to the new combo key; main, side and drink
    main_item = input(f"\nEnter {combo_id}'s main item: ").title()
    main_price = float(input(f"Enter {main_item}'s price: $"))
    combos[combo_id][main_item] = main_price

    side_item = input(f"\nEnter {combo_id}'s side: ").title()
    side_price = float(input(f"Enter {side_item}'s price: $"))
    combos[combo_id][side_item] = side_price

    drink = input(f"\nEnter {combo_id}'s drink: ").title()
    drink_price = float(input(f"Enter {drink}'s price: $"))
    combos[combo_id][drink] = drink_price


# Edit an existing menu item
def edit_item():
    existing_id = input("\nEnter the ID of the combo you want to edit: ").upper()
    if existing_id in combos:

        # Allows user to edit existing item or keep it the same in a existing combo
        new_main = input(f"\nEnter {existing_id}'s new main item ('x' to keep the same): ").title()
        if new_main != "X":
            new_m_price = float(input(f"Enter {new_main}'s price: $"))
            combos[existing_id][new_main] = new_m_price

        new_side = input(f"\nEnter {existing_id}'s side ('x' to keep the same): ").title()
        if new_side != "X":
            new_s_price = float(input(f"Enter {new_side}'s price: $"))
            combos[existing_id][new_side] = new_s_price

        new_drink = input(f"\nEnter {existing_id}'s drink ('x' to keep the same): ").title()
        if new_drink != "X":
            new_d_price = float(input(f"Enter {new_drink}'s price: $"))
            combos[existing_id][new_drink] = new_d_price
    else:
        print("This combo ID does not exist")


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
