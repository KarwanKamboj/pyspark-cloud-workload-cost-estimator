# Cloud Workload Cost Estimator using PySpark

## Overview
This project uses Apache PySpark and machine learning to analyze cloud workload resource utilization and estimate workload costs. It uses Google Cluster Data-based workload records and applies Linear Regression and Random Forest Regression to predict cost per second.

## Objectives
- Analyze CPU, memory, and disk resource utilization.
- Clean and preprocess large-scale workload data using PySpark.
- Estimate workload cost using an assumed pricing formula.
- Train and compare machine learning regression models.
- Visualize actual and predicted costs.

## Technologies Used
- Python
- Apache PySpark
- Spark MLlib
- Pandas
- Matplotlib
- Google Cluster Data

## Machine Learning Models
1. Linear Regression
2. Random Forest Regression (50 trees)

## Model Performance

| Metric | Linear Regression | Random Forest |
|---|---:|---:|
| MAE | 0.00000242 | 0.00000153 |
| RMSE | 0.00000405 | 0.00000315 |
| R² Score | 0.8103 | 0.8850 |

Random Forest performed better than Linear Regression across the evaluated metrics.

## Project Workflow
1. Load workload dataset.
2. Inspect and handle missing values.
3. Perform data cleaning and preprocessing.
4. Calculate workload duration and estimated cost.
5. Perform exploratory data analysis.
6. Select relevant features using VectorAssembler.
7. Split data into training and testing sets.
8. Train regression models.
9. Evaluate model performance.
10. Visualize predictions and compare results.

## How to Run

Install the required libraries:

```bash
pip install pyspark pandas matplotlib
```

Run the Python script:

```bash
python main.py
```

Update the dataset file path in the code before execution.

## Important Note
The cost per second is calculated using an assumed resource-pricing formula. It does not represent actual Google Cloud billing data or real cloud invoices. Model predictions are based on this estimated target.

## Future Improvements
- Use actual cloud pricing and billing data.
- Perform automated feature selection and hyperparameter tuning.
- Build an interactive dashboard for cost analysis.

## Author
Developed as a machine learning and big data analytics project using PySpark.
