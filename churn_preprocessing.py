# churn_preprocessing.py
# Purpose: Load, explore, and clean churn-related data

import pandas as pd
import numpy as np

# File paths
customer_csv     = "customer_demographic.csv"
transactions_csv = "customer_transactions.csv"
support_csv      = "customer_support_log.csv"
churn_csv        = "churn_data.csv"

# Load datasets
df_customers   = pd.read_csv(customer_csv)
df_transactions = pd.read_csv(transactions_csv)
df_support     = pd.read_csv(support_csv)
df_churn       = pd.read_csv(churn_csv)

# ---- Clean column names (lowercase, underscores) ----
def clean_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df

df_customers   = clean_columns(df_customers)
df_transactions = clean_columns(df_transactions)
df_support     = clean_columns(df_support)
df_churn       = clean_columns(df_churn)

# Quick check of shapes
print("Customers:", df_customers.shape, df_customers.columns.tolist())
print("Transactions:", df_transactions.shape, df_transactions.columns.tolist())
print("Support:", df_support.shape, df_support.columns.tolist())
print("Churn:", df_churn.shape, df_churn.columns.tolist())

# ---- Merge: customers + churn ----
df = df_customers.merge(df_churn, on="customerid", how="left")

# ---- Aggregate transactions ----
df_transactions["transactiondate"] = pd.to_datetime(df_transactions["transactiondate"])

agg_tx = df_transactions.groupby("customerid").agg({
    "amountspent": ["sum", "mean", "count"],
    "transactiondate": "max"
})
agg_tx.columns = ["total_spent", "avg_spent", "num_transactions", "last_transaction_date"]
agg_tx = agg_tx.reset_index()

# Calculate recency
reference_date = df_transactions["transactiondate"].max()
agg_tx["recency_days"] = (reference_date - agg_tx["last_transaction_date"]).dt.days

# Merge into main df
df = df.merge(agg_tx, on="customerid", how="left")

# ---- Aggregate support ----
df_support["interactiondate"] = pd.to_datetime(df_support["interactiondate"])

agg_support = df_support.groupby("customerid").agg({
    "interactionid": "count",
    "interactiondate": "max"
}).rename(columns={"interactionid": "tickets_count", "interactiondate": "last_ticket_date"}).reset_index()

df = df.merge(agg_support, on="customerid", how="left")

# ---- Final check ----
print("Final merged dataset:", df.shape)
print(df.head())
