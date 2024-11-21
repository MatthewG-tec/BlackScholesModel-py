# main.py
import pandas as pd
import sys
import unittest
from plotter import plot_with_ITM_ATM_OTM
from exclparse import process_sheets
from blackscholes import black_scholes_call, black_scholes_put, black_scholes_call_div, black_scholes_put_div
from BlackScholesTest import TestBlackScholes

def get_input_choice():
    print("----------------------------------------------------------------------")
    print("Please choose: ")
    print("1. Enter the values manually")
    print("2. Use values from an Excel file")
    choice = input("Enter your choice (1 or 2): ")
    return choice

def get_manual_inputs():
    stock_name = str(input("Enter stock name: "))
    stock_price = float(input("Enter stock price (S): "))
    strike_price = float(input("Enter strike price (K): "))
    risk_free_rate = float(input("Enter risk-free rate (r): "))
    time_to_maturity = float(input("Enter time to maturity (T) in years: "))
    volatility = float(input("Enter volatility (sigma): "))
    dividend_yield = float(input("Enter dividend yield (q) as a decimal (e.g., 0.02 for 2%) or 0 if none: "))
    call_market_price = float(input("Enter market price for Call Option: "))
    put_market_price = float(input("Enter market price for Put Option: "))
    
    return (stock_name, stock_price, strike_price, risk_free_rate, time_to_maturity, volatility, dividend_yield, call_market_price, put_market_price)

def get_excel_inputs():
    excel_file = 'BlackScholesData.xlsx'
    xls = pd.ExcelFile(excel_file)
    sheet_names = xls.sheet_names
    sheet_data = process_sheets(sheet_names, excel_file)
    
    inputs = []
    for sheet_name, data in sheet_data.items():
        stock_name = data['Stock Name']
        black_scholes_params = data['Black-Scholes Params']
        
        # Ensure the Black-Scholes parameters are valid
        if None in black_scholes_params:
            print(f"Skipping invalid data for {stock_name}")
            continue
        
        # Manually ask for dividend yield input (get it from user input)
        dividend_yield = float(input(f"Enter dividend yield for {stock_name} as a decimal (e.g., 0.02 for 2%) or 0 if none: "))
        
        # Add the dividend yield to the tuple of values
        inputs.append((stock_name, *black_scholes_params, dividend_yield))  # Now contains 9 values
    
    return inputs if inputs else None

def check_valuation(option_type, calculated_price, market_price):
    threshold = 0.05
    
    if abs(calculated_price - market_price) / market_price > threshold:
        if calculated_price > market_price:
            print(f"The {option_type} option is overvalued by {((calculated_price - market_price) / market_price) * 100:.2f}%")
        else:
            print(f"The {option_type} option is undervalued by {((market_price - calculated_price) / market_price) * 100:.2f}%")
    else:
        print(f"The {option_type} option is fairly valued (within {threshold*100}% of the market price).")

if __name__ == '__main__':
    print("Running tests before main execution...")

    suite = unittest.TestLoader().loadTestsFromTestCase(TestBlackScholes)
    result = unittest.TextTestRunner().run(suite)

    if not result.wasSuccessful():
        print("\nTests failed. Terminating program.")
        sys.exit()

    choice = get_input_choice()
    if choice == '1':
        input_data = [get_manual_inputs()]
    elif choice == '2':
        input_data = get_excel_inputs()
    else:
        print("Invalid choice. Terminating program.")
        sys.exit()

    if input_data:
        for stock_name, stock_price, strike_price, risk_free_rate, time_to_maturity, volatility, call_market_price, put_market_price, dividend_yield in input_data:
            # Calculate prices based on the dividend yield
            if dividend_yield > 0:
                call_price = black_scholes_call_div(stock_price, strike_price, time_to_maturity, risk_free_rate, dividend_yield, volatility)
                put_price = black_scholes_put_div(stock_price, strike_price, time_to_maturity, risk_free_rate, dividend_yield, volatility)
            else:
                call_price = black_scholes_call(stock_price, strike_price, time_to_maturity, risk_free_rate, volatility)
                put_price = black_scholes_put(stock_price, strike_price, time_to_maturity, risk_free_rate, volatility)
            
            # Print results
            print("\nStock Ticker:", stock_name)
            print("Call Option Price:", call_price)
            print("Put Option Price:", put_price)
            
            check_valuation("Call", call_price, call_market_price)
            check_valuation("Put", put_price, put_market_price)
            
            plot_with_ITM_ATM_OTM(stock_name, stock_price, strike_price, time_to_maturity, risk_free_rate, volatility)