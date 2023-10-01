# Kaggle Competition: Predicting Sales Quantity

![Screenshot 2023-10-01 at 4 24 19 PM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/297a0296-645e-4118-91c5-901f0b41c68c)

## Competition Overview:
This project involved participating in a Kaggle competition titled "Predicting Sales Quantity". The goal of the competition was to develop an accurate machine learning model that could predict the sales quantity for various products across different cities. The dataset provided contained information about cities, their coordinates, population, education level, median income, and sales data for multiple products.

## Project Structure:

### Data Preparation:

The dataset was loaded and explored to understand its structure and features.
City coordinates were extracted and visualized using scatter plots.
Missing values in the dataset were imputed using the K-nearest neighbors (KNN) imputation technique.
A new feature, 'location', was created using clustering algorithms to identify distinct geographical areas based on population, education level, and median income.

### Feature Engineering:

Several new features were created, including 'no_of_city' (number of cities per coordinate), 'total_stores' (total stores in each city), and 'per_capita_income' (median income divided by population).
The dataset was preprocessed and prepared for training the machine learning models.

### Model Selection and Training:

Various machine learning models, including CatBoost Regressor, were tested and evaluated.
Hyperparameter tuning was performed using GridSearchCV to optimize the model's performance.
The training data was split into training and validation sets for model evaluation.

### Model Evaluation and Prediction:

The model's performance was evaluated using root mean square error (RMSE) on the validation set.
The optimized model was used to make predictions on the test dataset.
Predictions were rounded to the nearest integer as the sales quantity was a discrete variable.

### Results and Submission:

The final predictions were saved and submitted to the Kaggle competition.
The submission file included the predicted sales quantities for the test data.

### Files in the Repository:
trainPredicting Sales Quantity.csv: Training dataset containing sales data and city information.
testPredicting Sales Quantity.csv: Test dataset for making predictions.
supplemental_cities.csv: Additional information about cities including population, education level, and median income.
Submission_Predicting Sales Quantity.csv: CSV file containing the final predictions submitted to Kaggle.

### Dependencies:
Python Libraries: Pandas, NumPy, Seaborn, Matplotlib, Scikit-Learn, XGBoost, CatBoost.
Machine Learning Models: CatBoost Regressor, XGBoost Regressor, Linear Regression, Random Forest Regressor, Gradient Boosting Regressor.

### Running the Code:

Ensure you have Python installed on your system along with the required libraries mentioned above.
Place the provided datasets (trainPredicting Sales Quantity.csv, testPredicting Sales Quantity.csv, and supplemental_cities.csv) in the same directory as the Python script.
Execute the Python script to load, preprocess, train the models, and generate predictions.

### Results:

Among the tested classifiers (CatBoost, XGBoost, Random Forest), CatBoost Regressor demonstrated the best accuracy and robustness in predicting sales quantities (RMSE score = 223).
XGBoost, although powerful, tended to overfit the training data, resulting in lower accuracy on the test data.

### Kaggle Competition Link:

https://www.kaggle.com/competitions/predicting-sales-quantity-in-our-dynamic-gridworld/overview

### Conclusion:

This project demonstrates the application of machine learning techniques for predicting sales quantities based on city-related features. The use of advanced models and careful feature engineering allowed for accurate predictions, leading to a competitive rank in the Kaggle competition.
