import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

import streamlit as st


# Reading the dataset
df = pd.read_csv("ecommerce_sales_data.csv")


# Displaying first 5 rows
print("First 5 Rows of Dataset:\n")
print(df.head())


# Displaying dataset information
print("\nDataset Information:\n")
print(df.info())


# Displaying column names
print("\nColumn Names:\n")
print(df.columns)


# Removing missing values
df = df.dropna()


# Converting Order Date column into datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])


# Creating Month and Year columns
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year


# Monthly sales analysis
monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(10,5))

monthly_sales.plot(kind='line', marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=0)

plt.grid(True)

plt.show()


# Category wise sales analysis
category_sales = df.groupby('Category')['Sales'].sum()

plt.figure(figsize=(8,5))

category_sales.plot(kind='bar')

plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.xticks(rotation=0)

plt.show()


# Region wise profit analysis
region_profit = df.groupby('Region')['Profit'].sum()

plt.figure(figsize=(8,5))

region_profit.plot(kind='bar')

plt.title("Region Wise Profit")
plt.xlabel("Region")
plt.ylabel("Profit")

plt.xticks(rotation=0)

plt.show()


# Finding top 10 selling products
top_products = df.groupby('Product Name')['Sales'].sum()

top_products = top_products.sort_values(ascending=False)

top_products = top_products.head(10)

plt.figure(figsize=(12,5))

top_products.plot(kind='bar')

plt.title("Top 10 Selling Products")
plt.xlabel("Product Name")
plt.ylabel("Sales")

plt.xticks(rotation=0)

plt.show()


# Region wise sales distribution
region_sales = df.groupby('Region')['Sales'].sum()

plt.figure(figsize=(8,8))

region_sales.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.ylabel("")

plt.title("Region Wise Sales Distribution")

plt.show()


# Profit distribution histogram
plt.figure(figsize=(10,5))

plt.hist(df['Profit'], bins=30)

plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")

plt.xticks(rotation=0)

plt.show()


# Correlation heatmap
numeric_data = df.select_dtypes(include=['float64', 'int64'])

plt.figure(figsize=(8,5))

sns.heatmap(numeric_data.corr(), annot=True)

plt.title("Correlation Heatmap")

plt.xticks(rotation=0)

plt.show()


# Preparing data for prediction model
X = df[['Month']]

y = df['Sales']


# Splitting dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Creating and training Linear Regression model
model = LinearRegression()

model.fit(X_train, y_train)


# Predicting test data
predictions = model.predict(X_test)


# Calculating prediction error
error = mean_absolute_error(y_test, predictions)

print("\nPrediction Model Error:")
print(error)


# Creating future months data
future_months = pd.DataFrame({
    'Month': [1,2,3,4,5,6,7,8,9,10,11,12]
})


# Predicting future sales
future_sales = model.predict(future_months)


# Creating prediction dataframe
prediction_df = pd.DataFrame({
    'Month': future_months['Month'],
    'Predicted Sales': future_sales
})


# Displaying future sales prediction
print("\nFuture Sales Prediction:\n")
print(prediction_df)


# Future sales prediction chart
plt.figure(figsize=(10,5))

plt.plot(
    prediction_df['Month'],
    prediction_df['Predicted Sales'],
    marker='o'
)

plt.title("Future Sales Prediction")
plt.xlabel("Month")
plt.ylabel("Predicted Sales")

plt.xticks(rotation=0)

plt.grid(True)

plt.show()


# Creating Streamlit dashboard
st.title("Sales Trend Visualization Dashboard")


# Showing dataset preview
st.subheader("Dataset Preview")
st.write(df.head())


# Showing monthly sales trend
st.subheader("Monthly Sales Trend")
st.line_chart(monthly_sales)


# Showing category wise sales
st.subheader("Category Wise Sales")

fig, ax = plt.subplots(figsize=(8,5))
category_sales.plot(kind='bar', ax=ax)

ax.set_xlabel("Category")
ax.set_ylabel("Sales")
ax.set_title("Category Wise Sales")

plt.xticks(rotation=0)

st.pyplot(fig)

# Showing region wise profit
st.subheader("Region Wise Profit")

fig, ax = plt.subplots(figsize=(8,5))
region_profit.plot(kind='bar', ax=ax)

ax.set_xlabel("Region")
ax.set_ylabel("Profit")
ax.set_title("Region Wise Profit")

plt.xticks(rotation=0)

st.pyplot(fig)


# Showing top selling products
st.subheader("Top 10 Selling Products")

fig, ax = plt.subplots(figsize=(12,5))
top_products.plot(kind='bar', ax=ax)

ax.set_xlabel("Product Name")
ax.set_ylabel("Sales")
ax.set_title("Top 10 Selling Products")

plt.xticks(rotation=0)

st.pyplot(fig)
# Showing future sales prediction table
st.subheader("Future Sales Prediction")
st.write(prediction_df)


# Showing prediction chart
st.line_chart(
    prediction_df.set_index('Month')
)


# Final message
print("\nSales Trend Visualization Project Completed Successfully!")