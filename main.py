import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    df['body'] = df['body'].str.lower()
    df.dropna(subset=['body'], inplace=True)
    df = df.dropna(subset=['sellingprice', 'year', 'odometer', 'condition'])
    df['saledate'] = pd.to_datetime(df['saledate'], format='%Y-%m-%d %H:%M:%S', errors='coerce', utc=True)
    return df

def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR)))]
    return df

def visualize_data(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['sellingprice'], kde=True)
    plt.title('Distribution of Selling Prices')
    plt.xlabel('Selling Price')
    plt.ylabel('Frequency')
    plt.show()

    plt.figure(figsize=(12, 8))
    sns.barplot(x='year', y='sellingprice', data=df, estimator=np.mean)
    plt.title('Average Selling Price by Year')
    plt.xticks(rotation=45)
    plt.xlabel('Year')
    plt.ylabel('Average Selling Price')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='odometer', y='sellingprice', data=df, alpha=0.5)
    plt.title('Odometer Reading vs. Selling Price')
    plt.xlabel('Odometer')
    plt.ylabel('Selling Price')
    plt.show()

def train_model(df):
    X = df[['year', 'odometer']]
    y = df['sellingprice']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error (MSE): {mse}')
    print(f'Coefficients: Year = {model.coef_[0]}, Odometer = {model.coef_[1]}')

def main():
    file_path = 'car_prices.csv'
    df = load_and_clean_data(file_path)
    df = remove_outliers(df, 'sellingprice')
    df = remove_outliers(df, 'odometer')
    visualize_data(df)
    train_model(df)

if __name__ == "__main__":
    main()