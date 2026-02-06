from flask import Blueprint, request, jsonify
import os
from werkzeug.utils import secure_filename
from services.autodev_service import generate_code_from_design

api = Blueprint("api", __name__)

UPLOAD_FOLDER = "uploads"

@api.route("/upload", methods=["POST"])
def upload_design():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Call AutoDev AI service (simulated for now)
    result = generate_code_from_design(filepath)

    return jsonify({
        "message": "File uploaded successfully",
        "filename": filename,
        "generated_code": result
    })
