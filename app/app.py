from flask import Flask, jsonify, request
from app.ocr_utils import extract_text
from app.llm_utils import generate_json

app = Flask(__name__)


@app.route("/extract", methods=["POST"])
def extract():
    try:
        data = request.json

        text = extract_text(data["file"])
        parsed_text = generate_json(text)

        return parsed_text

    except Exception as e:
        return jsonify({"error": str(e)}), 500
