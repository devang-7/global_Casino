
import yfinance as yf

rel = yf.Ticker("RELIANCE.NS")
print(rel)
"""
returns
<relinfo.Ticker object at 0x1a1715e898>
"""

# get stock info
rel.info



# get historical market data, here max is 5 years.
print(rel.history(period="1"))
