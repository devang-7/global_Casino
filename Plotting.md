Using pandas library support we can plot the charts for a particular stock. We can alter the time period as per our needs.
Here, we have used the stock symbol for Apple.
    
    >from alpha_vantage.timeseries import TimeSeries
    >import matplotlib.pyplot as plt

    >ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
    >data, meta_data = ts.get_intraday(symbol='AAPL',interval='60min', outputsize='full')
    >data['4. close'].plot()
    >plt.title('Intraday Times Series for the Apple stock (60 mins)')
    >plt.show()
