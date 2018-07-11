#quandle gives stock info see quandle.com
import quandl
import pandas as pd

df = quandl.get("NSE/PNB")

print df.tail()

#copied data from quandle to csv
#df.to_csv('pnb_quandle')

# creating features

df = df[['Open','High','Low','Close','Total Trade Quantity','Turnover (Lacs)']]

df['HighLow_percent'] = (df['High'] - df['Close'])/df['Close'] *100
df['Change_percent'] = (df['Close'] - df['Open'])/df['Open'] *100

df = df[['Close','HighLow_percent','Change_percent','Total Trade Quantity','Turnover (Lacs)']]

print df.tail()
