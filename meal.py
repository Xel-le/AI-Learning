def main():
    timeInput = input("What time is it? ").strip().lower()
    if "a.m." in timeInput:
        timeFormat = "12A"
    elif "p.m." in timeInput:
         timeFormat = "12P"
    else:
        timeFormat = "24"

    timeInput = timeInput.rstrip(" apm.")
    timeInput = convert(timeInput, timeFormat)

    if 7 <= timeInput <= 8:
        print("breakfast time")
    elif 12 <= timeInput <= 13:
        print("lunch time")
    elif 18 <= timeInput <= 19:
        print("dinner time")

def convert(time, format):
        whole, decimal = time.split(":", 1)
        decimal = float(decimal) / 60
        time = float(whole) + float(decimal)
        if format == "24":
            return time
        elif format == "12P":
            if 12 <= time <= 13:
                 return time
            elif 1 <= time:
                 return time+12
        elif format == "12A":
            if 12 <= time <= 13:
                 return time-12
            elif 1 <= time:
                 return time
                 
if __name__ == "__main__":
     main()