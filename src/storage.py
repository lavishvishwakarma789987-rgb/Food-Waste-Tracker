import csv
import os 
db_file = "pantry.csv"

def initialize_csv():
    if not os.path.exists(db_file):
        with open(db_file, mode='w', newline="") as f:
                   writer = csv.writer(f)
                   writer.writerow(["Name","Catrgory","Expiry Date"])
def save_item(name, category, expiry_date):
    with open(db_file, mode='a',newline='') as f:
        writer = csv.writer(f)
        writer.writerrow([name, category, expiry_date])

def load_items():
     if not os.path.exists(db_file):
          return[]
     
     items = []
     with open(db_file, mode='r') as f:
          reader = csv.reader(f)
          next(reader)
          for row in reader:
               if row:
                    items.append(row)
                    return items