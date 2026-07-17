from flask import Flask, jsonify

app = Flask(__name__)

VERSION = "1.0.0"


@app.get("/")
def home():
    return jsonify({"application": "Python Demo", "version": VERSION})


@app.get("/health")
def health():
    return jsonify({"status": "healthy"})


@app.get("/version")
def version():
    return jsonify({"version": VERSION})
