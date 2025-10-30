# step 1 import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# step 2 create a dataset
experience = np.array([1,2,3,4,5])
salary = np.array([25,30,35,40,45])

n = len(experience)
sum_x = np.sum(experience)
sum_y = np.sum(salary)
sum_xy = np.sum(experience*salary)
sum_x2 = np.sum(experience**2)


# step 3: Manual Calculation of m and c
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)

c = (sum_y - m * sum_x) / n

print("Slope (m):", m)
print("Intercept (c):", c)

# step 4: Predict the salary using our formula

y_pred = m*experience+c
print("Predicted Salaries:", y_pred)

# step 5: Calculate Error and Cost Function

error = salary - y_pred
mse = np.mean(error ** 2)
cost_function = np.sum(error ** 2) / (2 * n)

print("Error for each point:", error)
print("Mean Squared Error (MSE):", mse)
print("Cost Function J(m,c):", cost_function)

# Visualize the Line
# Step 6: Plot the data and regression line
plt.scatter(experience, salary, color='blue', label='Actual Data')
plt.plot(experience, y_pred, color='red', label='Regression Line')
plt.xlabel("Experience (years)")
plt.ylabel("Salary (in 1000s)")
plt.title("Experience vs Salary")
plt.legend()
plt.show()
