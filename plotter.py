# plotter.py
"""
The plot displays:
- Option prices (call and put) as functions of stock price.
- ITM/OTM regions with shaded areas.
- A vertical line for the current stock price and the strike price.
- Annotations for clarity.
"""
import numpy as np
import matplotlib.pyplot as plt
from blackscholes import black_scholes_call, black_scholes_put

def plot_with_ITM_ATM_OTM(stock_name, stock_price, strike_price, time_to_maturity, risk_free_rate, volatility):
    stock_prices = np.linspace(stock_price * 0.5, stock_price * 1.5, 100)
    call_prices = [black_scholes_call(s, strike_price, time_to_maturity, risk_free_rate, volatility) for s in stock_prices]
    put_prices = [black_scholes_put(s, strike_price, time_to_maturity, risk_free_rate, volatility) for s in stock_prices]

    plt.figure(figsize=(12, 8))
    
    # Plot Call and Put prices
    plt.plot(stock_prices, call_prices, label='Call Option Price', color='green', lw=2)
    plt.plot(stock_prices, put_prices, label='Put Option Price', color='red', lw=2)
    
    # Highlight ITM/ATM/OTM regions
    plt.fill_between(stock_prices, 0, call_prices, where=(stock_prices >= strike_price), color='lightgreen', alpha=0.3, label='ITM (Call)')
    plt.fill_between(stock_prices, 0, put_prices, where=(stock_prices <= strike_price), color='lightcoral', alpha=0.3, label='ITM (Put)')
    plt.fill_between(stock_prices, 0, call_prices, where=(stock_prices < strike_price), color='lightblue', alpha=0.3, label='OTM (Call)')
    plt.fill_between(stock_prices, 0, put_prices, where=(stock_prices > strike_price), color='lightyellow', alpha=0.3, label='OTM (Put)')
    
    plt.axvline(x=strike_price, color='gray', linestyle='--', label='Strike Price (ATM)', lw=2)
    plt.axvline(x=stock_price, color='black', linestyle='--', label=f'Current Stock Price: {stock_price}', lw=2)
    
    # Add labels and titles
    plt.xlabel('Stock Price', fontsize=12)
    plt.ylabel('Option Price', fontsize=12)
    plt.title(f'{stock_name} Option Prices with ITM/ATM/OTM Regions', fontsize=16)
    
    # Adding annotations for clarity
    plt.annotate(f'Strike Price: {strike_price}', xy=(strike_price, 0), xytext=(strike_price + 10, 5),
                 arrowprops=dict(facecolor='black', arrowstyle="->"), fontsize=12)
    plt.annotate(f'Current Stock Price: {stock_price}', xy=(stock_price, 0), xytext=(stock_price + 10, 15),
                 arrowprops=dict(facecolor='black', arrowstyle="->"), fontsize=12)

    # Add grid, legend and improve layout
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(loc='upper left', fontsize=12)
    plt.tight_layout()
    
    # Show the plot
    plt.show()
