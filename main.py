import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import stocklib as stl

portfolio_list = ["AMZN", # Amazon
                  "GOOG", # Alphapet C
                  "ABB", # ABB
                  "ARISE.ST", # Arise
                  "ATRLJ-B.ST", # Atrium Ljungberg
                  "AXFO.ST", # Axfood
                  "CLAS-B.ST", # Clas Ohlson B
                  "CLA-B.ST", # Cloetta B
                  "EOLU-B.ST", # Elous Vind B
                  "INVE-B.ST", # Investor B
                  "KINV-B.ST", # Kinnevik B 
                  "MC", # LVMH Moet Louise Vuitton
                  "NIBE-B.ST", # NIBE B
                  "SHOP", # Shopify
                  "SPOT", # Spotify SA (US)
                  "TEL2-B.ST", # Tele2 B
                  "TSLA", # Tesla
                  "VMW", # VMware
                  "VOLV-B.ST", # Volvo
                  "DIS", # Walt Disney
                  ] 

def merge_portfolio(portfolio: list):
    frames = [None]

    # för varje ticker i portfolion, så läggs tickerns data till i frames.
    for ticker in portfolio:
        st = stl.Stock(ticker)
        data = st.returns("5y")
        # print(data) # ta bort kommentaren här om du vill se hur datan ser ut
        frames.append(data)

    merged_portfolio = pd.concat(frames, axis=1)  # slå samman tickerdatan (y-axeln, därav axis=1)
    merged_portfolio.columns = portfolio_list     # byter namn på kolumnerna
    return merged_portfolio


merged_portfolio = merge_portfolio(portfolio_list)
print(merged_portfolio)
merged_portfolio.plot() # här kan man lägga till t ex "logy=True" för logscala på y-axeln
plt.legend(portfolio_list) # Legend baserat på portfolio-listan
plt.show()