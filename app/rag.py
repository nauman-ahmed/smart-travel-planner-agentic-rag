import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="data/chroma")
collection = client.get_or_create_collection("travel_knowledge")

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def add_documents(docs):
    for i, doc in enumerate(docs):
        emb = embedding_model.encode(doc["content"]).tolist()
        collection.add(
            ids=[f"{doc['destination']}_{i}"],
            embeddings=[emb],
            documents=[doc["content"]],
            metadatas=[{"destination": doc["destination"]}]
        )

def search_knowledge(query, n_results=5):
    emb = embedding_model.encode(query).tolist()
    results = collection.query(
        query_embeddings=[emb],
        n_results=n_results
    )
    return results