# Logistic Regression

## What is Logistic Regression?
Logistic Regression is a machine learning algorithm used for **classification problems** — where the output is categorical (Yes/No, 0/1, etc.).

---

## Purpose of Logistic Regression
To model the relationship between independent variables (features) and a **binary dependent variable (target)** using probabilities.

---

## Why Logistic Regression?

We use Linear Regression to predict continuous values, but it fails for classification problems because:

- Linear Regression outputs values beyond 0–1 (like -3, 5, 10).
- It’s sensitive to outliers, shifting the line and giving wrong predictions.
- We need probabilities between 0 and 1 for classification.
- Logistic Regression “squashes” linear outputs between 0 and 1 using the **sigmoid function**.

---

## Logistic Regression Equation

We calculate:
\[
z = 𝜃0+𝜃1𝑥1+𝜃2𝑥2+⋯+𝜃𝑛𝑥𝑛
\]

Then apply the sigmoid function:
\[
ℎ𝜃(𝑥)=1/1+e^{-z}
\]

So, `h(x)` = probability that the output belongs to class 1.

---

## Sigmoid (Squashing) Function
To squash the linear function output into the [0,1] range, we use the sigmoid (logistic) function
\[
σ(z)=1/1+e^{-z}
\]

- If z → +∞ → output → 1  
- If z → -∞ → output → 0  
- If z = 0 → output = 0.5  

So, it perfectly represents probabilities.

Example:  
z = 2 → 0.88  
z = -2 → 0.12

---

## Decision Boundary
The model decides:

- If ℎ𝜃(𝑥)≥0.5⇒𝑦=1
- If ℎ𝜃(𝑥)<0.5⇒𝑦=0

The “0.5 line” is called the **decision boundary**.

---

## Assumptions
- Dependent variable is binary.  
- Independent variables are linearly related to log-odds of the outcome. 
- Observations are independent.  
- No perfect multicollinearity.  
- The dataset should be large enough to estimate probabilities accurately.

---

## Why Not Linear Regression Cost Function?

Linear regression cost:
\[
𝐽(𝜃)=1/2𝑚∑(ℎ𝜃(𝑥(𝑖))−𝑦(𝑖))²
\]

Fails for logistic regression because:
- Sigmoid introduces non-linearity.
- Cost function becomes non-convex.
- Gradient descent may get stuck in local minima.

---

## Logistic Regression Cost Function

\[
𝐽(𝜃)=−1/𝑚∑𝑖=1/𝑚[𝑦(𝑖)log(ℎ𝜃(𝑥(𝑖)))+(1−𝑦(𝑖))log(1−ℎ𝜃(𝑥(𝑖)))]
\]

✅ **Properties**
- Convex → only one global minimum.  
- Strong penalty for wrong confident predictions.

---

## Gradient Descent for Logistic Regression

We minimize \( 𝐽(𝜃) \) using:
\[
𝜃𝑗:=𝜃𝑗−𝛼∂𝐽(𝜃)/∂𝜃𝑗
\]

Where, 𝛼 = learning rate.

- The gradient (derivative) simplifies nicely to:
\[
∂𝐽(𝜃)/∂𝜃𝑗=1/𝑚∑(ℎ𝜃(𝑥(𝑖))−𝑦(𝑖))𝑥𝑗(𝑖)
\]
- Same as linear regression but with sigmoid instead of plain linear output.

---

## Performance Metrics
-Once the Logistic Regression model predicts probabilities,
we need to evaluate how good those predictions are.

### 1. Confusion Matrix
- A confusion matrix compares actual vs predicted values. It helps us understand how many predictions were correct or wrong.

| Actual / Predicted | Predicted: 1 | Predicted: 0 |
|--------------------|--------------|--------------|
| Actual: 1          | TP           | FN           |
| Actual: 0          | FP           | TN           |

- **TP:** Correctly predicted 1  
- **TN:** Correctly predicted 0  
- **FP:** Predicted 1 but actually 0  
- **FN:** Predicted 0 but actually 1  

---

### 2. Accuracy
\[
Accuracy = {TP + TN}/{TP + TN + FP + FN}
\]
- Best when data is balanced.

---

### 3. Precision
\[
Precision = {TP}/{TP + FP}
\]
- Best when **false positives are costly** (e.g., spam detection).

---

### 4. Recall (Sensitivity / TPR)
\[
Recall = {TP}/{TP + FN}
\]
Best when **false negatives are costly** (e.g., disease detection).

---

5. F1-Score
\[
F1 = 2 * {Precision /times Recall}/{Precision + Recall}
\]
- Best when data is **imbalanced**.

---

### 6. Fβ-Score
\[
𝐹𝛽=(1+𝛽²)×{𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛×𝑅𝑒𝑐𝑎𝑙𝑙}/{(𝛽²×𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛)+𝑅𝑒𝑐𝑎𝑙𝑙}
\]

- β > 1 → more focus on Recall  
- β < 1 → more focus on Precision  

---

### 7. ROC Curve
- Plots **True Positive Rate (Recall)** vs **False Positive Rate (FPR)**
\[
FPR = {FP}/{FP + TN}
\]
- Closer to top-left → better model.

---

### 8. AUC (Area Under ROC Curve)
- Measures the overall ability to distinguish between classes.
- AUC = 1 → Perfect classifier  
- AUC = 0.5 → Random guessing  

---

## Balanced vs Imbalanced Data

- **Balanced:** Equal 0s and 1s → Accuracy works well.  
- **Imbalanced:** One class dominates → Accuracy misleading.

---

## Handling Imbalanced Data
1. **Oversampling:** Duplicate or synthesize minority samples.  
2. **Undersampling:** Remove majority samples.  
3. **Use Proper Metrics:** Precision, Recall, F1, ROC-AUC.  
4. **Adjust Threshold:** Change 0.5 cutoff to favor recall or precision.

---
