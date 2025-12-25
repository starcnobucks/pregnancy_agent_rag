
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from src.agents.router_agent import route_query
from src.rag.ingestion import ingest_pdfs
from src.tools.vector_search import retrieve

load_dotenv()
app = Flask(__name__)

ingest_pdfs()

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    q=request.json["q"]
    agent=route_query(q)
    ctx=retrieve(q)
    return jsonify(a=agent.run(q,ctx))

app.run()
