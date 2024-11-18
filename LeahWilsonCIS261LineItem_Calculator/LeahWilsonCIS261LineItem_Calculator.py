##Code tweaked a little to make it exit only after user states they dont want to enter another line.
import os

# Function to display the heading
def display_heading():
    print("\n===== The Invoice Line Item Calculator =====")

# Function to prompt for a valid price
def get_price():
    while True:
        try:
            price = float(input("Enter the price: "))
            if price < 0:
                print("Price cannot be negative. Please enter a valid price.")
            else:
                return price
        except ValueError:
            print("Invalid input. Please enter a valid number for the price.")

# Function to prompt for a valid quantity
def get_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please enter a valid quantity.")
            else:
                return quantity
        except ValueError:
            print("Invalid input. Please enter a valid integer for the quantity.")

# Function to calculate and display the total
def calculate_total(price, quantity):
    total = price * quantity
    print(f"\nPRICE:    ${price:.2f}")
    print(f"QUANTITY: {quantity}")
    print(f"TOTAL:    ${total:.2f}\n")
    
# Function to prompt the user to press any key to continue
def press_any_key_to_continue():
    input("Press any key to continue...")    

# Main function to handle the invoice line item logic
def invoice_line_item_calculator():
    display_heading()

while True:
    display_heading()
    price = get_price()  # Get a valid price
    quantity = get_quantity()  # Get a valid quantity
    calculate_total(price, quantity)  # Calculate and display the total

    # Prompt the user to press any key to continue
    ##press_any_key_to_continue()

    # Prompt the user to enter another line item
    another_item = input("Do you want to enter another line item? (Y/n): ").lower()
    if another_item == 'n':
        print("\nBye!")
        break
    elif another_item == 'Y':
        price = get_price()
        quantity = get_quantity
        calculate_total(price, quantity)
    else:
        press_any_key_to_continue()       
    

# Run the invoice line item calculator
invoice_line_item_calculator()
