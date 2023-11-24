import csv

csv_path = "./census_income_dataset.csv"
with open(csv_path, 'r') as f:
    reader = csv.reader(f)
    print(type(reader))
