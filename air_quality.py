import pandas as pd

# Load the air quality data
# Replace 'annual_aqi_by_county_2023.csv' with your actual file path if needed
data = pd.read_csv('annual_aqi_by_county_2023.csv')

# Display the first few rows of the dataset to understand its structure
print(data.head())

# Calculate the total days and the number of good days
data['Total Days'] = data['Days with AQI']
data['Good Days'] = data['Good Days']

# Calculate the number of unhealthy days
data['Unhealthy Days'] = data['Total Days'] - data['Good Days']

# Calculate the air impurity percentage
data['Air Impurity Percentage'] = (data['Unhealthy Days'] / data['Total Days']) * 100

# Display the results
print(data[['State', 'County', 'Year', 'Air Impurity Percentage']])