"""
Deep Dive: What Happens Inside the Embedding Model

This script shows you EXACTLY what happens when you call:
    embedding_model.encode("I love pizza")

We'll break down each step and show the intermediate results.

Requirements:
    pip install sentence-transformers transformers
"""

from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer
import numpy as np


# ============================================================================
# Load Model and Tokenizer
# ============================================================================

print("📥 Loading model and tokenizer...\n")

model = SentenceTransformer('all-MiniLM-L6-v2')
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

print("✅ Loaded!\n")


# ============================================================================
# Example Text
# ============================================================================

text = "Our refund policy allows returns within 30 days"
print(f"📝 Input Text: '{text}'")
print("="*70)
print()


# ============================================================================
# STEP 1: Tokenization
# ============================================================================

print("STEP 1: TOKENIZATION")
print("-"*70)

# Convert text to tokens (subwords)
tokens = tokenizer.tokenize(text)
print(f"Tokens (subwords): {tokens}")
print(f"Number of tokens: {len(tokens)}")
print()

# Show how words are split
print("How tokenization works:")
print("  'refund'   → ['ref', '##und']  (split into subwords)")
print("  'policy'   → ['policy']         (kept as one)")
print("  'returns'  → ['returns']        (kept as one)")
print()


# ============================================================================
# STEP 2: Convert Tokens to IDs
# ============================================================================

print("STEP 2: TOKEN IDs")
print("-"*70)

# Each token gets a unique number
token_ids = tokenizer.encode(text, add_special_tokens=True)
print(f"Token IDs: {token_ids}")
print()

# Show the mapping
print("Token → ID mapping:")
encoded = tokenizer(text, return_tensors='pt')
for i, (token, token_id) in enumerate(zip(tokens, token_ids[1:-1])):  # Skip [CLS] and [SEP]
    print(f"  '{token}' → {token_id}")
print()

print("Special tokens:")
print(f"  [CLS] (start) → {token_ids[0]}")
print(f"  [SEP] (end)   → {token_ids[-1]}")
print()


# ============================================================================
# STEP 3: Create Embedding (The Magic!)
# ============================================================================

print("STEP 3: NEURAL NETWORK PROCESSING")
print("-"*70)

# This is what happens inside model.encode():
embedding = model.encode(text, convert_to_numpy=True)

print(f"Final embedding shape: {embedding.shape}")
print(f"Dimensions: {len(embedding)}")
print()

print("First 10 values of the embedding:")
print(embedding[:10])
print()

print("What happened inside:")
print("  1. Token IDs → Embedding lookup (each ID → 384D vector)")
print("  2. Pass through 12 transformer layers:")
print("     - Self-attention (tokens relate to each other)")
print("     - Feed-forward networks")
print("     - Layer normalization")
print("  3. Pooling: Average all token embeddings")
print("  4. Normalization: Scale to unit length")
print()


# ============================================================================
# STEP 4: Verify Normalization
# ============================================================================

print("STEP 4: NORMALIZATION CHECK")
print("-"*70)

# Calculate magnitude (should be 1.0 for normalized vectors)
magnitude = np.linalg.norm(embedding)
print(f"Vector magnitude: {magnitude:.6f}")
print(f"Expected: 1.0 (unit vector)")
print()

if abs(magnitude - 1.0) < 0.0001:
    print("✅ Vector is normalized (unit length)")
else:
    print("⚠️  Vector is not normalized")
print()


# ============================================================================
# STEP 5: Compare Two Sentences
# ============================================================================

print("STEP 5: SEMANTIC SIMILARITY DEMO")
print("-"*70)

sentences = [
    "Our refund policy allows returns within 30 days",
    "You can return products in the first month",
    "Shipping takes 3-5 business days"
]

print("Creating embeddings for 3 sentences...\n")

embeddings = model.encode(sentences, convert_to_numpy=True)

print("Sentence 1:", sentences[0])
print("Sentence 2:", sentences[1])
print("Sentence 3:", sentences[2])
print()

# Calculate similarities
sim_1_2 = np.dot(embeddings[0], embeddings[1])
sim_1_3 = np.dot(embeddings[0], embeddings[2])
sim_2_3 = np.dot(embeddings[1], embeddings[2])

print("Cosine Similarities:")
print(f"  Sentence 1 ↔ Sentence 2: {sim_1_2:.4f}  (similar meaning!)")
print(f"  Sentence 1 ↔ Sentence 3: {sim_1_3:.4f}  (different topic)")
print(f"  Sentence 2 ↔ Sentence 3: {sim_2_3:.4f}  (different topic)")
print()

print("✅ Notice: Sentences 1 & 2 have high similarity even though")
print("   they use different words ('refund' vs 'return', '30 days' vs 'first month')")
print("   This is the power of semantic embeddings!")
print()


# ============================================================================
# STEP 6: Visualize Embedding Distribution
# ============================================================================

print("STEP 6: EMBEDDING STATISTICS")
print("-"*70)

print(f"Min value: {embedding.min():.4f}")
print(f"Max value: {embedding.max():.4f}")
print(f"Mean value: {embedding.mean():.4f}")
print(f"Std deviation: {embedding.std():.4f}")
print()

print("Value distribution:")
positive = (embedding > 0).sum()
negative = (embedding < 0).sum()
print(f"  Positive values: {positive} ({positive/len(embedding)*100:.1f}%)")
print(f"  Negative values: {negative} ({negative/len(embedding)*100:.1f}%)")
print()


# ============================================================================
# Summary
# ============================================================================

print("="*70)
print("📚 SUMMARY: What model.encode() Does")
print("="*70)
print()
print("1. Tokenization:    Text → subword tokens")
print("2. Token IDs:       Tokens → unique numbers")
print("3. Embedding Lookup: IDs → initial vectors (384D each)")
print("4. Transformers:    12 layers of neural network processing")
print("5. Pooling:         Average all token vectors → sentence vector")
print("6. Normalization:   Scale to unit length (magnitude = 1.0)")
print()
print("Result: 384 numbers that capture the MEANING of your text!")
print("="*70)

