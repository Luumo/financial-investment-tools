from financelib.portfolio import Portfolio

portfolio_list = ["AMZN", # Amazon
                  "GOOG", # Alphapet C
                  "ABB", # ABB
                  "ARISE.ST", # Arise
                  "ATRLJ-B.ST", # Atrium Ljungberg
                  "AXFO.ST" # Axfood
                  ] 



my_portfolio = Portfolio(portfolio_list)
my_portfolio_returns = my_portfolio.returns("5y", merge = True)
print(my_portfolio_returns)
# portfolio_correlation = my_portfolio.portfolio_correlation("5y")
# print(portfolio_correlation)

