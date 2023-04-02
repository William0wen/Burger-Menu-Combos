# Burger combos V6 final version - 3/04/2023
# Converts the whole program to be read through the easygui interface.

import easygui


# Print the full menu, including total prices.
def print_menu():
    menu_display = "---------------------------"

    for combo_id, combo_info in combos.items():
        menu_display += f"\n\nCombo ID: {combo_id}"
        total_combo_price = 0

        for key in combo_info:
            menu_display += f"\n{key}: ${combo_info[key]}"
            # Add price to total price
            total_combo_price += combo_info[key]

        menu_display += f"\nTotal: ${round(total_combo_price, 2)}"
    menu_display += "\n---------------------------"
    easygui.msgbox(menu_display, "******* MENU *******")


# Add a new item to the menu
def add_item():
    global combos
    # Create new combo key
    combo_id = easygui.enterbox("\nCreate a new combo ID").upper()
    combos[combo_id] = {}
    # Adds 3 items to the new combo key; main, side and drink
    main_item = easygui.enterbox(f"\nEnter {combo_id}'s main item: ").title()
    main_price = easygui.integerbox(f"Enter {main_item}'s price: $")
    combos[combo_id][main_item] = main_price

    side_item = easygui.enterbox(f"\nEnter {combo_id}'s side: ").title()
    side_price = easygui.integerbox(f"Enter {side_item}'s price: $")
    combos[combo_id][side_item] = side_price

    drink = easygui.enterbox(f"\nEnter {combo_id}'s drink: ").title()
    drink_price = easygui.integerbox(f"Enter {drink}'s price: $")
    combos[combo_id][drink] = drink_price


# Edit an existing menu item
def edit_item():
    existing_id = easygui.enterbox("\nEnter the ID of the combo you want to edit: ").upper()
    if existing_id in combos:

        # Allows user to edit existing item or keep it the same in an existing combo
        new_main = easygui.enterbox(f"\nEnter {existing_id}'s new main item ('X' to keep the same): ").title()
        if new_main != "X":
            new_m_price = easygui.integerbox(f"Enter {new_main}'s price: $")
            combos[existing_id][new_main] = new_m_price

        new_side = easygui.enterbox(f"\nEnter {existing_id}'s side ('X' to keep the same): ").title()
        if new_side != "X":
            new_s_price = easygui.integerbox(f"Enter {new_side}'s price: $")
            combos[existing_id][new_side] = new_s_price

        new_drink = easygui.enterbox(f"\nEnter {existing_id}'s drink ('X' to keep the same): ").title()
        if new_drink != "X":
            new_d_price = easygui.integerbox(f"Enter {new_drink}'s price: $")
            combos[existing_id][new_drink] = new_d_price
    else:
        easygui.msgbox("This combo ID does not exist")


# Delete existing menu item
def delete_combo():
    delete_id = easygui.enterbox("\nEnter the ID of the combo you want to delete: ").upper()

    if delete_id in combos:
        # Pops the entire combo from the list
        combos.pop(delete_id)
        easygui.msgbox(f"{delete_id} was successfully removed from the menu.")

    else:
        easygui.msgbox("This combo ID does not exist")


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
    choice = easygui.buttonbox("\n\nWhat would you like to do?",
                               "Control Centre", choices=["Add menu item", "Edit menu item", "Delete combo",
                                                          "Print menu", "Exit"])

    if choice == "Add menu item":
        add_item()

    elif choice == "Edit menu item":
        edit_item()

    elif choice == "Delete combo":
        delete_combo()

    elif choice == "Print menu":
        print_menu()

    elif choice == "Exit":
        easygui.msgbox("\n*** Thank you for using this program ***")
        exit()
