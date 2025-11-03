# Linear Regression

---

## Introduction

- **Linear Regression** is a **Supervised Learning** algorithm used for predicting a continuous value (Y) from one or more input features (X).
- It predicts a continuous value based on one or more input variables.

**Example:**  
Predict a person’s salary (Y) based on years of experience (X).  
We expect that as experience increases, salary increases approximately linearly.

So, the relationship between X and Y can be modeled by a straight line:

\[
Y = mX + c
\]

where:
- **m** = slope (how much Y changes for a unit change in X)  
  \[
  m = n(∑XY)-(∑X)(∑Y)/n(∑X²) - (∑X)²
  \]
- **c** = intercept value  
  \[
  c = ∑Y - m∑X/n
  \]
- **X** = input variable  
- **Y** = predicted or output feature  

Linear Regression finds the **best-fitting straight line** through all the data points.

---

## Purpose
To find the relationship between two or more variables and use it for prediction.

**Goal:**  
Find the line that gives the **least error** between predicted and actual values.

---

## What Does “Best Line” Mean?

The best line is the one that makes the **difference between actual Y and predicted Y** as small as possible.

Error = \( 𝑌−𝑌(predicted) \)

Because errors can be positive or negative, we **square them** and take the **average** — called the **Mean Squared Error (MSE)** or **Cost Function**.

---

## Step-by-Step Explanation

### Step 1: Take a Training Dataset  
We start with sample data having input (X) and output (Y) pairs.

### Step 2: Find Prediction and Error  
Compute predicted Y and find the difference between actual and predicted.

### Step 3: Measure Total Error (Cost Function)
\[
𝐽(𝑚,𝑐)=1/2𝑛∑(𝑌𝑖−(𝑚𝑋𝑖+𝑐))² 
\]

If MSE is:
- **Large** → Line is not fitting well.
- **Small** → Line is close to actual values.

### Step 4: Minimize the Error Using Gradient Descent
We keep adjusting `m` and `c` to reduce the cost function `J`.

---

### Why Derivatives?
To reduce J, we need to know **how J changes** with respect to m and c.  
We do this by calculating **partial derivatives (gradients):**

\[
∂J/∂m = -2/n∑Xi(Y input −Y predicted)
\] and 
\[
∂J/∂c = -2/n∑Xi(Y input −Y predicted)
\]

---

### Step 5: Gradient Descent Updates

We iteratively update m and c:

\[
m := m - α (∂J/∂m)
\] and 
\[
c := c - α (∂J/∂c)
\]

where:
- **α (alpha)** = learning rate (step size)

**Goal:** Find the minimum value of J(m, c), i.e., the **global minimum**.

---

### Step 6: Visualize the Cost Function

If we plot \( J(m) \) vs. \( m \), it forms a **parabola**.  
- The **lowest point (valley)** = global minimum (minimum error).  
- **Gradient Descent** finds this point step-by-step by following the slope.

---

## Performance Metrics

Even after finding the best m and c, we must evaluate how well the model fits unseen data.

---

### (1) Mean Absolute Error (MAE)
\[
MAE = 1/𝑛∑|𝑌 input −𝑌 predited∣
\]

- Average magnitude of errors.  
- Easy to interpret, same unit as target variable.

---

### (2) Mean Squared Error (MSE)
\[
MSE = 1/𝑛∑(𝑌 input −𝑌 predicted)²
\]

- Penalizes large errors more (since squared).  
- Commonly used for optimization.

---

### (3) Root Mean Squared Error (RMSE)
\[
RMSE = sqrt(𝑀𝑆𝐸)
\]

- Brings error back to original units of Y.  
- Useful for comparing models.

---

### (4) R² – Coefficient of Determination
\[
R^2 = 1 - {SS_{res}}/{SS_{tot}}
\]

where:  
\[
SS_{res} = ∑(Y_{input} - Y_{predicted})^2
\]  
\[
SS_{tot} = ∑(Y_{input} - \bar{Y})^2
\]

- Measures how much of the variance in Y is explained by the model.  
- Range: 0 to 1 (closer to 1 = better fit).

---

### (5) Adjusted R²
\[
Adj. R^2 = 1 - (1 - R^2) \frac{n - 1}{n - p - 1}
\]
where:
- **p** = number of predictors (features)

Adjusts R² for multiple features — penalizes extra features that don’t improve the model.

---

## Why We Need These Metrics

| Metric | Purpose |
|--------|----------|
| **MAE** | Shows average actual deviation (easy to interpret) |
| **MSE** | Used for training (smooth gradient) |
| **RMSE** | Same scale as output (practical measure) |
| **R²** | Shows model’s explanatory power |
| **Adjusted R²** | Prevents overfitting in multi-variable regression |

---

## Global vs Local Minima

- **Global Minimum:** Lowest point of the parabola (only one in linear regression since cost is convex).  
- **Local Minimum:** A lower point but not the absolute lowest (in non-convex functions).

---

## Libraries Commonly Used

- **numpy** → Fast mathematical operations (arrays, sum, mean, etc.)
- **pandas** → Handle tabular data (rows & columns)
- **matplotlib** → Plot graphs and visualize data
- **sklearn** → Machine learning models (like `LinearRegression`)

---

## Common Functions (Matplotlib)

| Function | Description |
|-----------|--------------|
| `plt.figure()` | Creates a new plotting area |
| `plt.plot()` | Draws a line for data points |
| `plt.title()` | Adds a title to the chart |
| `plt.xlabel()` | Adds label to X-axis |
| `plt.ylabel()` | Adds label to Y-axis |
| `plt.legend()` | Displays which line represents what |
| `plt.grid(True)` | Adds background grid |
| `plt.show()` | Displays the chart |

---

