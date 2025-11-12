## 3. Random Forest — (Example of Bagging)

### What is Random Forest?

Random Forest is an **ensemble of Decision Trees**, built using the **Bagging technique**.

Each tree:
- Trains on a **random subset of rows (bootstrap samples)**
- Uses a **random subset of features** at each split

Final prediction:
- **Classification:** Majority voting  
- **Regression:** Mean/Average  

---

### Why Random Forest?

Solves overfitting of Decision Trees  
Reduces variance by averaging multiple trees  
Works well for both classification and regression  
Handles missing data and outliers well  
Requires minimal preprocessing (no scaling needed)

---

### Problems with a Single Decision Tree

| Problem | Description |
|----------|--------------|
| Overfitting | Fits perfectly on training data but fails on new data |
| High Variance | Small change in data causes large change in tree |
| Low Bias, High Variance | Model memorizes instead of generalizing |

**Random Forest fixes this:**  
By combining many trees → results in **low bias and low variance**.

---

### Algorithm of Random Forest

1. Select random samples (rows) and random features (columns).  
2. Train a **Decision Tree** on each subset.  
3. Aggregate predictions:
   - Majority vote → classification  
   - Average → regression  

---

### Random Forest Interview Points

| Question | Answer |
|-----------|---------|
| Is normalization/standardization required? | No |
| Is it affected by outliers? | No |
| Key hyperparameters | `n_estimators`, `max_depth`, `max_features` |
| Difference from Decision Tree | Random Forest = many trees + bagging → less overfitting |

---

## 4. Custom Bagging

You can create your own ensemble using **different base models** (not just Decision Trees).

### Example:

| Model | Type | Output |
|--------|------|--------|
| M₁ | Logistic Regression | 1 |
| M₂ | KNN | 0 |
| M₃ | Decision Tree | 1 |

**Final Output:** Majority Vote = **1**

This is called **Custom Bagging** — combining diverse learners to improve robustness.

---

