import csv

# Hardcoded stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}


def show_available_stocks():
    print("Available stocks and prices:")
    for stock, price in STOCK_PRICES.items():
        print(f"  {stock}: ${price}")
    print()


def get_portfolio():
    portfolio = {}

    show_available_stocks()
    print("Enter stock name and quantity (type 'done' as stock name to finish).\n")

    while True:
        stock = input("Stock name: ").upper().strip()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("Stock not found in price list. Try again.\n")
            continue

        try:
            quantity = int(input(f"Quantity of {stock}: "))
            if quantity < 0:
                print("Quantity cannot be negative.\n")
                continue
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity
        print(f"Added {quantity} share(s) of {stock}.\n")

    return portfolio


def calculate_total(portfolio):
    total = 0
    print("\n--- Portfolio Summary ---")
    for stock, quantity in portfolio.items():
        price = STOCK_PRICES[stock]
        value = price * quantity
        total += value
        print(f"{stock}: {quantity} share(s) x ${price} = ${value}")
    print(f"Total Investment: ${total}\n")
    return total


def save_to_file(portfolio, total):
    choice = input("Save results to a file? (yes/no): ").lower().strip()

    if choice != "yes":
        return

    file_format = input("Choose format - txt or csv: ").lower().strip()

    if file_format == "csv":
        filename = "portfolio.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, quantity in portfolio.items():
                price = STOCK_PRICES[stock]
                writer.writerow([stock, quantity, price, price * quantity])
            writer.writerow(["", "", "Total", total])
        print(f"Saved to {filename}\n")

    elif file_format == "txt":
        filename = "portfolio.txt"
        with open(filename, "w") as f:
            f.write("Portfolio Summary\n")
            f.write("------------------\n")
            for stock, quantity in portfolio.items():
                price = STOCK_PRICES[stock]
                value = price * quantity
                f.write(f"{stock}: {quantity} share(s) x ${price} = ${value}\n")
            f.write(f"Total Investment: ${total}\n")
        print(f"Saved to {filename}\n")

    else:
        print("Invalid format. Skipping save.\n")


def main():
    print("Welcome to the Stock Portfolio Tracker!\n")
    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    total = calculate_total(portfolio)
    save_to_file(portfolio, total)


if __name__ == "__main__":
    main()
