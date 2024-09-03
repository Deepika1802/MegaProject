import yfinance as yf
import pandas as pd

# Define the date range
start_date = "2024-01-01"
end_date = "2024-06-30"

# Define the stock tickers for BSE and NSE (full list)
stock_tickers = {
    "BSE": [
        "RELIANCE.BO",   # Reliance Industries
        "TCS.BO",        # Tata Consultancy Services
        "INFY.BO",       # Infosys
        "HDFCBANK.BO",   # HDFC Bank
        "ICICIBANK.BO",  # ICICI Bank
        "HINDUNILVR.BO", # Hindustan Unilever
        "ITC.BO",        # ITC Limited
        "LT.BO",         # Larsen & Toubro
        "SBIN.BO",       # State Bank of India
        "BAJFINANCE.BO", # Bajaj Finance
    ],  
    "NSE": [
        "RELIANCE.NS",   # Reliance Industries
        "TCS.NS",        # Tata Consultancy Services
        "INFY.NS",       # Infosys
        "HDFCBANK.NS",   # HDFC Bank
        "ICICIBANK.NS",  # ICICI Bank
        "HINDUNILVR.NS", # Hindustan Unilever
        "ITC.NS",        # ITC Limited
        "LT.NS",         # Larsen & Toubro
        "SBIN.NS",       # State Bank of India
        "BAJFINANCE.NS", # Bajaj Finance
        "MARUTI.NS",     # Maruti Suzuki
        "BHARTIARTL.NS", # Bharti Airtel
        "AXISBANK.NS",   # Axis Bank
        "KOTAKBANK.NS",  # Kotak Mahindra Bank
        "SUNPHARMA.NS"   # Sun Pharmaceutical
    ]
}

# Function to fetch stock data and return a DataFrame
def fetch_stock_data(ticker):
    # Fetch stock data from yfinance
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    # Add 'No. of Trades' column as a placeholder
    stock_data["No. of Trades"] = None
    return stock_data

# Function to fetch and save data to separate CSV files for BSE and NSE
def save_data_to_csv(exchange):
    combined_data = pd.DataFrame()  # Empty DataFrame to append all stock data

    for ticker in stock_tickers[exchange]:
        stock_data = fetch_stock_data(ticker)
        stock_data["Ticker"] = ticker  # Add ticker symbol to the data
        combined_data = pd.concat([combined_data, stock_data])

    # Save combined data to CSV for each exchange
    combined_data.to_csv(f"{exchange}_stocks_{start_date}_to_{end_date}.csv")
    print(f"Data for {exchange} saved to CSV.")

# Save data for both BSE and NSE into separate CSV files
save_data_to_csv("BSE")
save_data_to_csv("NSE")

print("All stock data has been retrieved and saved to the files.")
