
import chromadb, os
from pypdf import PdfReader

client=chromadb.Client()
col=client.get_or_create_collection("pregnancy")

def ingest_pdfs():
    if col.count()>0: return
    path="data/raw"
    if not os.path.exists(path): return
    for f in os.listdir(path):
        r=PdfReader(os.path.join(path,f))
        for i,p in enumerate(r.pages):
            col.add([p.extract_text()],[f"{f}-{i}"])
