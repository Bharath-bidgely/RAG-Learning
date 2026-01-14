"""
RAG Example with REAL Hugging Face Embeddings

This version uses actual Sentence Transformers from Hugging Face
to show you how embeddings work in production.

Requirements:
    pip install sentence-transformers

Model used: all-MiniLM-L6-v2
- Size: 80MB (small, fast)
- Dimensions: 384
- Quality: Good for most use cases
- Speed: Very fast
- Cost: FREE!
"""

import numpy as np
from typing import List, Tuple
from sentence_transformers import SentenceTransformer


# ============================================================================
# STEP 1: Load Real Embedding Model from Hugging Face
# ============================================================================

print("📥 Loading embedding model from Hugging Face...")
print("   Model: all-MiniLM-L6-v2 (384 dimensions)")
print("   This will download ~80MB on first run...\n")

# Load the model (downloads automatically from Hugging Face)
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

print("✅ Model loaded successfully!\n")


# ============================================================================
# STEP 2: Sample Documents
# ============================================================================

DOCUMENTS = [
    {
        "id": 1,
        "content": "Our refund policy allows customers to return products within 30 days "
                   "of purchase for a full refund. Items must be in original condition.",
        "metadata": {"category": "policy", "topic": "refunds"}
    },
    {
        "id": 2,
        "content": "Shipping takes 3-5 business days for standard delivery. "
                   "Express shipping is available for an additional fee and takes 1-2 days.",
        "metadata": {"category": "policy", "topic": "shipping"}
    },
    {
        "id": 3,
        "content": "Customer support is available Monday through Friday, 9 AM to 5 PM EST. "
                   "You can reach us by phone, email, or live chat on our website.",
        "metadata": {"category": "support", "topic": "contact"}
    },
    {
        "id": 4,
        "content": "We accept all major credit cards, PayPal, and Apple Pay. "
                   "Payment is processed securely through our encrypted payment gateway.",
        "metadata": {"category": "policy", "topic": "payment"}
    },
]


# ============================================================================
# STEP 3: Create Real Embeddings with Hugging Face
# ============================================================================

def create_embedding(text: str) -> np.ndarray:
    """
    Create a REAL embedding using Hugging Face Sentence Transformers.
    
    What happens inside:
    1. Tokenization: Text → tokens (["Our", "refund", "policy", ...])
    2. Token IDs: Tokens → numbers ([2256, 25278, 3343, ...])
    3. Neural Network: 12 transformer layers process the tokens
    4. Pooling: Average all token embeddings → sentence embedding
    5. Normalization: Scale to unit length
    
    Args:
        text: Input text
        
    Returns:
        384-dimensional vector representing the text meaning
    """
    # This single line does ALL the magic:
    # - Tokenization
    # - Embedding lookup
    # - Neural network processing (12 layers!)
    # - Pooling
    # - Normalization
    embedding = embedding_model.encode(text, convert_to_numpy=True)
    
    return embedding


# ============================================================================
# STEP 4: Cosine Similarity (Same as Before)
# ============================================================================

def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """
    Calculate cosine similarity between two vectors.
    
    Formula: cos(θ) = (A · B) / (||A|| × ||B||)
    
    Since our vectors are already normalized (unit length),
    this simplifies to just the dot product!
    """
    similarity = np.dot(vec1, vec2)
    return float(similarity)


# ============================================================================
# STEP 5: Vector Database (In-Memory)
# ============================================================================

class VectorDB:
    """Simple in-memory vector database using real embeddings."""
    
    def __init__(self):
        self.documents = []
        self.embeddings = []
    
    def add_document(self, doc: dict):
        """Add a document and create its embedding."""
        # Create REAL embedding using Hugging Face
        embedding = create_embedding(doc["content"])
        
        # Store both
        self.documents.append(doc)
        self.embeddings.append(embedding)
        
        print(f"✅ Added document {doc['id']}: {doc['content'][:50]}...")
        print(f"   Embedding shape: {embedding.shape} (384 dimensions)")
        print(f"   First 5 values: {embedding[:5]}")
        print()
    
    def search(self, query: str, top_k: int = 2) -> List[Tuple[dict, float]]:
        """Search for documents similar to the query."""
        # Create embedding for query
        query_embedding = create_embedding(query)
        
        print(f"🔍 Query embedding shape: {query_embedding.shape}")
        print(f"   First 5 values: {query_embedding[:5]}\n")
        
        # Calculate similarity with all documents
        similarities = []
        for i, doc_embedding in enumerate(self.embeddings):
            similarity = cosine_similarity(query_embedding, doc_embedding)
            similarities.append((self.documents[i], similarity))
        
        # Sort by similarity (highest first)
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        return similarities[:top_k]


# ============================================================================
# STEP 6: RAG System
# ============================================================================

def rag_query(question: str, vector_db: VectorDB) -> str:
    """Answer a question using RAG."""
    print(f"\n{'='*70}")
    print(f"❓ Question: {question}")
    print(f"{'='*70}\n")
    
    # Retrieve relevant documents
    results = vector_db.search(question, top_k=2)
    
    print("📚 Retrieved Documents:")
    context_parts = []
    for doc, score in results:
        print(f"  - [Score: {score:.4f}] {doc['content'][:60]}...")
        context_parts.append(doc["content"])
    
    # Build context
    context = "\n\n".join(context_parts)
    
    print(f"\n💡 In a real system, we'd send this to an LLM:")
    print(f"   Prompt: 'Based on: {context[:100]}... Answer: {question}'")
    print()
    
    return context


# ============================================================================
# MAIN: Run the Example
# ============================================================================

if __name__ == "__main__":
    print("🚀 RAG System with Real Hugging Face Embeddings")
    print("="*70)
    print()
    
    # Create vector database
    db = VectorDB()
    
    # Add all documents
    print("📥 Indexing documents with real embeddings...\n")
    for doc in DOCUMENTS:
        db.add_document(doc)
    
    # Ask questions
    questions = [
        "How do I return a product?",
        "What payment methods do you accept?",
        "How can I contact support?",
    ]
    
    for question in questions:
        rag_query(question, db)
    
    print("\n" + "="*70)
    print("✅ Done! Notice how the similarity scores are more accurate")
    print("   with real embeddings compared to the simple keyword-based version.")
    print("="*70)

