# Stock Movement Prediction Using Technical Indicators and LSTM
![Screenshot 2023-09-29 at 9 56 54 PM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/511fd727-ec31-402f-b77d-7180e0f5a783)


This repository showcases a comprehensive stock price prediction system using historical data, technical indicators, and LSTM (Long Short-Term Memory) neural networks. The project incorporates various components such as data fetching, data analysis, technical indicator integration, feature engineering, model construction, training, and visualization. The primary goal is to predict stock movements for Alphabet Inc. (GOOGL) based on historical price data and the Relative Strength Index (RSI) technical indicator.

## Notebook Overview
Notebook Name: Stock Movement Prediction Using Technical Indicator RSI.ipynb

## Environment Setup

### Dependencies
The project requires the yfinance library for fetching historical stock data and various Python libraries such as NumPy, Pandas, TensorFlow, Plotly, and requests.

### Installation
The required packages can be installed using !pip install package_name.

### Fetching Stock Market Data

The code fetches historical stock data for Alphabet Inc. (GOOGL) from Yahoo Finance starting from January 1, 2018, with a daily interval.

## Understanding the Stock Market Data

Provides an in-depth analysis of the fetched data, including the shape, first and last few records, missing value check, and statistical summary.

## Understanding the Trends Within Data

Utilizes Plotly to visualize stock trends, including closing prices, volume, open prices, high prices, low prices, and adjusted close prices.

## Data Preparation

Implements data preprocessing techniques, including feature scaling using MinMaxScaler, and prepares the data for model training.
Defines a custom Scaler class for feature scaling and creates features and targets using a rolling window approach.

## Model Building

Constructs a Bidirectional LSTM neural network using TensorFlow/Keras.
Compiles the model with Mean Squared Error (MSE) loss and Stochastic Gradient Descent (SGD) optimizer.
Incorporates custom callbacks for learning rate adjustment and saving the best model weights during training.

## Incorporating RSI as a Feature
Integrates the Relative Strength Index (RSI) technical indicator into the model as an additional feature.
Utilizes the Alpha Vantage API to obtain RSI data for GOOGL stock.

## Model Training and Evaluation
Trains the LSTM model with the prepared data and evaluates its performance on the test dataset.
Visualizes the predicted stock prices against the actual prices using interactive line charts created with Plotly.

## Requirements
#### Python 3.x
#### Jupyter Notebook
#### Libraries: NumPy, Pandas, yfinance, TensorFlow, Plotly, requests

## Acknowledgments
Data Source: Yahoo Finance
Technical Indicator Data: Alpha Vantage API
