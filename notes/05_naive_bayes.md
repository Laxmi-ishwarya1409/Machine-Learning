# Naive Bayes Algorithm

Naive Bayes is a simple, fast algorithm used for **classification**.

---

## Where It Is Used
It’s built on **Bayes’ Theorem**, and makes a strong (but useful) assumption — features are *conditionally independent* given the class (the “naive” assumption).

**Uses:**
- Spam detection  
- Text classification  
- Medical diagnosis problems  

---

## Review of Probability

### Independent Events
Example: rolling a fair die.  
Outcomes (1..6) are independent — probability of any face (e.g., 1) is **1/6**.  
If events are independent , the probability of A and B:  
\[
P(A/B) = P(A) * P(B)
\]

### Dependent Events & Conditional Probability
Example: marbles in a bag — 3 red, 2 green (5 total).  
- First draw: \( P(red) = 3/5 \)
- If a red marble is removed, total left = 4 → \( P(green second) = 2/4 = 1/2 \)

Conditional probability:  
\[
P(B/A){Probability of B given A} = P(B)*P(A/B)
\]

---

## Bayes’ Theorem (Core Idea)

From conditional probability symmetry:
\[
P(A/B) = P(B/A)
\]
Therefore:

\[
P(A/B) = {P(A) * P(B/A)}/{P(B)}
\]

This is **Bayes’ theorem** — it lets us *flip* conditional probabilities using prior information.

---

## Applying Bayes to Classification

Let:
- \( Y \) = class label (e.g., Yes/No)
- \( X = (X_1, X_2, …, X_n) \) = features

We want:
\[
P(Y/X) = {P(Y) * P(X|Y)}/{P(X)}
\]

Since \( P(X) \) is same for all classes, we cancel it.

---

## Example — “Play Tennis” Dataset

| Day | Outlook  | Temperature | Humidity | Wind  | Play |
|-----|-----------|-------------|-----------|-------|------|
| D1  | Sunny     | Hot         | High      | Weak  | No   |
| D2  | Sunny     | Hot         | High      | Strong| No   |
| D3  | Overcast  | Hot         | High      | Weak  | Yes  |
| D4  | Rain      | Mild        | High      | Weak  | Yes  |
| D5  | Rain      | Cool        | Normal    | Weak  | Yes  |
| D6  | Rain      | Cool        | Normal    | Strong| No   |
| D7  | Overcast  | Cool        | Normal    | Strong| Yes  |
| D8  | Sunny     | Mild        | High      | Weak  | No   |
| D9  | Sunny     | Cool        | Normal    | Weak  | Yes  |
| D10 | Rain      | Mild        | Normal    | Weak  | Yes  |
| D11 | Sunny     | Mild        | Normal    | Strong| Yes  |
| D12 | Overcast  | Mild        | High      | Strong| Yes  |
| D13 | Overcast  | Hot         | Normal    | Weak  | Yes  |
| D14 | Rain      | Mild        | High      | Strong| No   |

**Total Records = 14**  
Play = Yes → 9, Play = No → 5

---

## Step 1 — Compute Class Priors

\[
P(Yes) = {9}/{14} = 0.6429
\]
\[
P(No) = {5}/{14} = 0.3571
\]

---

## Step 2 — Conditional Probabilities

### a) Outlook
<pre>
| Outlook  | Yes | No | P(value | Yes) | P(value | No) |
|-----------|-----|----|---------------|---------------|
| Sunny     | 2   | 3  | 2/9 = 0.222   | 3/5 = 0.6     |
| Overcast  | 4   | 0  | 4/9 = 0.444   | 0/5 = 0       |
| Rain      | 3   | 2  | 3/9 = 0.333   | 2/5 = 0.4     |
</pre>
### b) Temperature
<pre>
| Temperature | Yes | No | P(value | Yes) | P(value | No) |
|--------------|-----|----|----------------|----------------|
| Hot          | 2   | 2  | 2/9 = 0.222    | 2/5 = 0.4      |
| Mild         | 4   | 2  | 4/9 = 0.444    | 2/5 = 0.4      |
| Cool         | 3   | 1  | 3/9 = 0.333    | 1/5 = 0.2      |
</pre>
### c) Humidity
<pre>
| Humidity | Yes | No | P(value | Yes) | P(value | No) |
|-----------|-----|----|----------------|----------------|
| High      | 3   | 4  | 3/9 = 0.333    | 4/5 = 0.8      |
| Normal    | 6   | 1  | 6/9 = 0.667    | 1/5 = 0.2      |
</pre>
### d) Wind
<pre>
| Wind   | Yes | No | P(value | Yes) | P(value | No) |
|--------|-----|----|----------------|----------------|
| Weak   | 6   | 2  | 6/9 = 0.667    | 2/5 = 0.4      |
| Strong | 3   | 3  | 3/9 = 0.333    | 3/5 = 0.6      |
</pre>
---

## Step 3 — Example Predictions

### (a) **Sunny, Hot, High, Weak**

\[
P(Yes) (0.222)*(0.222)*(0.333)*(0.667) = 0.00737
\]

\[
P(No) (0.6)*(0.4)*(0.8)(0.4) = 0.0274
\]

Normalize:

\[
Yes = {0.00737}/{0.00737+0.0274} = 0.212
\]

\[
No = 1-0.212 = 0.788
\]

---

### (b) **Overcast, Mild, High, Strong**

\[
P(Yes) (0.444)*(0.444)*(0.333)8(0.333) = 0.0147
\]

\[
P(No) (0)*(0.4)*(0.8)*(0.6) = 0
\]

Normalize → **Yes = 1.0 → Predict Yes**

---


## Pros and Cons

**Pros**
- Very fast to train and predict  
- Works with small and high-dimensional data  
- Simple, interpretable, robust

**Cons**
- Independence assumption rarely true  
- Zero probability issue (needs smoothing)  
- Doesn’t model interactions

---

**Examples:**
- (Sunny, Hot) → Predict **No (73%)**
- (Overcast, Mild) → Predict **Yes (100%)**

---