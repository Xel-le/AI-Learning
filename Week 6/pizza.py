import sys
from tabulate import tabulate
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Only .csv files are supported")

try:
    with open(sys.argv[1], "r") as file:
        menu = csv.DictReader(file)
        print(tabulate(menu, headers="keys", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File not found")
