import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# model that finds m (slope) and c (intercept).
from sklearn.linear_model import LinearRegression 
# mean_absolute_error, mean_squared_error, r2_score: used to check performance.
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score


experience = np.array([1,2,3,4,5])
salary = np.array([25,30,35,40,45])

# Step 1: Using scikit-learn model
X = experience.reshape(-1, 1)  # reshape because sklearn expects 2D array
model = LinearRegression()
model.fit(X, salary)  # fit means: learn m and c

print("Slope (m):", model.coef_)
print("Intercept (c):", model.intercept_)

# Predictions
y_pred_lib = model.predict(X)


# Step 2: Evaluate Performance
mae = mean_absolute_error(salary, y_pred_lib)
mse = mean_squared_error(salary, y_pred_lib)
rmse = np.sqrt(mse)
r2 = r2_score(salary, y_pred_lib)

# Adjusted R²
n = len(salary)  # number of data points
p = 1  # number of predictors (experience)
adj_r2 = 1 - (1 - r2) * ((n - 1) / (n - p - 1))

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R²:", r2)
print("Adjusted R²:", adj_r2)









# # Linear Regression using Scikit-Learn

# # Step 1: Import required libraries
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# # Step 2: Create the dataset
# # Experience (in years)
# X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)   # reshape to 2D for sklearn

# # Salary (in 1000s)
# y = np.array([25, 30, 35, 40, 45])

# # Step 3: Create and train the Linear Regression model
# model = LinearRegression()
# model.fit(X, y)   # Finds best m and c (internally minimizes cost function)

# # Step 4: Extract parameters (m and c)
# m = model.coef_[0]        # slope
# c = model.intercept_      # intercept

# print(f"Slope (m): {m}")
# print(f"Intercept (c): {c}")

# # Step 5: Predict salary for each experience level
# y_pred = model.predict(X)
# print("Predicted Salaries:", y_pred)

# # Step 6: Visualize the actual points and regression line
# plt.figure(figsize=(8,5))
# plt.scatter(X, y, color='blue', label='Actual Data')
# plt.plot(X, y_pred, color='red', label='Regression Line')
# plt.title("Experience vs Salary (Linear Regression)")
# plt.xlabel("Experience (Years)")
# plt.ylabel("Salary (in 1000s)")
# plt.legend()
# plt.grid(True)
# plt.show()

# # Step 7: Calculate Performance Metrics
# mae = mean_absolute_error(y, y_pred)
# mse = mean_squared_error(y, y_pred)
# rmse = np.sqrt(mse)
# r2 = r2_score(y, y_pred)

# # Display results
# print("\nPerformance Metrics:")
# print(f"Mean Absolute Error (MAE): {mae}")
# print(f"Mean Squared Error (MSE): {mse}")
# print(f"Root Mean Squared Error (RMSE): {rmse}")
# print(f"R² Score: {r2}")

# # Step 8: Predict for a new value (e.g., 6 years of experience)
# new_experience = np.array([[6]])
# predicted_salary = model.predict(new_experience)
# print(f"\nPredicted Salary for 6 years experience: {predicted_salary[0]:.2f}k")

