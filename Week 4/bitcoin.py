from bitcoin_config import api_key
import requests
import sys

def main():

    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments provided")
    else:
        try:
            amount = float(sys.argv[1])
        except ValueError:
            sys.exit("Provided argument is not a number")
        else:
            bitcoin_value = make_request()
            total = round(float(amount*bitcoin_value), 4)
            print(f"{total:,}") 

def make_request():
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin", {"apiKey": api_key})
        response.raise_for_status()
    except requests.RequestException:
        print(f"Request failed. Response code: {response.status_code}")
        sys.exit()
    else:
        response = response.json()["data"]["priceUsd"]
        return float(response)

if __name__ == "__main__":
    main()