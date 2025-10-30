import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Create a Sample Dataset
# Features: [Experience, Skill Level, Interview Score]
X = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 2],
    [4, 5, 5],
    [5, 6, 4],
    [6, 7, 6],
    [7, 8, 5],
    [8, 9, 7]
])

# Target: Salary (in 1000s)
y = np.array([25, 30, 28, 40, 42, 48, 52, 58])


# Step 2: Fit Linear, Ridge, and Lasso Regression
# Ridge Regression (L2 regularization)
# adds a penalty = α * Σ(w²)
ridge_model = Ridge(alpha=1.0)   # alpha = λ 
ridge_model.fit(X, y)

# Lasso Regression (L1 regularization)
# adds a penalty = α * Σ|w|
lasso_model = Lasso(alpha=0.1)
lasso_model.fit(X, y)

# Step 3: Compare Coefficients (Weights)
print("Ridge Coefficients :", ridge_model.coef_)
print("Lasso Coefficients :", lasso_model.coef_)


# Step 4: Compare Predictions
y_pred_ridge = ridge_model.predict(X)
y_pred_lasso = lasso_model.predict(X)


# Step 5: Evaluate Each Model
def evaluate_model(y_true, y_pred, model_name):
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    print(f"{model_name} → MSE: {mse:.2f}, R²: {r2:.3f}")

evaluate_model(y, y_pred_ridge, "Ridge Regression")
evaluate_model(y, y_pred_lasso, "Lasso Regression")

# Step 6: Visual Comparison (Predictions vs Actual)
plt.figure(figsize=(8,5))
plt.plot(y, label='Actual Salary', color='black', linewidth=2)
plt.plot(y_pred_ridge, label='Ridge', linestyle='--')
plt.plot(y_pred_lasso, label='Lasso', linestyle='--')
plt.title("Ridge vs Lasso Regression")
plt.xlabel("Sample Index")
plt.ylabel("Salary (in 1000s)")
plt.legend()
plt.grid(True)
plt.show()
