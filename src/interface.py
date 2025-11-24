Red = "\033[91m"
Green = "\033[92m"
Yellow = "\033[93m"
Reset = "\033[0m"
Cyan = "\033[96m"

def print_header():
    print(f"\n{Cyan}=== Smart Pantry Tracker ==={Reset}")
    
    
def get_user_input(prompt):
        return input(f"{Yellow}{prompt}{Reset}")
    
def show_message(message, color="green"):
        if color == "red":
            print(f"{Red}{message}{Reset}")
        elif color == "green":
            print(f"{Green}{message}{Reset}")
        else:
            print(message)

def format_row(name, category, status):
     print(f"{name:<20}{category:<15}{status}")

def show_table_header():
     print(f"\n{Yellow}{'Item Name':<20}{'Category':<15}{'Status':<20}{Reset}")
     print("-"*60)

