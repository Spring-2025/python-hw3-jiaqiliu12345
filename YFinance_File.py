# -*- coding: utf-8 -*-
"""YFinance_File.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ge_I5uy2Ui2EIA_LedHyBb_YzUqbz1TI
"""

import yfinance as yf
import pandas as pd
import numpy as np

def get_stock_data(symbol):
    """
    Download stock data from Yahoo Finance and extract 'Adj Close' prices.
    Handles MultiIndex issues.
    :param symbol: Stock ticker symbol (e.g., 'GS')
    :return: Pandas Series containing 'Adj Close' or 'Close' prices.
    """
    data = yf.download(symbol, group_by="ticker")
    print("Available columns:", data.columns)  # Debugging output

    if ('Adj Close', symbol) in data.columns:
        return data[('Adj Close', symbol)]
    elif ('Close', symbol) in data.columns:
        print("Warning: 'Adj Close' not found, using 'Close' instead.")
        return data[('Close', symbol)]
    else:
        raise KeyError(f"'Adj Close' column not found for {symbol}. Check API response.")

def YahooData2returns(YahooData):
    """
    Calculate the lagged returns from Yahoo Finance stock data.
    :param YahooData: Pandas DataFrame with stock data containing 'Adj Close'
    :return: Pandas Series of lagged returns
    """
    if 'Adj Close' not in YahooData.columns:
        raise KeyError("'Adj Close' column not found in provided data.")

    returns = YahooData['Adj Close'].pct_change().dropna()
    return returns

if __name__ == "__main__":
    # Example usage
    stock_symbol = 'GS'  # Goldman Sachs ticker symbol
    try:
        prices = get_stock_data(stock_symbol)
        lagged_returns = YahooData2returns(prices.to_frame())

        # Display data
        print("Stock Prices:")
        print(prices.head())
        print("\nLagged Stock Returns:")
        print(lagged_returns.head())

        # Save to CSV for further analysis
        prices.to_csv(f"{stock_symbol}_prices.csv")
        lagged_returns.to_csv(f"{stock_symbol}_lagged_returns.csv")
    except Exception as e:
        print("Error:", e)