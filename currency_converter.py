import requests

def currency_converter():
    # Enter your API Key here
    API_KEY = "YOUR_API_KEY"
    BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"
    
    print("Welcome to the Currency Converter!")
    print("Fetching live exchange rates...")

    try:
        # Input the base currency
        base_currency = input("Enter the base currency (e.g., USD): ").upper()
        response = requests.get(BASE_URL + base_currency)
        data = response.json()

        # Check for valid response
        if data["result"] == "success":
            rates = data["conversion_rates"]
            print(f"Exchange rates for {base_currency} loaded successfully!")
            
            # Input the target currency and amount
            target_currency = input("Enter the target currency (e.g., EUR): ").upper()
            if target_currency not in rates:
                print(f"Currency {target_currency} not found. Please try again.")
                return
            
            amount = float(input(f"Enter the amount in {base_currency}: "))
            converted_amount = amount * rates[target_currency]
            
            # Display the result
            print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        else:
            print("Failed to fetch exchange rates. Please check your API key or base currency.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    currency_converter()
