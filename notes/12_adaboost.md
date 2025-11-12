
## 6. AdaBoost (Adaptive Boosting)

### Concept:

AdaBoost combines multiple **weak learners** (usually **Decision Stumps**, i.e., depth=1 trees) into a **strong classifier**.  
Each subsequent model gives **more focus to the data points misclassified** by previous models.

---

### Algorithm (AdaBoost — Classification)

1. Assign **equal weights** to all training samples.  
   - If there are 7 samples → weight = 1/7 each  
2. Train the first weak learner (e.g., Decision Stump).  
3. Compute error → identify misclassified samples.  
4. **Increase weights** of misclassified samples (so the next model focuses on them).  
5. Repeat for multiple weak learners (M₁, M₂, M₃, …).  
6. Combine all weak models with **weighted voting** to make the final prediction.

---

### Goal:

To **give more importance to difficult samples** and build a strong learner by combining many weak models.

---

### Weak Learner Example:
A **Decision Stump** (a 1-level Decision Tree) — splits data based on one feature.  
It’s weak individually, but in a group, becomes powerful.

---

### AdaBoost — Regression:

For regression, AdaBoost minimizes **weighted squared error** and combines outputs using a **weighted average** of weak regressors.

---

### Advantages of AdaBoost

| Benefit | Description |
|----------|--------------|
| Simple | Easy to implement |
| Reduces Bias | Focuses on correcting mistakes |
| Effective | Works even with weak base learners |
| Strong Performance | Performs well on small-to-medium datasets |

---

### Disadvantages of AdaBoost

| Limitation | Description |
|-------------|--------------|
| Sensitive to Noise | Outliers can mislead model updates |
| Computational Cost | Sequential training → slower |
| Overfitting | If weak learners are too complex |

---

### Applications of AdaBoost

- Spam Detection  
- Credit Risk Scoring  
- Fraud Detection  
- Face Recognition  
- Medical Diagnosis  

---