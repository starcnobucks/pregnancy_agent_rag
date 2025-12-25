
import chromadb
client=chromadb.Client()
col=client.get_or_create_collection("pregnancy")

def retrieve(q):
    r=col.query([q],n_results=2)
    return " ".join(r["documents"][0]) if r["documents"] else ""
