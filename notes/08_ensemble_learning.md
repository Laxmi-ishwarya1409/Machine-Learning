# Ensemble Learning

---

## 1. What is Ensemble Learning?

**Definition:**
Ensemble Learning is a **technique in Machine Learning** where we combine multiple models (learners) to solve a problem and improve performance compared to using a single model.

<!-- **Analogy:**
Instead of relying on one “weak” model (like a single Decision Tree), we combine multiple models and let them **vote or average** their predictions — just like a team making a group decision rather than one person deciding alone. -->

**Goal:**
> To create a **strong learner** by combining the predictions of multiple **weak learners**.

---

## Why Use Ensemble Learning?

| Reason | Explanation |
|--------|--------------|
| Reduces Overfitting | Especially effective for high-variance models like Decision Trees |
| Increases Accuracy | Aggregation improves performance and generalization |
| Works for Both Tasks | Useful for both classification and regression |
| Makes Models Robust | Reduces the impact of noise and random errors |
| Handles Bias–Variance Tradeoff | Balances model stability and complexity |

---

## Types of Ensemble Learning

There are mainly two primary ensemble strategies:

| Type | Description | Execution |
|------|--------------|------------|
| **Bagging (Bootstrap Aggregation)** | Builds multiple models in **parallel** on random subsets of data | Parallel |
| **Boosting** | Builds multiple models **sequentially**, each correcting errors from the previous | Sequential |

---

