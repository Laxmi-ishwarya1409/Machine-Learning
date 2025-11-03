# Regularization in Linear Regression (Ridge & Lasso)

---

## The Goal of Linear Regression

The goal of linear regression is to find a straight line:

\[
y = mX + c
\]

It does this by minimizing the **Cost Function (MSE)**:

\[
𝐽=1/𝑛∑(𝑦𝑖−y predicted)²0
\]

But sometimes, when we have:
- Too many features (independent variables)
- Noisy or correlated data

→ The model **overfits** — it performs great on training data but poorly on unseen data.

---

## Overfitting & Underfitting

When training a regression model (like Linear Regression), we want it to work well on **unseen data**, not just the training data.

### ➤ Overfitting
- Model fits training data **too perfectly** — passes through almost every point.
- Performs great on training data but **bad on test data**.
- Therefore:
  - **Low bias** (fits training data well)
  - **High variance** (fails on new data)

### ➤ Underfitting
- Model cannot even fit the training data properly.
- Performs poorly on both training and test data.
- Therefore:
  - **High bias**
  - **High variance**

### ➤ Goal
We want a **generalized model** that performs well on both training and test data.

---

## Regularization (Ridge & Lasso)

Regularization is a technique to **prevent overfitting**.

It **penalizes large coefficients** (slope values) in the model so that the line doesn’t become too steep.

---

### Without Regularization
The model only cares about minimizing error:

\[
𝐽=1/2𝑚∑(𝑦𝑖−𝑦 predicted)²
\]

→ This can make the model too flexible and overfit.

---

### With Regularization
We tell the model:  
“Don’t just minimize error — also keep your coefficients small.”

So, we add a penalty term:

\[
𝐽=1/2𝑚∑(𝑦 𝑖 − 𝑦 predicted)² + 𝜆 x Penalty
\]

Where:
- **λ (lambda)** = Regularization strength (hyperparameter)  
  → Controls how strong the penalty is.  
- **Penalty** = Depends on whether we use **L1** or **L2** regularization.

---

### Role of λ (Lambda)

| λ Value | Meaning | Effect |
|----------|----------|--------|
| λ = 0 | No regularization | Normal Linear Regression |
| λ → Large | Too much penalty | Underfitting |
| λ → Small but > 0 | Just right | Balances fit & simplicity |

---

## Types of Regularization

### 1️⃣ Ridge Regression (L2 Regularization)

Ridge Regression adds the **sum of squares of coefficients** (weights) to the cost function:

\[
𝐽=1/𝑛∑(𝑦 𝑖 − 𝑦 predicted)² + 𝜆 ∑𝑤𝑗² 
\]

Where:
- **λ** = Regularization strength (hyperparameter)
- **wⱼ** = Model coefficients (slopes)
- **λ ∑ wⱼ²** = L2 penalty term

#### 🔹 Intuition
- Keeps **all features**, but **shrinks coefficients** toward 0.  
- Reduces the impact of less important features.  
- Helps when features are **correlated (multicollinearity)**.

✅ **Ridge says:**  
> “Don’t remove any feature, but keep their weights small and balanced.”

**Main Purpose:** Prevents Overfitting.

---

### 2️⃣ Lasso Regression (L1 Regularization)

Lasso Regression adds the **sum of absolute values of coefficients** to the cost function:

\[
𝐽=1/𝑛∑(𝑦𝑖−𝑦 predicted)²+𝜆∑∣𝑤𝑗∣
\]

#### 🔹 Intuition
- Can force some coefficients to become **exactly 0**.  
- Automatically selects **important features** and removes irrelevant ones.  
- Great for **feature selection**.

✅ **Lasso says:**  
> “I’ll keep only the most important features and make the rest 0.”

**Main Purpose:** Prevents Overfitting **and** performs Feature Selection.

---

