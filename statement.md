Project Statement: *Smart Pantry Waste Tracker*

1. Problem Definition
Food waste is a global issue that starts in the household. Individuals frequently purchase groceries but lose track of expiry dates, leading to spoilage. There is a need for a digital solution that helps users monitor their food inventory and alerts them before items expire.
2. Objectives
• Develop a modular Python application to track grocery items.
• Implement an alert system based on date calculation.
• Apply "Top-Down Design" by splitting code into functional modules.
• Ensure data persistence using file handling.
3. Proposed Solution
The Smart Pantry Tracker is a Console-Based Application (CLI) that allows users to:
1. Input Data: Log items with names, categories, and expiration dates.
2. Store Data: Save records to a CSV file so data is not lost on exit.
3. Monitor Status: Automatically calculate "Days Remaining" for every item.
4. Receive Alerts: Visually flag items as "URGENT" (Red) or "SAFE" (Green).
4. Features
• Modular Architecture: The code is separated into Logic, Storage, and Interface modules for better maintainability.
• Input Validation: Prevents the system from crashing if incorrect date formats are entered.
• Color-Coded UI: Uses ANSI escape codes to improve user experience in the terminal.
5. Tech Stack
• Language: Python 3
• Libraries: datetime (Time logic), csv (Data storage), os (File system).

