# Food-Waste-Tracker
Vityarthi Project : 
*Smart Pantry Tracker* 🍟

Python tool to track food expiring and reduce household waste, developed module by module.

Food waste is a global issue that starts in the household. Individuals frequently purchase groceries but lose track of expiry dates, leading to spoilage. There is a need for a digital solution that helps users monitor their food inventory and alerts them before items expire.

✨*OBJECTIVE* 

• Develop a modular Python application to track grocery items.

• Implement an alert system based on date calculation.

• Apply "Top-Down Design" by splitting code into functional modules.

• Ensure data persistence using file handling.

📂 Project Structure - 

The project follows a Top-Down modular design:
* src/main.py: Central controller script
* src/dates.py: Handles all date parsing and calculations.
* src/storage.py: Handles reading/writing of the CSV file.
* src/interface.py: handles UI colors and print formatting.

How to Run 🏃🏻‍♂️

* Open your terminal.
* Go to the src directory:
cd src

* Run the application: 
 python main.py

Usage ⛏️

* Add Item: Enter the name, category, and expiry date (YYYY-MM-DD).
* View Pantry: access a color-coded list of your inventory.
* 🟥 Red: Expired or expiring within 3 days.
* 🟨 Yellow. Expiring within 1 week.
* 🟩 Green is good to go.

