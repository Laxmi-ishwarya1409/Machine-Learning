## 5. Boosting

### Defination:

Boosting builds models **sequentially**, where **each model corrects the mistakes** made by the previous one.

**Goal:**  
> Reduce bias and build a strong learner from many weak learners.

---

### Key Differences: Bagging vs Boosting

| Feature | Bagging | Boosting |
|----------|----------|----------|
| Execution | Parallel | Sequential |
| Focus | Reduces Variance | Reduces Bias |
| Model Weighting | Equal Weight | Weighted based on performance |
| Error Handling | Independent models | Later models focus on earlier errors |
| Output Combination | Majority/Average | Weighted Sum |

---
