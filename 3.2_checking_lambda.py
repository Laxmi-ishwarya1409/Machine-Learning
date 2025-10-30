from sklearn.linear_model import RidgeCV, LassoCV
import numpy as np


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


ridge_cv = RidgeCV(alphas=[0.01, 0.1, 1, 10, 100])
ridge_cv.fit(X, y)
print(ridge_cv.alpha_)  # best alpha found automatically

lasso_cv = LassoCV(alphas=[0.01, 0.1, 1, 10, 100])
lasso_cv.fit(X, y)
print(lasso_cv.alpha_)
