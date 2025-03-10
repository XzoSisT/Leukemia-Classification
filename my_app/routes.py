from flask import Blueprint, render_template, request, jsonify
from .utils import process_image  # Import the corrected function

# Create Blueprint
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

    file = request.files['file']
    result = process_image(file)
    return render_template('upload.html', prediction=result)

