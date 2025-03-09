from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .utils import process_image

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/upload')
def upload():
    return render_template('upload.html')

@main.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    try:
        file = request.files['file']  # รับไฟล์จากฟอร์ม
        result = process_image(file)  # ส่งไฟล์ไปยังฟังก์ชัน process_image
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
