# global_Casino
This is a python module which aims to gather models for Stock forecasting.

The aim is to build a tool that investors can use to filter a large database of stocks into a more manageable list of stocks that qualify for further analysis. There are some free screeners out there, as well as more advanced programs that can be quite costly. Selecting stocks can be a difficult and tedious process, and hence we decided to build such tool. 
However, removing emotion and behavioral biases from the investment decision-making process.

**Install**

We need to install the pandas and vantage package to get stock APIs:

  #To install alpha-vantage
  >pip install alpha_vantage                                     
  
  #To install pandas library
  >pip install pandas                                                 

 - [USAGE](https://github.com/devang-7/global_Casino/blob/master/Usage.md)
 
 **Data Frame Structure**
The data frame structure is given by the call on alpha vantage rest API. The column names of the data frames are the ones given by their data structure. 
```python
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
pprint(data.head(2))
```

This is the Output of the above code:

![alt text](https://github.com/devang-7/global_Casino/blob/master/Images/DATA_usage.png)
## Plotting
### Time Series
Using pandas support we can plot the intra-minute value for various stocks quite easily:

```python
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()
```
Giving us as output:
![alt text](images/docs_ts_msft_example.png?raw=True "MSFT minute value plot example")

![alt text](https://github.com/devang-7/global_Casino/blob/master/Images/EMA.png)


