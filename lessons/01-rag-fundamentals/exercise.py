"""
Exercise 1: Build Your Own Mini RAG System

GOAL: Understand RAG by building a simple document search system.

SCENARIO:
You have a collection of product descriptions. Build a system that can
find the most relevant products based on a customer's question.

TASKS:
1. Add 3 more products to the PRODUCTS list
2. Implement the find_relevant_products() function
3. Test with different customer questions
4. Observe how semantic search works

LEARNING POINTS:
- How embeddings capture meaning
- How similarity search finds relevant content
- Why RAG is better than keyword search
"""

import numpy as np
from typing import List, Tuple


# ============================================================================
# PRODUCT DATABASE
# ============================================================================

PRODUCTS = [
    {
        "id": "P001",
        "name": "Wireless Bluetooth Headphones",
        "description": "Premium over-ear headphones with active noise cancellation, "
                      "40-hour battery life, and crystal-clear sound quality. "
                      "Perfect for music lovers and frequent travelers.",
        "price": 199.99
    },
    {
        "id": "P002",
        "name": "Smart Fitness Watch",
        "description": "Track your health and fitness with heart rate monitoring, "
                      "sleep tracking, GPS, and waterproof design. "
                      "Compatible with iOS and Android.",
        "price": 299.99
    },
    # TODO: Add 3 more products here
    # Ideas: laptop, phone case, water bottle, backpack, etc.
]


# ============================================================================
# HELPER FUNCTIONS (Already Implemented)
# ============================================================================

def create_embedding(text: str) -> np.ndarray:
    """
    Create a simple embedding for text.
    (Same as simple_example.py - already implemented)
    """
    text = text.lower()
    
    keywords = [
        "headphone", "audio", "sound", "music", "noise",
        "watch", "fitness", "health", "track", "heart",
        "laptop", "computer", "screen", "keyboard",
        "phone", "mobile", "call", "smartphone",
        "water", "bottle", "drink", "hydration",
        "bag", "backpack", "carry", "storage"
    ]
    
    vector = []
    for keyword in keywords:
        count = text.count(keyword)
        vector.append(count)
    
    vector = np.array(vector, dtype=float)
    norm = np.linalg.norm(vector)
    if norm > 0:
        vector = vector / norm
    
    return vector


def calculate_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """Calculate cosine similarity between two vectors."""
    return float(np.dot(vec1, vec2))


# ============================================================================
# YOUR TASK: Implement This Function
# ============================================================================

def find_relevant_products(
    customer_question: str,
    products: List[dict],
    top_k: int = 2
) -> List[Tuple[dict, float]]:
    """
    Find the most relevant products for a customer's question.
    
    STEPS TO IMPLEMENT:
    1. Create an embedding for the customer's question
    2. For each product:
       a. Create an embedding for the product description
       b. Calculate similarity with the question embedding
       c. Store (product, similarity_score)
    3. Sort products by similarity (highest first)
    4. Return top K products
    
    Args:
        customer_question: What the customer is looking for
        products: List of product dictionaries
        top_k: Number of products to return
        
    Returns:
        List of (product, similarity_score) tuples, sorted by relevance
        
    HINT: Look at simple_example.py SimpleVectorDB.search() for reference
    """
    
    # TODO: Your code here
    # Step 1: Create embedding for the question
    question_embedding = None  # Replace with actual code
    
    # Step 2: Calculate similarities
    results = []  # List of (product, score) tuples
    
    # TODO: Loop through products and calculate similarities
    
    # Step 3: Sort by similarity
    # TODO: Sort results
    
    # Step 4: Return top K
    return results[:top_k]


# ============================================================================
# TEST YOUR IMPLEMENTATION
# ============================================================================

def test_product_search():
    """Test your implementation with different questions."""
    
    print("🛍️  Product Search System")
    print("=" * 70)
    
    # Test questions
    test_questions = [
        "I need something for listening to music while traveling",
        "What can help me track my daily exercise?",
        "I'm looking for a device to monitor my health",
    ]
    
    for question in test_questions:
        print(f"\n❓ Customer Question: {question}")
        print("-" * 70)
        
        # Find relevant products
        results = find_relevant_products(question, PRODUCTS, top_k=2)
        
        # Display results
        if results:
            print("📦 Recommended Products:")
            for i, (product, score) in enumerate(results, 1):
                print(f"\n  {i}. {product['name']} (Relevance: {score:.3f})")
                print(f"     {product['description'][:80]}...")
                print(f"     Price: ${product['price']}")
        else:
            print("❌ No results found. Check your implementation!")


# ============================================================================
# BONUS CHALLENGE (Optional)
# ============================================================================

def bonus_challenge():
    """
    BONUS: Improve the search system
    
    Try these enhancements:
    1. Add price filtering (e.g., "under $200")
    2. Add category filtering (e.g., "electronics")
    3. Combine multiple product fields (name + description)
    4. Implement a minimum similarity threshold
    
    This will prepare you for Lesson 5 (Semantic Search)!
    """
    pass


# ============================================================================
# RUN THE TESTS
# ============================================================================

if __name__ == "__main__":
    # First, add your 3 products to the PRODUCTS list above
    
    # Then run the test
    test_product_search()
    
    # Optional: Try the bonus challenge
    # bonus_challenge()


# ============================================================================
# EXPECTED OUTPUT (After Implementation)
# ============================================================================
"""
When correctly implemented, you should see output like:

🛍️  Product Search System
======================================================================

❓ Customer Question: I need something for listening to music while traveling
----------------------------------------------------------------------
📦 Recommended Products:

  1. Wireless Bluetooth Headphones (Relevance: 0.850)
     Premium over-ear headphones with active noise cancellation...
     Price: $199.99

  2. Smart Fitness Watch (Relevance: 0.120)
     Track your health and fitness with heart rate monitoring...
     Price: $299.99

(Notice how the headphones have much higher relevance!)
"""

