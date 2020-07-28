
import pandas as pd

def correlation_table(portfolio, period):
    '''
    Takes in a portfolio of stocks (Dataframe) and returns a correlation table.

    :param portfolio: Portfolio represented by stocks (tickers)
    :type portfolio: Portfolio
    :return: correlation table of all stocks in the portfolio
    '''
    return portfolio.returns(period).corr()
