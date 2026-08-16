import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Only .csv files are supported")

students = []

try:
    with open(sys.argv[1], "r") as before_file:
        initial_students = csv.DictReader(before_file)
        for row in initial_students:
            last_temp, first_temp = row["name"].split(", ")
            house_temp = row["house"]
            students.append({"first": first_temp, "last": last_temp, "house": house_temp })
except FileNotFoundError:
    sys.exit("File not found")
else:
    with open(sys.argv[2], 'w', newline='') as after_file:
        after_students = csv.DictWriter(after_file, fieldnames=["first", "last", "house"])
        after_students.writeheader()
        for row in students:
            after_students.writerow(row)
