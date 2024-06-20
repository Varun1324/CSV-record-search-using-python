import csv
def search_records(csv_file, inp):
    all_records = []
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if inp.lower() in row['Name'].lower():
                all_records.append(row)
    return all_records

# main
csv_file = 'temp.csv'
inp = input("Enter a name : ")
all_records = search_records(csv_file, inp)
# display 
if all_records:
    print(f"Found {len(all_records)} record(s) matching '{inp}':")
    for i in all_records:
        print(i)
else:
    print(f"No records found matching '{inp}'.")
