#quandle gives stock info see quandle.com
import quandl
import pandas as pd
import math, datetime
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

df = quandl.get("NSE/PNB")

#print df.tail()

#copied data from quandle to csv
#df.to_csv('pnb_quandle')

# creating features

df = df[['Open','High','Low','Close','Total Trade Quantity']]

df['HighLow_percent'] = (df['High'] - df['Close'])/df['Close'] *100
df['Change_percent'] = (df['Close'] - df['Open'])/df['Open'] *100

df = df[['Close','HighLow_percent','Change_percent','Total Trade Quantity']]


forecast_col = 'Close'
#checking for missing data

df.fillna(-99999, inplace=True)

# predicting future close price
forecast_out = int(math.ceil(0.01*len(df)))
print forecast_out

df['label'] = df[forecast_col].shift(-forecast_out)

x = np.array(df.drop(['label'],1))
x = preprocessing.scale(x)
x_lately = x[-forecast_out:]
x = x[:-forecast_out]

df.dropna(inplace=True)

y = np.array(df['label'])
print len(x)
print len(y)

x_train,x_test,y_train,y_test = model_selection.train_test_split(x,y, test_size=0.4)
clf = LinearRegression(n_jobs= -1)
clf.fit(x_train, y_train)
accuracy = clf.score(x_test,y_test)


forecast_set = clf.predict(x_lately)

print accuracy
print forecast_set
print forecast_out


df['forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['Close'].plot()
df['forecast'].plot
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
           
