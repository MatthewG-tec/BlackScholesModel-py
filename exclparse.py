# exclparse.py
"""
Function for parsing through excel "Database"
    - Each cell is extrated according to specified parameters below
"""
import pandas as pd

def get_black_scholes_params(sheet_df):
    # First row contains the necessary values
    stock_name = sheet_df.iloc[0, 0]         # Column 1 for stock name
    stock_price = sheet_df.iloc[0, 1]        # Column 2 for stock price
    strike_price = sheet_df.iloc[0, 2]       # Column 3 for strike price
    risk_free_rate = sheet_df.iloc[0, 3]     # Column 4 for risk-free rate
    time_to_maturity = sheet_df.iloc[0, 4]   # Column 5 for time to maturity
    volatility = sheet_df.iloc[0, 5]         # Column 6 for volatility
    call_market_price = sheet_df.iloc[0, 6]  # Column 7 for call option market price
    put_market_price = sheet_df.iloc[0, 7]   # Column 8 for put option market price
    return stock_name, stock_price, strike_price, risk_free_rate, time_to_maturity, volatility, call_market_price, put_market_price

def process_sheets(sheet_names, excel_file):
    data = {}
    
    for sheet in sheet_names:
        df = pd.read_excel(excel_file, sheet_name=sheet)
        
        # Get stock name and Black-Scholes parameters
        black_scholes_params = get_black_scholes_params(df)
        
        # Store the extracted data
        data[sheet] = {
            'Stock Name': black_scholes_params[0],  # Store stock name
            'Black-Scholes Params': black_scholes_params[1:]  # Store remaining params
        }
    
    return data
