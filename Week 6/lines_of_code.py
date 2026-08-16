import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Only .py files are supported")

counter = 0

# Normally I would not use "try" with a loop but since the error we are trying to catch appear right at the start, I consider it fine
try:
    with open(sys.argv[1], "r") as file:
        for line in file:
            # I consider ".lstrip().startswith("#")" to be more effective than "#" and " #" filter in the task
            if not line.lstrip().startswith("#") and not line == "" and not line.isspace():
                counter += 1
except FileNotFoundError:
    sys.exit("File not found")


print(counter)