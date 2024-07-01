from yahoo_fin import stock_info
from tkinter import *


def stock_price():
    try:
        price = stock_info.get_live_price(e1.get())
        Current_stock.set(f"${price:.2f}")
    except Exception as e:
        Current_stock.set(f"Error: {e}")


def create_gui():
    master = Tk()
    master.title("Stock Price Checker")

    Label(master, text="Company Symbol:").grid(row=0, sticky=W)
    Label(master, text="Stock Result:").grid(row=3, sticky=W)

    e1.grid(row=0, column=1)
    result2.grid(row=3, column=1, sticky=W)
    b.grid(row=0, column=2, padx=5, pady=5)

    mainloop()


if __name__ == "__main__":
    master = Tk()
    Current_stock = StringVar(master)
    e1 = Entry(master)
    result2 = Label(master, text="", textvariable=Current_stock)
    b = Button(master, text="Show", command=stock_price)

    master.withdraw()  # Hide the root window until everything is set up
    create_gui()
    master.deiconify()  # Show the root window after setup

# import yfinance as yf
#
# # Define a list of top Indian company symbols (replace with your preferred ones)
# company_symbols = ["RELIANCE.NS", "HDFC.NS", "ITC.NS", "INFY.NS", "TCS.NS"]


# Get current stock data for each company
# def get_stock_data(symbol):
#     try:
#         stock_data = yf.download(symbol, period="1d")  # Download data for 1 day
#         current_price = stock_data["Close"][0]
#         return f"{symbol}: {current_price:.2f}"
#     except (yf.DownloadError, KeyError):
#         return f"Error retrieving data for {symbol}"
#
#
# # Get current Sensex and Nifty data (replace URLs if needed)
# def get_market_status():
#     try:
#         sensex_url = "https://finance.yahoo.com/quote/%5ENSEI?p=%5ENSEI"
#         nifty_url = "https://finance.yahoo.com/quote/%5E^NSEI?p=%5E^NSEI"
#         sensex_data = yf.download(sensex_url, period="1d")
#         nifty_data = yf.download(nifty_url, period="1d")
#         current_sensex = sensex_data["Close"][0]
#         change_sensex = sensex_data["Change"][0]
#         current_nifty = nifty_data["Close"][0]
#         change_nifty = nifty_data["Change"][0]
#         change_symbol = "+" if change_sensex > 0 else ""
#         change_symbol_nifty = "+" if change_nifty > 0 else ""
#         return (f"Sensex: {current_sensex:.2f} ({change_symbol}{change_sensex:.2f})\n"
#                 f"Nifty: {current_nifty:.2f} ({change_symbol_nifty}{change_nifty:.2f})")
#     except (yf.DownloadError, KeyError):
#         return "Error retrieving market data"
#
#
# # Print market status
# print(get_market_status())

# Print stock prices
# for symbol in company_symbols:
#     print(get_stock_data(symbol))

# import requests
#
#
# def get_market_status():
#     url = "https://financialmodelingprep.com/api/v3/majors-indexes"
#     response = requests.get(url)
#     data = response.json()
#     if 'Error Message' in data:
#         return "Failed to retrieve market status."
#     else:
#         sensex_data = None
#         nifty_data = None
#         for index_data in data:
#             if index_data['ticker'] == '^BSESN':  # Sensex
#                 sensex_data = index_data
#             elif index_data['ticker'] == '^NSEI':  # Nifty
#                 nifty_data = index_data
#
#         if sensex_data and nifty_data:
#             sensex_status = "Up" if sensex_data['changesPercentage'] >= 0 else "Down"
#             nifty_status = "Up" if nifty_data['changesPercentage'] >= 0 else "Down"
#             return f"Sensex: {sensex_data['price']} ({sensex_status}), Nifty: {nifty_data['price']} ({nifty_status})"
#         else:
#             return "Market data not found."
#
#
# def get_stock_prices():
#     top_companies = ['RELIANCE', 'TCS', 'HDFCBANK', 'HDFC', 'INFY']  # Reliance, TCS, HDFC Bank, HDFC, Infosys
#     prices = []
#
#     for symbol in top_companies:
#         url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}"
#         response = requests.get(url)
#         data = response.json()
#         if 'Error Message' in data:
#             print(f"Failed to retrieve data for {symbol}.")
#         elif data:
#             prices.append(f"{data[0]['symbol']}: {data[0]['price']}")
#         else:
#             print(f"No data found for {symbol}.")
#
#     return prices
#
#
# def main():
#     print("Welcome to the Market Status Checker!")
#     print("Fetching market status...")
#     status = get_market_status()
#     print("Market Status:", status)
#     print("Fetching stock prices...")
#     prices = get_stock_prices()
#     print("Stock Prices:")
#     for price in prices:
#         print(price)
#
#
# if __name__ == "__main__":
#     main()
