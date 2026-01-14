#!/usr/bin/env python3
"""
Test script to verify RAG Learning installation
Run this to make sure everything is working!
"""

def test_imports():
    """Test that all required packages can be imported"""
    print("🔍 Testing package imports...")
    
    try:
        import torch
        print("✅ PyTorch:", torch.__version__)
    except ImportError as e:
        print("❌ PyTorch import failed:", e)
        return False
    
    try:
        import transformers
        print("✅ Transformers:", transformers.__version__)
    except ImportError as e:
        print("❌ Transformers import failed:", e)
        return False
    
    try:
        import chromadb
        print("✅ ChromaDB:", chromadb.__version__)
    except ImportError as e:
        print("❌ ChromaDB import failed:", e)
        return False
    
    try:
        from sentence_transformers import SentenceTransformer
        print("✅ Sentence Transformers: OK")
    except ImportError as e:
        print("❌ Sentence Transformers import failed:", e)
        return False
    
    try:
        import fastapi
        print("✅ FastAPI:", fastapi.__version__)
    except ImportError as e:
        print("❌ FastAPI import failed:", e)
        return False
    
    return True


def test_basic_functionality():
    """Test basic RAG functionality"""
    print("\n🧪 Testing basic functionality...")
    
    try:
        # Test embeddings
        from sentence_transformers import SentenceTransformer
        
        print("  Loading embedding model (this may take a moment)...")
        model = SentenceTransformer('all-MiniLM-L6-v2')
        
        print("  Creating embeddings...")
        texts = ["Hello world", "RAG is awesome"]
        embeddings = model.encode(texts)
        
        print(f"  ✅ Created {len(embeddings)} embeddings of dimension {len(embeddings[0])}")
        
        # Test ChromaDB
        import chromadb
        from chromadb.config import Settings
        
        print("  Testing ChromaDB...")
        client = chromadb.Client(Settings(anonymized_telemetry=False))
        collection = client.create_collection("test")
        
        collection.add(
            documents=texts,
            ids=["1", "2"]
        )
        
        results = collection.query(query_texts=["greeting"], n_results=1)
        print(f"  ✅ ChromaDB query returned: {results['documents'][0]}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Functionality test failed: {e}")
        return False


def main():
    """Run all tests"""
    print("=" * 60)
    print("🚀 RAG Learning Installation Test")
    print("=" * 60)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed!")
        print("Try running: pip install -r requirements.txt")
        return
    
    # Test functionality
    if not test_basic_functionality():
        print("\n❌ Functionality tests failed!")
        return
    
    print("\n" + "=" * 60)
    print("✅ All tests passed! Your installation is working!")
    print("=" * 60)
    print("\n📚 Next steps:")
    print("  1. Read QUICKSTART.md")
    print("  2. Go to lessons/lesson1_embeddings/")
    print("  3. Run: python basic_embeddings.py")
    print("\nHappy learning! 🎓")


if __name__ == "__main__":
    main()

