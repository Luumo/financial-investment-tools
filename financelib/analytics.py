
import pandas as pd

def correlation_table(portfolio: pd.DataFrame):
    '''
    Takes in a portfolio of stocks (Dataframe) and returns a correlation table.
    '''
    return portfolio.corr()
