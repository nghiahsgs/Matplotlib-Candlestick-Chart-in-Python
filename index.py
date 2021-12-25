# pip install mpl_finance
# pip install --upgrade mplfinance

# tutorial
# https://saralgyaan.com/posts/python-candlestick-chart-matplotlib-tutorial-chapter-11/

# web download data stock
# https://www1.nseindia.com/products/content/equities/indices/historical_index_data.htm



import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
# from mplfinance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates

# We are using the style ‘ggplot’.
plt.style.use('ggplot')

# Extracting Data for plotting
data = pd.read_csv('data.csv')
ohlc = data.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]

# convert 28-Dec-2020 =>  2020-12-28
ohlc['Date'] = pd.to_datetime(ohlc['Date'])

# chuyển ngày ra số, tính từ 1970-01-01
ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num)

#  converted all the data to float using pandas.astype().
ohlc = ohlc.astype(float)
ohlc['SMA5'] = ohlc['Close'].rolling(5).mean()

def draw_chart(ohlc,is_show_sma):
    # Creating Subplots
    fig, ax = plt.subplots()

    candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)

    if is_show_sma:
        ax.plot(ohlc['Date'], ohlc['SMA5'], color='green', label='SMA5')
        plt.legend()

    # Setting labels & titles
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    fig.suptitle('Daily Candlestick Chart of NIFTY50')

    # Formatting Date
    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)

    # tránh trường hợp date đè lên nhau
    fig.autofmt_xdate()

    fig.tight_layout()

    plt.show()

# draw_chart(ohlc,True)
draw_chart(ohlc,False)