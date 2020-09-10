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
The output of the above code is:
![alt text](https://github.com/devang-7/global_Casino/blob/master/Images/Figure_1.png)


### Technical indicators
The same way we can get pandas to plot technical indicators like Bollinger Bands®

```python
import pandas as pd
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

api_key = 'RNZPXZ6Q9FEFMEHM'

ti = TechIndicators(key=api_key, output_format='pandas')
data, meta_data = ti.get_ema(symbol='MSFT', interval='1min', time_period=60, series_type='close')

data.plot()
plt.title('Exponential Moving Average (60 Minutes) Microsoft')
plt.show()
```
The output of the above code is:
![alt text](https://github.com/devang-7/global_Casino/blob/master/Images/EMA.png)

### Sector Performance
We have to buy stocks in accordance with the sector performance. Hence, we can plot historgrams for the sector performance.

```python
from alpha_vantage.sectorperformance import SectorPerformances
import matplotlib.pyplot as plt

sp = SectorPerformances(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = sp.get_sector()
data['Rank A: Real-Time Performance'].plot(kind='bar')
plt.title('Real Time Performance (%) per Sector')
plt.tight_layout()
plt.grid()
plt.show()
```

Giving us as output:






![alt text](https://github.com/devang-7/global_Casino/blob/master/Images/b84b03cb-11d1-444e-83a3-97be15e8088b.jpg)


