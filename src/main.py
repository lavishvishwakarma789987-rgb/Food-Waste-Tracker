import dates
import storage
import interface

def add_new_product():
    interface.show_message("\n--- Add New Product ---", "green")
    name = interface.get_user_input("Enter Item Name:")
    category = interface.get_user_input("Enter Category:")
    
    valid_date = None
    while not valid_date:
        date_str = interface.get_user_input("Enter Expiry (YYYY-MM-DD):")
        valid_date = dates.parse_date_string(date_str)
        if not valid_date:
            interface.show_message("Error: Use YYYY-MM-DD format.", "red")
            
    storage.save_item(name, category, date_str)
    interface.show_message(f"Success! {name} saved.", "green")

def view_inventory():
    all_items = storage.load_items()
    interface.show_table_header()
    
    for item in all_items:
        name, category, date_str = item
        expiry_obj = dates.parse_date_string(date_str)
        days = dates.calculate_days_remaining(expiry_obj)
        
        status_text = ""
        if days < 0:
            status_text = f"{interface.RED}EXPIRED ({abs(days)} days ago){interface.RESET}"
        elif days <= 3:
            status_text = f"{interface.RED}URGENT ({days} days left){interface.RESET}"
        elif days <= 7:
            status_text = f"{interface.YELLOW}Use Soon ({days} days left){interface.RESET}"
        else:
            status_text = f"{interface.GREEN}Safe ({days} days left){interface.RESET}"
            
        interface.format_row(name, category, status_text)

def start_app():
    storage.initialize_csv()
    
    while True:
        interface.print_header()
        print("1. Add Item")
        print("2. View Pantry")
        print("3. Exit")
        
        choice = interface.get_user_input("Select Option:")
        
        if choice == '1':
            add_new_product()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            interface.show_message("Goodbye!", "green")
            break
        else:
            interface.show_message("Invalid choice.", "red")

if __name__ == "__main__":
    start_app()

