from flask import Flask
from flask_cors import CORS
import os
from routes.api import api

app = Flask(__name__)
CORS(app)

# Ensure required folders exist
os.makedirs("uploads", exist_ok=True)
os.makedirs("generated_code", exist_ok=True)

# Register API routes
app.register_blueprint(api, url_prefix="/api")

@app.route("/")
def home():
    return {
        "message": "Backend for Code From Design is running!",
        "status": "success"
    }

if __name__ == "__main__":
    app.run(debug=True)
