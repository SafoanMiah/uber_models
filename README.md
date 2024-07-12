# $$\text{Uber Price Prediction And Regression Model Analysis}$$

## $$\text{Description:}$$
This project provides a comprehensive and extensive approach to predicting Uber prices using a variety of regression models. 
Through the use of **data cleaning**, **exploratory data analysis**, **model training**, **hyperparameter tuning**, and **model evaluation**. The project is structured to demonstrate a full cycle of data processing and modelling to achieve accurate predictions.

## <div align="center">[Streamlit Application](https://regression-price.streamlit.app/predictions)</div>
Interactive Streamlit application designed to predict Uber prices. Web application makes use of the best-performing model from the comprehensive analysis and allows users to input parameters for real-time predictions. Paired with SQL Database usage to store entries.

---
### Cleaning:
Improving data quality by:
- Removing unecessary columns
- Removing invalid fields
- Excluding outliers
- Date time correction
- Hevershine distance calculation
---
### Analysis:
Exploratory Data Analysis to uncover insights using:
- Exploratory Data Analysis
- Mapping 
- Time Series
- Corelation and Relationships
---
### Model Training:
Implementing, tuning, and evaluating multiple regression models to identify the most effective one for Uber price predictions. 
Trough hyperparameter tuning, model training, and performance evaluation using metrics and visualizations.
- Data Preparation
- Model Description
- Hyperparameter Tuning
- Model Traning and Scoring
- Results Visualization


#### Models:
  - Linear Regression
  - Ridge Regression
  - Lasso Regression
  - ElasticNet Regression
  - Decision Tree Regression
  - Random Forest Regression
  - Gradient Boosting Regression
  - Saving best model


#### Metrics:
  - Mean Absolute Error
  - Root Mean Squared Error
  - $R^2$ Score
---
### Streamlit:
- Interactive input of pickup and dropoff locations (both address and coordinates)
- Optional time and date input for predictions
- Real-time prediction of Uber ride prices
- Visualization of pickup and dropoff locations on a map
- SQL Database of entered rides with options to view and clear entries
---  
## $$\text{File Structure:}$$

```
├── data/
│ ├── uber_rides.csv            # Raw data from:  
│ └── processed_data.csv        # Processed and cleaned data
├── model/
│ └── trained_model.pkl         # Best score trained model
├── notebooks/
│ ├── data_cleaning.ipynb       # Data Cleaning Notebook
│ ├── data_analysis.ipynb       # Exploratory Data Analysis
│ ├── model_training.ipynb      # Model Tuning Training and Comparison
├── scripts/
│ ├── distance_utils.py         # Functions for distance calculations
│ ├── dataframe_utils.py        # Functions for DataFrame
├── sql_db/
│ ├── create_db.py              # Script to create DataBase (SQL)
│ ├── load_to_sql.py            # Inserting CSV into Dataframe (SQL)
│ └── uber_rides.db             # SQLite DataDabse with processed data
├── requirements.txt
└── README.md
```
