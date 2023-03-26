# Burger combos V1 - 22/03/2023
# Stores the menu of combo meals in a dictionary

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

# testing the dict
for combo_id, combo_info in combos.items():
    print(f"\nCombo ID: {combo_id}")
    total_combo_price = 0

    for key in combo_info:
        print(f"{key}: ${combo_info[key]}")
        # Add price to total price
        total_combo_price += combo_info[key]

    print(f"Total: ${round(total_combo_price, 2)}")

