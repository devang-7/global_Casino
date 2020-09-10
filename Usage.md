To get data from the API, simply import the library and call the object with your API key.You can receive your api_key by registering your e-mail id with alpha vantage.

>from alpha_vantage.timeseries import TimeSeries
>ts = TimeSeries(key='34BMI2433QZQD8DZ',output_format='pandas')

Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('AAPL')
Internally there is a retries counter, that can be used to minimize connection errors (in case that the API is not able to respond in time), the default is set to 5 but can be increased or decreased whenever needed.
For the default date string index behavior
>ts = TimeSeries(key='YOUR_API_KEY',output_format='pandas', indexing_type='date')

The pandas data frame given by the call, can have either a date string indexing or an integer indexing (by default the indexing is 'date'), depending on your needs, you can use both.
