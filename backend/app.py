from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()
app = Flask(__name__)
CORS(app) 

# THIS IS BAD PRACTICE, DO NOT PUT API KEY OUTSIDE OF ENVIRONMENT VARIABLE FILES
# REFER TO THE DOCUMENTS TO COMPLETE THE PROJECT
CTA_API_KEY = os.getenv("CTA_KEY_TRAIN")

@app.route("/")
def get_cta_trains():
    """
    Fetches real-time train data from CTA API and returns JSON.
    """
    url = f"http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={CTA_API_KEY}&mapid=40790&outputType=JSON"
    
    try:
        response = requests.get(url)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
    