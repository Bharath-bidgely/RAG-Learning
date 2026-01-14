# 📐 Math Cheatsheet - Quick Reference

Quick formulas and concepts for RAG systems.

---

## 🔢 Cosine Similarity Formula

```
cos(θ) = (A · B) / (||A|| × ||B||)

Where:
  A · B     = Dot product (sum of element-wise multiplication)
  ||A||     = Magnitude of vector A = √(a₁² + a₂² + ... + aₙ²)
  ||B||     = Magnitude of vector B = √(b₁² + b₂² + ... + bₙ²)
  θ (theta) = Angle between vectors
```

**Result Range**: -1 to +1
- `1.0` = Identical (0° angle)
- `0.5` = Somewhat similar (60° angle)
- `0.0` = Unrelated (90° angle)
- `-1.0` = Opposite (-180° angle)

---

## 📊 Step-by-Step Calculation

Given:
```
A = [0.8, 0.6, 0.9]
B = [0.7, 0.5, 0.8]
```

### Step 1: Dot Product
```
A · B = (0.8 × 0.7) + (0.6 × 0.5) + (0.9 × 0.8)
      = 0.56 + 0.30 + 0.72
      = 1.58
```

### Step 2: Magnitude of A
```
||A|| = √(0.8² + 0.6² + 0.9²)
      = √(0.64 + 0.36 + 0.81)
      = √1.81
      = 1.345
```

### Step 3: Magnitude of B
```
||B|| = √(0.7² + 0.5² + 0.8²)
      = √1.38
      = 1.175
```

### Step 4: Final Similarity
```
cos(θ) = 1.58 / (1.345 × 1.175)
       = 1.58 / 1.580
       = 0.9999 ≈ 1.0
```

---

## 🧮 Trigonometry Quick Reference

```
        |\
        | \  c (Hypotenuse)
      a |  \
        |   \
        |____\
          b

sin(θ) = a/c  (Opposite / Hypotenuse)
cos(θ) = b/c  (Adjacent / Hypotenuse)
tan(θ) = a/b  (Opposite / Adjacent)
```

### Common Values
| Angle | sin | cos | tan |
|-------|-----|-----|-----|
| 0°    | 0   | 1   | 0   |
| 45°   | 0.707 | 0.707 | 1 |
| 90°   | 1   | 0   | ∞   |

---

## 💻 Python Implementation

```python
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Example
vec1 = np.array([0.8, 0.6, 0.9])
vec2 = np.array([0.7, 0.5, 0.8])
print(cosine_similarity(vec1, vec2))  # 0.9999
```

---

## 🎯 Why Cosine (Not Euclidean Distance)?

### Euclidean Distance
```
d = √((a₁-b₁)² + (a₂-b₂)² + ...)
```
❌ Sensitive to vector length
❌ Long vectors seem "far" even if same direction

### Cosine Similarity
```
cos(θ) = (A · B) / (||A|| × ||B||)
```
✅ Only measures direction (angle)
✅ Perfect for text (meaning, not length)

---

## 📈 Text → Vector Process

```
1. Tokenization:    "I love pizza" → ["I", "love", "pizza"]
2. Token IDs:       ["I", "love", "pizza"] → [245, 1523, 8934]
3. Embeddings:      [245, 1523, 8934] → 3 vectors of 384 dims each
4. Neural Network:  Process through 12 transformer layers
5. Pooling:         Average → Final vector [0.23, 0.81, ...]
```

---

## 🔑 Key Formulas Summary

| Operation | Formula | Use Case |
|-----------|---------|----------|
| Dot Product | A · B = Σ(aᵢ × bᵢ) | Similarity component |
| Magnitude | ‖A‖ = √(Σaᵢ²) | Vector length |
| Cosine Similarity | cos(θ) = (A·B)/(‖A‖×‖B‖) | Text similarity |
| Euclidean Distance | d = √(Σ(aᵢ-bᵢ)²) | Not used in RAG |

---

**For detailed explanations, see CONCEPTS.md**

