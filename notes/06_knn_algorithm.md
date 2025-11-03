# K-Nearest Neighbors (KNN) Algorithm

## 1. Definition
**K-Nearest Neighbors (KNN)** is a supervised machine learning algorithm used for **classification** and **regression** tasks.
- It’s non-parametric (no assumption about data distribution)
- It’s instance-based (lazy learner — doesn’t build a model)
- It’s based on the idea of “similar things are close to each other.”

---

## 2. Purpose
The main goal of KNN is to:

> Predict the label (class) of a new data point based on its nearest neighbors in the dataset.

Example:
> If most of your closest neighbors are “cats,” you are probably a “cat.”

---

## 3. When to Use KNN
- When you want a simple, interpretable model  
- When data is not too large  
- When relationships between features and outputs are non-linear  

---

## 4. How KNN Works — Step-by-Step

### Step 1: Choose the number of neighbors (K)
Select how many neighbors to look at — for example, **K = 3**, **K = 5**, etc.

### Step 2: Calculate the distance
For a new data point, find the distance between it and every point in the dataset.

**Common distance metrics:**

#### • Euclidean Distance
\[
d(p,q) = sqrt{(p_1 - q_1)² + (p_2 - q_2)² + ..... + (p_n - q_n)²}
\]

#### • Manhattan Distance
\[
d(p,q) = |p_1 - q_1| + |p_2 - q_2| + ..... + |p_n - q_n|
\]


---

### Step 3: Find the K nearest neighbors
After calculating all distances, sort them and pick the **K closest points**.

---

### Step 4: Assign the class (for Classification)
Use **majority voting** — whichever class is most frequent among the neighbors becomes the predicted class.

Example:  
If **K = 5**, and neighbors’ classes are `[A, B, A, A, B]` → predict **Class A**.

---

### Step 5: Predict the value (for Regression)
Take the **average (or weighted average)** of the target values of the K nearest neighbors.

Example:  
If **K = 3**, and neighbors’ values = `[40, 50, 60]` →  
Predicted = (40 + 50 + 60) / 3 = **50**

---

## 5. Example (Classification)
You want to classify a new fruit (based on weight & color) as “Apple” or “Orange.”

Choose **K = 3**  
Nearest fruits: `[Apple, Orange, Apple]`  
→ **Prediction: Apple**

---

## 6. Choosing the Right K
| K Value | Behavior |
|----------|-----------|
| Too Small | Model becomes noisy, may **overfit** |
| Too Large | Model becomes too smooth, may **underfit** |

**Note:**  
Use **odd K (3, 5, 7, …)** to avoid ties.  
Try multiple K values and choose the best one using validation accuracy.

---


## 7. Advantages
- Simple to understand and implement  
- No training phase (lazy learner)  
- Works well for non-linear data  
- Can be used for both classification & regression  

---

## 8. Disadvantages
- Slow prediction for large datasets  
- Works bad for Outliners 
- Not suitable for high-dimensional data (curse of dimensionality)  
- Can be biased if data is imbalanced  

---

## 9. KNN Hyperparameters

| Hyperparameter | Meaning | Typical Values |
|----------------|----------|----------------|
| `n_neighbors` | Number of neighbors (K) | 3, 5, 7 |
| `metric` | Distance metric | euclidean, manhattan|

---

## 10. Performance Metrics

**For Classification:**
- Confusion Matrix  
- Accuracy  
- Precision, Recall, F1-Score  
- ROC-AUC  

**For Regression:**
- Mean Absolute Error (MAE)  
- Mean Squared Error (MSE)  
- R² Score  

---

## 11. KNN in Real Life

- Recommender Systems (similar movies or users)  
- Image Recognition (classify images by pixel similarity)  
- Credit Scoring (similar financial profiles)  
- Medical Diagnosis (similar patient symptoms)

---

## 12. Summary Table

| Concept | Explanation |
|----------|-------------|
| Type | Supervised (Classification + Regression) |
| Learning Type | Lazy learning (no training phase) |
| Core Idea | Similar points have similar outputs |
| Distance Metrics | Euclidean, Manhattan, Minkowski |
| Output | Majority voting (Classification), Average (Regression) |
| Requires Scaling? | Yes |
| Sensitive to K | Yes |
| Works for Non-linear Data | Yes |

---
