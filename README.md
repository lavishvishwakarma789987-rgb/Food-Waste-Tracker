# Food-Waste-Tracker
Vityarthi Project
*Smart Pantry Tracker* 🍟

Python tool to track food expiring and reduce household waste, developed module by module.

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

