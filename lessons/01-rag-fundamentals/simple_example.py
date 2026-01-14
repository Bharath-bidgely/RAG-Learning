"""
Simple RAG Example - Your First RAG System in ~100 Lines

This demonstrates the core RAG concept:
1. Store documents with their "meaning" (embeddings)
2. Find relevant documents by meaning (semantic search)
3. Use LLM to generate answer from relevant context

No fancy frameworks - just pure Python to understand the concept.
"""

import numpy as np
from typing import List, Tuple


# ============================================================================
# STEP 1: Sample Documents (Imagine these are from your database)
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
# STEP 2: Simple Embedding Function (Simulated)
# ============================================================================

def simple_embedding(text: str) -> np.ndarray:
    """
    Create a simple embedding (vector representation) of text.
    
    In reality, you'd use AWS Bedrock or OpenAI for this.
    This is a SIMPLIFIED version just to demonstrate the concept.
    
    How it works:
    - Counts word frequencies
    - Creates a vector based on key terms
    - Similar texts will have similar vectors
    
    Args:
        text: Input text
        
    Returns:
        Vector (numpy array) representing the text
    """
    # Normalize text
    text = text.lower()
    
    # Key terms we care about (in real life, this would be learned)
    keywords = [
        "refund", "return", "money", "back",
        "shipping", "delivery", "ship",
        "support", "help", "contact", "customer",
        "payment", "pay", "credit", "card"
    ]
    
    # Create vector based on keyword presence
    vector = []
    for keyword in keywords:
        # Count how many times keyword appears
        count = text.count(keyword)
        vector.append(count)
    
    # Convert to numpy array and normalize
    vector = np.array(vector, dtype=float)
    
    # Normalize to unit length (important for similarity calculation)
    norm = np.linalg.norm(vector)
    if norm > 0:
        vector = vector / norm
    
    return vector


# ============================================================================
# STEP 3: Calculate Similarity Between Vectors
# ============================================================================

def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """
    Calculate how similar two vectors are (0 = different, 1 = identical).
    
    This is called "cosine similarity" - it measures the angle between vectors.
    
    Args:
        vec1: First vector
        vec2: Second vector
        
    Returns:
        Similarity score between 0 and 1
    """
    # Dot product of normalized vectors = cosine similarity
    similarity = np.dot(vec1, vec2)
    return float(similarity)


# ============================================================================
# STEP 4: Build Simple Vector Database (In-Memory)
# ============================================================================

class SimpleVectorDB:
    """
    A simple in-memory vector database.
    
    In production, you'd use ChromaDB, Pinecone, or AWS OpenSearch.
    This demonstrates the core concept.
    """
    
    def __init__(self):
        self.documents = []
        self.embeddings = []
    
    def add_document(self, doc: dict):
        """Add a document and its embedding to the database."""
        # Create embedding for the document
        embedding = simple_embedding(doc["content"])
        
        # Store both
        self.documents.append(doc)
        self.embeddings.append(embedding)
        
        print(f"✅ Added document {doc['id']}: {doc['content'][:50]}...")
    
    def search(self, query: str, top_k: int = 2) -> List[Tuple[dict, float]]:
        """
        Search for documents similar to the query.
        
        Args:
            query: Search query
            top_k: Number of results to return
            
        Returns:
            List of (document, similarity_score) tuples
        """
        # Create embedding for query
        query_embedding = simple_embedding(query)
        
        # Calculate similarity with all documents
        similarities = []
        for i, doc_embedding in enumerate(self.embeddings):
            similarity = cosine_similarity(query_embedding, doc_embedding)
            similarities.append((self.documents[i], similarity))
        
        # Sort by similarity (highest first)
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        # Return top K results
        return similarities[:top_k]


# ============================================================================
# STEP 5: Simple RAG System
# ============================================================================

def simple_rag(question: str, vector_db: SimpleVectorDB) -> str:
    """
    Answer a question using RAG.
    
    Steps:
    1. Search for relevant documents
    2. Build context from top results
    3. Generate answer (simulated - in reality, use LLM)
    
    Args:
        question: User's question
        vector_db: Vector database with documents
        
    Returns:
        Generated answer
    """
    print(f"\n🔍 Question: {question}")
    print("=" * 70)
    
    # STEP 1: Retrieve relevant documents
    results = vector_db.search(question, top_k=2)
    
    print("\n📚 Retrieved Documents:")
    context_parts = []
    for doc, score in results:
        print(f"  - [Score: {score:.3f}] {doc['content'][:60]}...")
        context_parts.append(doc["content"])
    
    # STEP 2: Build context
    context = "\n\n".join(context_parts)
    
    # STEP 3: Generate answer (simulated)
    # In reality, you'd send this to AWS Bedrock Claude:
    # prompt = f"Context:\n{context}\n\nQuestion: {question}\n\nAnswer:"
    # answer = bedrock_client.generate(prompt)
    
    print(f"\n💡 Answer: Based on the retrieved context...")
    print(f"   Context: {context[:100]}...")
    
    return context


# ============================================================================
# MAIN: Run the Example
# ============================================================================

if __name__ == "__main__":
    print("🚀 Simple RAG System Demo")
    print("=" * 70)
    
    # Create vector database
    db = SimpleVectorDB()
    
    # Add all documents
    print("\n📥 Indexing documents...")
    for doc in DOCUMENTS:
        db.add_document(doc)
    
    # Ask questions
    questions = [
        "How do I return a product?",
        "What payment methods do you accept?",
        "How can I contact support?",
    ]
    
    for question in questions:
        simple_rag(question, db)
        print()

