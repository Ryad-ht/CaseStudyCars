import pandas as pd
import numpy as np

file_path = 'car_prices.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Normalize the 'body' column to lowercase and remove NaN values
df['body'] = df['body'].str.lower()
unique_values = df['body'].unique()
print(unique_values)
df.dropna(subset=['body'], inplace=True)

# Check for missing values
print(df.isnull().sum())

# Remove rows with missing values in key columns
df = df.dropna(subset=['sellingprice', 'year', 'odometer', 'condition'])

# Convert 'saledate' to datetime format, specifying utc=True to avoid warnings
df['saledate'] = pd.to_datetime(df['saledate'], format='%Y-%m-%d %H:%M:%S', errors='coerce', utc=True)

# Removing outliers for 'sellingprice' and 'odometer'
Q1_sp = df['sellingprice'].quantile(0.25)
Q3_sp = df['sellingprice'].quantile(0.75)
IQR_sp = Q3_sp - Q1_sp
df = df[~((df['sellingprice'] < (Q1_sp - 1.5 * IQR_sp)) | (df['sellingprice'] > (Q3_sp + 1.5 * IQR_sp)))]

Q1_od = df['odometer'].quantile(0.25)
Q3_od = df['odometer'].quantile(0.75)
IQR_od = Q3_od - Q1_od
df = df[~((df['odometer'] < (Q1_od - 1.5 * IQR_od)) | (df['odometer'] > (Q3_od + 1.5 * IQR_od)))]


import matplotlib.pyplot as plt
import seaborn as sns

# Ensure plots are displayed inline in Jupyter notebooks
# If using PyCharm, this line is not necessary
# %matplotlib inline

# Distribution of Selling Prices
plt.figure(figsize=(10, 6))
sns.histplot(df['sellingprice'], kde=True)
plt.title('Distribution of Selling Prices')
plt.xlabel('Selling Price')
plt.ylabel('Frequency')
plt.show()

# Average Selling Price by Year
plt.figure(figsize=(12, 8))
sns.barplot(x='year', y='sellingprice', data=df, estimator=np.mean)
plt.title('Average Selling Price by Year')
plt.xticks(rotation=45)
plt.xlabel('Year')
plt.ylabel('Average Selling Price')
plt.show()

# Odometer vs. Selling Price
plt.figure(figsize=(10, 6))
sns.scatterplot(x='odometer', y='sellingprice', data=df, alpha=0.5)
plt.title('Odometer Reading vs. Selling Price')
plt.xlabel('Odometer')
plt.ylabel('Selling Price')
plt.show()




from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Preparing the data
X = df[['year', 'odometer']]  # Features
y = df['sellingprice']  # Target variable

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing the model
model = LinearRegression()

# Fitting the model to the training data
model.fit(X_train, y_train)

# Making predictions on the testing set
y_pred = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error (MSE): {mse}')

# Displaying the coefficients
print(f'Coefficients: Year = {model.coef_[0]}, Odometer = {model.coef_[1]}')
