# Sales Forecasting and Analysis
![Screenshot 2023-08-28 at 6 13 43 PM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/af8e0700-40f6-4769-8e8d-2d5aa0dfad14)

## Introduction:
In this project, we will dive into the realm of sales data analysis and forecasting. The dataset at hand consists of records pertaining to sales transactions, encompassing a wide range of information such as date, country, store, product, and the number of units sold. Our goal is to extract valuable insights from this dataset through exploratory analysis, visualization, and the application of machine learning techniques to build a sales forecasting model.

## Dataset Overview:

The dataset contains essential information that will be the foundation of our analysis:

* id: A unique identifier for each record.
* date: The date of the sales transaction.
* country: The country where the sale took place.
* store: The store where the sale occurred.
* product: The product that was sold.
* num_sold: The number of units sold in each transaction.



## Importing Libraries 

You start by importing essential libraries like NumPy, Pandas, TensorFlow, and scikit-learn (sklearn). These libraries provide tools for data manipulation, machine learning, and data visualization. Additionally, the XGBRegressor class from the XGBoost library is imported for gradient boosting-based regression.

## Importing the Dataset

The training and test datasets are read from CSV files using the pd.read_csv() function. These datasets are stored in the train_df and test_df DataFrames.

## Dataset Overview

To understand the data, you create an overview DataFrame that contains information about each column in the training dataset. This includes the column name, data type, number of missing values, and the number of unique values.

## Sales Distribution

You generate a histogram to visualize the distribution of the target variable 'num_sold'. This histogram helps you understand the range and frequency of different sales values.

## Timeseries Plot for Sales

A line plot of sales over time (using the 'date' column) provides insights into the temporal trends in sales. This visualization can help identify patterns, seasonality, and overall trends.

## Sales by Country

A boxplot is created to compare the distribution of sales across different countries. This visualization helps you understand how sales vary based on the country.

## Sales by Store

Similar to the previous step, a boxplot is used to compare sales distribution across different stores, shedding light on potential differences in store performance.

## Extraction of Year/Month/Day

The 'date' column is transformed into separate columns for year, month, and day of the week. This data preprocessing step prepares the data for time-based analysis.

## One-Hot Encoding 

Categorical variables such as 'country', 'store', and 'product' are one-hot encoded. This converts categorical data into binary columns, making it suitable for machine learning algorithms that require numerical input.

## Ensuring Consistent Features

The test dataset is brought in line with the training dataset by adding any missing columns (identified in the one-hot encoding process) and setting their values to zero.

## Splitting Data

The dataset is split into training and validation sets using the train_test_split() function. This prepares the data for model training and evaluation.

## Initializing Models

Instances of various regression models (Linear Regression, Random Forest, Gradient Boosting, XGBoost) are created. These models will later be trained and evaluated.

## Training and Evaluation

The models are looped through, trained on the training set, and evaluated on the validation set using RMSE. RMSE helps assess how well the models are performing by measuring the difference between predicted and actual values.

## Hyperparameter Tuning (Grid Search)

For the XGBoost model, hyperparameter tuning is performed using GridSearchCV(). This involves searching for the best combination of hyperparameters (learning rate, max depth, and number of estimators) that minimize the negative mean squared error.

## Testing on Validation Set

The best XGBoost model obtained from hyperparameter tuning is used to predict values on the validation set. The RMSE of these predictions is calculated, giving an indication of the model's performance.

## Best Parameters 

The best hyperparameters identified by the grid search are reported.

## Best Features

The importance of features in the best XGBoost model is computed using feature_importances_. This helps understand which features contribute most to the model's predictions.

## Testing on Kaggle Test Set

The best XGBoost model is used to predict values on the test set. The predictions are rounded, and a submission CSV file is generated.

## Conclusion

The entire code showcases a comprehensive machine learning pipeline, encompassing data exploration, visualization, feature engineering, model training, hyperparameter tuning, and making predictions. It demonstrates your approach to solving a regression problem with time series and categorical data using various machine learning techniques.

## Results

The dictionary displaying RMSE for different models on the validation set helps you compare their performance. Lower RMSE values indicate better predictive accuracy.

The "Validation RMSE with best XGBOOST is 

20.696420047087305" line shows the RMSE of the best XGBoost model on the validation set. This indicates how well the tuned XGBoost model is performing on unseen data.

The tuple "({'learning_rate': 0.1, 'max_depth': 7, 'n_estimators': 200}, 20.84328972067065)" represents the best combination of hyperparameters for the XGBoost model, along with the associated RMSE. These parameters and RMSE value reflect the optimal configuration found through hyperparameter tuning.



