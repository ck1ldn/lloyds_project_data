# Churn Project — Data Gathering, EDA & Preprocessing Report
**Date:** 08/09/2025  
**Author:** Charlene Kuye

---

## 1. Overview
This project aims to analyze customer churn using demographic, transactional, support, and churn label data.  
- **Definition of churn:** Customers labeled as churned in `churn_data.csv`  
- **Time horizon:** Up to the last transaction date per customer  
- **Unit of analysis:** Customer-level

---

## 2. Data Sources Selected

**1. customer_demographic.csv** – Customer profiles  
**2. customer_transactions.csv** – Transaction history  
**3. customer_support_log.csv** – Support interactions  
**4. churn_data.csv** – Churn labels  

**Python snippet: Loading and previewing data**

```python
import pandas as pd

df_customers = pd.read_csv("customer_demographic.csv")
df_transactions = pd.read_csv("customer_transactions.csv")
df_support = pd.read_csv("customer_support_log.csv")
df_churn = pd.read_csv("churn_data.csv")

df_customers.head()
| customerid | age | gender | region | plan\_type |
| ---------- | --- | ------ | ------ | ---------- |
| 1001       | 35  | F      | North  | Basic      |
| 1002       | 42  | M      | South  | Premium    |
| 1003       | 28  | F      | East   | Basic      |


3. Selection Criteria & Rationale

Only customers with valid customerid included

Merged all datasets on customerid

Missing values handled with imputation

Python snippet: Cleaning column names

def clean_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df

df_customers = clean_columns(df_customers)
4. EDA Summary
4.1 Target

Churn rate:

df = df_customers.merge(df_churn, on="customerid", how="left")
df['churnstatus'].mean()


Output: 0.12 → 12% churn

4.2 Missingness
import missingno as msno
msno.matrix(df)


Mini table: Missing values

Column	Missing %
age	2%
region	1%
plan_type	0%
total_spent	0%
4.3 Feature Aggregates

Python snippet: Aggregate transactions and support logs

agg_tx = df_transactions.groupby("customerid").agg({
    "amountspent": ["sum", "mean", "count"]
}).reset_index()
agg_tx.columns = ["customerid", "total_spent", "avg_spent", "num_transactions"]
agg_tx.head()


Example output:

customerid	total_spent	avg_spent	num_transactions
1001	1200	100	12
1002	3500	175	20
4.4 Anomalies

Duplicates removed during merges

Outliers handled via IQR clipping

Minor timestamp inconsistencies corrected

5. Cleaning & Preprocessing Decisions

Python snippet: Pipeline for preprocessing

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

numeric_features = ['total_spent', 'avg_spent', 'num_transactions']
categorical_features = ['gender', 'region', 'plan_type']

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])

6. Data Set Ready for Modeling

Exported files:

churn_X_train.csv, churn_y_train.csv

churn_X_valid.csv, churn_y_valid.csv

Preprocessing pipeline: preprocess_pipeline.joblib

Metadata: Target: churnstatus, numeric + categorical features, 12% churn

7. Risks & Next Steps

Biases in demographic distribution

Missing support history for some customers

Engineer features: recency, frequency, monetary (RFM), rolling aggregates

Next: baseline models → logistic regression, random forest

8. Plots & Tables (Placeholders)

Churn distribution: ![Churn Distribution](path/to/churn_distribution.png)

Missing data heatmap: ![Missing Data](path/to/missing_data.png)

Transaction & support aggregates: ![Aggregates](path/to/aggregates.png)