import yfinance as yf 
import pandas as pd

class Stock:
    def __init__(self, ticker):
        self.ticker = yf.Ticker(ticker)

    def get_close_price(self, period):
        ticker_data = self.ticker.history(period=period)
        data = pd.DataFrame(ticker_data, columns=["Close"])
        return data

    def returns(self, period):
      returns = pd.DataFrame(self.ticker.history(period=period), columns=["Close"])
      return returns.pct_change()