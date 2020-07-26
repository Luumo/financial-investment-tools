import pandas as pd
import yfinance as yf

class Portfolio:
    def __init__(self, tickers: list):
        self.tickers = tickers

        #create list of holdings based on ticker-list
        self.holdings = list(yf.Ticker(ticker) for ticker in self.tickers)
    
    def get_holdings(self):
        '''
        :return: list of holdings
        '''
        return self.holdings

    # TODO: add functionality for start and end-date, instead of period. hint: alternative parameters
    def returns(self, period):
        '''
        Creates dataframe of returns within given period

        :param period: period of returns, i.e. "1d", "1y"
        :return: dataframe of portfolio returns
        :return type: pandas dataframe
        '''
        returnsDF = [None]
        for stock in self.holdings:
            returns = pd.DataFrame(stock.history(period = period), columns=["Close"])
            # returns = pd.DataFrame(stock.history(start=default_start, end=default_end), columns=["Close"])
            returnsDF.append(returns)

        # slå samman tickerdatan (y-axeln, därav axis=1)
        portfolio_returns = pd.concat(returnsDF, axis=1)
        # byter namn på kolumnerna
        portfolio_returns.columns = self.tickers

        portfolio_returns['Total Portfolio'] = portfolio_returns.iloc[:,0:len(self.holdings)].sum(axis=1) / len(self.holdings)
        return portfolio_returns