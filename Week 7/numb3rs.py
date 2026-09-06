from re import search
from sys import exit

def main():
    try:
        print(validate_ipv4(input("IPv4: ")))
    except EOFError:
        exit()

def validate_ipv4(ip):
    if ip_segments := search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
            if (0 <= int(ip_segments.group(1)) <= 255) and (0 <= int(ip_segments.group(2)) <= 255) and (0 <= int(ip_segments.group(3)) <= 255) and (0 <= int(ip_segments.group(4)) <= 255):
                return True
            else:
                return False
    else:
        return False

if __name__ == "__main__":
    main()