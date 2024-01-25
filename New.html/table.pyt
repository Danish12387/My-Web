import pandas as pd
import matplotlib.pyplot as plt

# create a DataFrame with the given data
data = {
    'Year': [1977, 1978, 1979, 1980],
    'I': [102, 125, 281, 484],
    'II': [71, 106, 229, 447],
    'III': [47, 73, 209, 457],
    'IV': [98, 231, 488, 966]
}
df = pd.DataFrame(data)
df = df.set_index('Year')

# plot the time series
plt.plot(df.index, df.values)

# compute the 4-quarter centered moving average
rolling_mean = df.rolling(window=4, center=True).mean()

# plot the trend line
plt.plot(rolling_mean.index, rolling_mean.values, color='red')

# add title and labels
plt.title('Time Series with 4-Quarter Centered Moving Average Trend')
plt.xlabel('Year')
plt.ylabel('Quarterly Value')

# display the plot
plt.show()
