import csv

with open('/shared_data/raw.csv', 'r') as infile, open('/shared_data/clean.csv', 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=["name", "age"])
    writer.writeheader()
    for row in reader:
        row["name"] = row["name"].upper()
        writer.writerow(row)

print("Data Transformed!")
