import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

import financelib.stock as stl

portfolio_list = ["AMZN", # Amazon
                  "GOOG", # Alphapet C
                  "ABB", # ABB
                  "ARISE.ST", # Arise
                  "ATRLJ-B.ST", # Atrium Ljungberg
                  "AXFO.ST" # Axfood
                  ] 


# nu när vi har en df för hela portföljen, då vill vi ha en correlation table för allt. 
# https://datascienceplus.com/visualize-correlation-matrices-in-python/
def correlation_table(result):
  result_corr = result.corr()

  snygg_corr = result_corr.reset_index(drop=True).style.background_gradient(cmap='viridis').set_precision(2)
  return snygg_corr

def merge_portfolio(portfolio: list):
    frames = [None]

    # för varje ticker i portfolion, så läggs tickerns data till i frames.
    for ticker in portfolio:
        st = stl.Stock(ticker)
        data = st.returns("1y")
        # print(data) # ta bort kommentaren här om du vill se hur datan ser ut
        frames.append(data)

    merged_portfolio = pd.concat(frames, axis=1)  # slå samman tickerdatan (y-axeln, därav axis=1)
    merged_portfolio.columns = portfolio_list     # byter namn på kolumnerna
    return merged_portfolio


merged_portfolio = merge_portfolio(portfolio_list)
# print(merged_portfolio)
# merged_portfolio.plot()
# plt.legend(portfolio_list)
corr = correlation_table(merged_portfolio)
fig, ax = plt.subplots()


ax.table(cellText=merged_portfolio.values, colLabels=merged_portfolio.columns, loc='center')

fig.tight_layout()

plt.show()


# ax.table(merged_portfolio)
# pd.plotting.table(corr)
plt.show()