# Decision Tree Algorithm — Complete Explanation (Step by Step)

## 1️. What is a Decision Tree?

A **Decision Tree** is a supervised learning algorithm used for **classification** and **regression** tasks.

It works like a **flowchart**:

- **Each internal node** → tests a feature (e.g., “Age < 30?”)  
- **Each branch** → represents an outcome (Yes/No)  
- **Each leaf node** → gives the final decision or prediction  

### Example (Classification)

<pre>
If Age < 30:
If Salary > 50K → Buy Laptop
Else → Don’t Buy
Else:
Buy
</pre>


### Example (Regression)
<pre>
If Area < 1000:
Price = 5L
Else:
Price = 10L
</pre>



---

## 2️. Purpose of Decision Tree

- To split data into smaller, more homogeneous groups.  
- To find rules that clearly separate classes or predict continuous values.  
- It **mimics human decision-making**, making it easy to interpret.

---

## 3️. How a Decision Tree Works — Step by Step

### **Step 1:** Start with the full dataset (root node)
All training data is in one group.

### **Step 2:** Choose the best feature to split
The algorithm checks each feature and finds the one that gives the **purest child nodes**.

### **Step 3:** Split the dataset
Divide it into subsets based on the best feature’s values (e.g., “Age < 30”).

### **Step 4:** Repeat recursively
Keep splitting until:
- All samples in a node belong to one class, **or**
- You reach a **stopping condition** (like max depth or minimum samples).

### **Step 5:** Assign final label/value at leaf nodes.

---

## 4️. Important Terms

| Term | Meaning |
|------|----------|
| **Root Node** | Represents the entire dataset (starting point). |
| **Decision Node** | Splits the data into subsets. |
| **Leaf Node (Terminal Node)** | Gives the final output (no more splitting). |
| **Branch** | Outcome of a decision (True/False, Yes/No). |
| **Splitting** | Dividing data into subgroups. |
| **Pruning** | Cutting off unnecessary branches to reduce overfitting. |
| **Depth** | Number of levels in the tree. |
| **Impurity** | Measure of how mixed a node is (more pure = better). |

---

## 5️. How to Choose the Best Split (Impurity Measures)

The algorithm decides which feature to split by measuring **how “pure” the data becomes after splitting**.

### For Classification Trees

#### a. **Entropy (E)**
Measures impurity (how mixed the data is).

\[
Entropy = -p_1+ \log_2(p_1) + -p_2 - \log_2(p_2)-
\]

Where \( p_1, p_2 \) = proportions of each class.

- Pure node (all same class) → **Entropy = 0**  
- Mixed (50–50) → **Entropy = 1** (max)

#### b. **Information Gain (IG)**  
Tells us how much uncertainty (entropy) is reduced after the split.

\[
IG = Entropy_{before} - Entropy_{after}
\]

**Higher Information Gain = Better Feature to Split**

#### c. **Gini Index (Gini Impurity)**  
Used in **CART algorithm**.

\[
Gini = 1 - \sum(p_i^2)
\]

- Gini = 0 → Pure node  
- Gini = 0.5 → Completely mixed

---

### For Regression Trees

We use **Variance Reduction**:

\[
Var(S) = {1}/{n} \sum (y_i - \bar{y})^2
\]

Best split → gives **maximum reduction in variance**.

---


## 6. Overfitting and Pruning

### Overfitting
- When the tree becomes too deep and learns **noise instead of patterns**.  
- Performs well on training data but poorly on unseen data.

### Pruning
Removes branches that don’t add value → helps **generalize better**.

**Types of Pruning:**

- **Pre-Pruning (Early Stopping)**  
  Stop growing tree early using:
  - `max_depth`
  - `min_samples_split`
  - `min_samples_leaf`

- **Post-Pruning (Cost Complexity Pruning)**  
  Grow the full tree first, then remove unnecessary branches.

---

## 7. Advantages and Disadvantages

### Advantages
- Easy to **visualize and interpret**  
- Handles **numerical & categorical** data  
- No **feature scaling** required  
- Works for **classification & regression**

### Disadvantages
- Prone to **overfitting**  
- **Unstable** (small data change → different tree)  
- **Greedy algorithm** (locally optimal, not globally)  
- Can be **biased** towards features with many levels

---

## 8. Performance Metrics

### For Classification
- Confusion Matrix  
- Accuracy  
- Precision  
- Recall  
- F1-Score  
- ROC Curve & AUC

### For Regression
- Mean Absolute Error (MAE)  
- Mean Squared Error (MSE)  
- Root Mean Squared Error (RMSE)  
- R² Score  

---
