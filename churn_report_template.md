# Churn Project — Data Gathering, EDA & Preprocessing Report

_Date:_ 08/09/2025
_Author:_ Charlene Kuye

## 1. Overview
Brief context of business problem, definition of churn, time horizon (e.g., 30-day churn), and unit of analysis (customer-level).

## 2. Data Sources Selected
- **Source 1** (file/table): what it contains, date range, grain
- **Why included:** tie to churn hypothesis
- **Key fields:** customer_id, timestamps, label, etc.

(Repeat for each data set.)

## 3. Selection Criteria & Rationale
Explain inclusion/exclusion criteria (e.g., only active customers last 12 months; exclude test accounts).

## 4. EDA Summary
### 4.1 Target
- Class balance (% churn)
- Any label leakage discovered? (e.g., fields updated after churn)

### 4.2 Missingness
- Variables with highest missing rates and how you addressed them

### 4.3 Univariate Highlights
- Top numeric signals (e.g., point-biserial correlation)
- Top categorical signals (churn rate spread)

### 4.4 Anomalies
- Outliers detected (where, why), duplicates, data quality issues

## 5. Cleaning & Preprocessing Decisions
- Duplicates: how handled
- Imputation: numeric (strategy), categorical (strategy + “Missing” class if used)
- Outliers: method (IQR clip / winsorize), justification
- Encoding: one-hot (unknowns handled), rare-category grouping threshold
- Scaling: which scaler and why

## 6. Data Set Ready for Modeling
Files exported, shapes, and feature counts:
- `churn_X_train.csv`, `churn_y_train.csv`
- `churn_X_valid.csv`, `churn_y_valid.csv`
- Preprocessing pipeline: `preprocess_pipeline.joblib`
- Metadata (target name, columns, class balance)

## 7. Risks & Next Steps
- Potential biases, data gaps
- Additional features to engineer (e.g., recency/frequency/monetary, tenure, rolling window aggregates)
- Plan for model baseline(s) in the next phase
