def main():
    timeInput = input("What time is it? ").strip().lower()
    if "a.m." in timeInput:
        timeFormat = "12A"
    elif "p.m." in timeInput:
         timeFormat = "12P"
    else:
        timeFormat = "24"

    timeInput = timeInput.rstrip(" apm.")
    timeInput = convert(timeInput)

    print(timeInput)
    print(timeFormat)

    if timeFormat == "24":
        if 7 <= timeInput <= 8:
             print("breakfast time")
        elif 12 <= timeInput <= 13:
             print("lunch time")
        elif 18 <= timeInput <= 19:
             print("dinner time")
    elif timeFormat == "12A" or timeFormat == "12P":
        if 7 <= timeInput <= 8 and timeFormat == "12A":
             print("breakfast time")
        elif (0 <= timeInput <= 1 or 12 <= timeInput < 13) and timeFormat == "12P":
             print("lunch time")
        elif 6 <= timeInput <= 7 and timeFormat == "12P":
             print("dinner time")

def convert(time):
        whole, decimal = time.split(":", 1)
        decimal = float(decimal) / 60
        time = float(whole) + float(decimal)
        return time

main()