from . import stock as st
import pandas as pd

class Portfolio:
    def __init__(self, tickers: list):
        self.tickers = tickers
        

    def portfolioReturns(self, period: string):
        '''
        Creates table of returns based of a list of stock tickers
        :param period: period of returns, i.e. "1d", "1y"
        '''
        returnsDF = [None]

        # för varje ticker i portfolion, så läggs tickerns data till i frames.
        for ticker in self.tickers:
            st = st.Stock(ticker)
            data = st.returns(period)
            # print(data) # ta bort kommentaren här om du vill se hur datan ser ut
            returnsDF.append(data)

        # slå samman tickerdatan (y-axeln, därav axis=1)
        portfolio_returns = pd.concat(returnsDF, axis=1)
        # byter namn på kolumnerna
        portfolio_returns.columns = self.tickers
        return portfolio_returns

    def portfolio_correlation(self):
        '''
        returns a correlation table of the portfolio
        '''
        return self.portfolioReturns.corr()

    