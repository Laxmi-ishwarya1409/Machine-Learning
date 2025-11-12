## 2. Bagging (Bootstrap Aggregation)

### Concept:
Bagging stands for **Bootstrap Aggregation**.

It trains **multiple models in parallel** on different random subsets of the training data, then combines their outputs using:
- **Majority voting** → for classification  
- **Averaging** → for regression

**Goal:**  
> Reduce variance and prevent overfitting.

---

### Algorithm: Steps of Bagging

1. Take the original dataset **D** with **N** samples.  
2. Create multiple random subsets (with replacement) → called **bootstrap samples**:  
   - D₁, D₂, D₃, D₄, …  
3. Train independent base models (M₁, M₂, M₃, …) on each subset.  
4. During prediction:  
   - **Classification:** Use majority vote  
   - **Regression:** Use average of all outputs  

---

### Example (Bagging — Classification)

| Model | Output |
|--------|--------|
| M₁ | 0 |
| M₂ | 1 |
| M₃ | 1 |
| M₄ | 1 |

✅ **Final Output:** 1 (Majority Voting)

---

### Example (Bagging — Regression)

| Model | Output |
|--------|--------|
| M₁ | 120 |
| M₂ | 130 |
| M₃ | 140 |

✅ **Final Output:**  
Mean = (120 + 130 + 140) / 3 = **130**

---

