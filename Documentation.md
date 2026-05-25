# Sales Trend Visualization Dashboard Documentation

# Project Title

## E-Commerce Sales Trend Analysis and Forecasting Dashboard

---

# 1. Introduction

The **Sales Trend Visualization Dashboard** is a Data Analytics project developed using Python, Machine Learning, and Streamlit.
The main objective of this project is to analyze e-commerce sales data, visualize important business insights, and predict future sales trends.

This dashboard helps users understand:

* Monthly sales performance
* Category-wise sales
* Region-wise profit
* Top-selling products
* Sales distribution
* Future sales prediction

The project uses various Python libraries for data processing, visualization, machine learning, and dashboard development.

---

# 2. Objectives

The major objectives of this project are:

* To analyze e-commerce sales data
* To visualize sales and profit trends
* To identify top-performing categories and products
* To perform region-wise business analysis
* To build a future sales prediction model
* To create an interactive dashboard using Streamlit

---

# 3. Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Programming Language      |
| Pandas       | Data Processing           |
| Matplotlib   | Data Visualization        |
| Seaborn      | Statistical Visualization |
| Scikit-learn | Machine Learning          |
| Streamlit    | Dashboard Development     |

---

# 4. Dataset Description

The dataset used in this project is:

## `ecommerce_sales_data.csv`

### Important Columns

| Column Name  | Description        |
| ------------ | ------------------ |
| Order Date   | Date of order      |
| Sales        | Total sales amount |
| Profit       | Profit earned      |
| Category     | Product category   |
| Region       | Sales region       |
| Product Name | Name of product    |

---

# 5. Project Workflow

The project follows the following workflow:

1. Import Libraries
2. Load Dataset
3. Data Cleaning
4. Data Preprocessing
5. Exploratory Data Analysis
6. Data Visualization
7. Machine Learning Model Building
8. Future Sales Prediction
9. Streamlit Dashboard Creation

---

# 6. Data Preprocessing

The preprocessing steps include:

* Removing missing values using `dropna()`
* Converting the `Order Date` column into datetime format
* Creating new columns:

  * Month
  * Year

Example:

```python
df['Order Date'] = pd.to_datetime(df['Order Date'])

df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year
```

---

# 7. Data Visualization

Various visualizations are created to analyze sales data.

## 7.1 Monthly Sales Trend

A line chart is used to analyze monthly sales performance.

### Insights:

* Shows seasonal sales trends
* Helps identify high-sales months

---

## 7.2 Category Wise Sales

A bar chart is used to compare sales among different categories.

### Insights:

* Identifies best-performing categories
* Helps understand customer demand

---

## 7.3 Region Wise Profit

A bar chart is used to analyze profit across regions.

### Insights:

* Shows profitable regions
* Helps business expansion decisions

---

## 7.4 Top 10 Selling Products

A bar chart is used to display the top-selling products.

### Insights:

* Identifies high-demand products
* Useful for inventory management

---

## 7.5 Region Wise Sales Distribution

A pie chart is used to show sales contribution by region.

### Insights:

* Displays percentage share of sales

---

## 7.6 Profit Distribution Histogram

A histogram is used to analyze profit distribution.

### Insights:

* Shows frequency of profit values
* Detects unusual patterns

---

## 7.7 Correlation Heatmap

A heatmap is created using Seaborn.

### Insights:

* Shows relationships between numerical variables

---

# 8. Machine Learning Model

The project uses:

## Linear Regression

### Purpose:

To predict future sales trends based on monthly sales data.

---

# 9. Model Training Process

## Features Used

```python
X = df[['Month']]
```

## Target Variable

```python
y = df['Sales']
```

## Train-Test Split

```python
train_test_split()
```

## Model Used

```python
LinearRegression()
```

---

# 10. Model Evaluation

The model performance is evaluated using:

## Mean Absolute Error (MAE)

```python
mean_absolute_error()
```

Lower MAE indicates better prediction accuracy.

---

# 11. Future Sales Prediction

The model predicts sales for future months from January to December.

Example:

| Month | Predicted Sales |
| ----- | --------------- |
| 1     | 12000           |
| 2     | 13500           |
| 3     | 14200           |

---

# 12. Streamlit Dashboard

The project includes an interactive dashboard built using Streamlit.

## Dashboard Features

* Dataset Preview
* Monthly Sales Trend
* Category Analysis
* Profit Analysis
* Product Analysis
* Sales Prediction
* Interactive Charts

---

# 13. Advantages of the Project

* Easy to understand business trends
* Helps in decision making
* Predicts future sales
* Interactive and user-friendly dashboard
* Real-time visualization

---

# 14. Applications

This project can be used in:

* E-commerce companies
* Retail business analysis
* Sales forecasting systems
* Business intelligence applications
* Data analytics learning projects

---

# 15. Conclusion

The **Sales Trend Visualization Dashboard** successfully analyzes e-commerce sales data and provides valuable business insights using visualizations and machine learning techniques.

The project demonstrates:

* Data preprocessing
* Exploratory data analysis
* Visualization techniques
* Predictive analytics
* Dashboard development

This project is useful for understanding sales behavior and making future business decisions.

---

# 16. Future Enhancements

Future improvements can include:

* Advanced Machine Learning models
* Real-time data integration
* Interactive filters
* Deployment on cloud platforms
* Advanced business intelligence features

---

# 17. References

* Python Documentation
* Pandas Documentation
* Matplotlib Documentation
* Seaborn Documentation
* Scikit-learn Documentation
* Streamlit Documentation
