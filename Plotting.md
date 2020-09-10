Using pandas library support we can plot the charts for a particular stock. We can alter the time period as per our needs.

>from alpha_vantage.timeseries import TimeSeries
>import matplotlib.pyplot as plt

>ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
>data, meta_data = ts.get_intraday(symbol='AAPL',interval='60min', outputsize='full')
>data['4. close'].plot()
>plt.title('Intraday Times Series for the MSFT stock (1 min)')
>plt.show()
