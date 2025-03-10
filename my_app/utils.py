import os
import tensorflow as tf
import numpy as np
from PIL import Image
from flask import current_app
from werkzeug.utils import secure_filename

# Load the model once at the start
try:
    model = tf.keras.models.load_model('D:/study/241-252/Leukemia-Classification/models/efficientnetv2-b3-Leukemia detection-96.31.h5')
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {str(e)}")
    model = None  # Prevent the app from breaking if the model fails to load

def process_image(uploaded_file):
    try:
        # ตรวจสอบโมเดล
        if model is None:
            raise ValueError("Model not loaded successfully. Please check the model path or configuration.")

        # กำหนดโฟลเดอร์สำหรับบันทึกภาพ
        upload_folder = os.path.join(current_app.root_path, 'static/uploads')
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        # บันทึกไฟล์และทำชื่อไฟล์ให้ปลอดภัย
        filename = secure_filename(uploaded_file.filename)
        file_path = os.path.join(upload_folder, filename)
        uploaded_file.save(file_path)

        # โหลดภาพและ Preprocess
        image = Image.open(file_path).convert("RGB")
        image = image.resize((224, 224))
        img_array = np.expand_dims(image, axis=0)

        # ทำนายผลลัพธ์
        prediction = model.predict(img_array)
        print("Raw prediction:", prediction)

        # ตีความผลลัพธ์
        classes = ['ALL', 'HEM']
        index = np.argmax(prediction[0])
        klass = classes[index]
        probability = prediction[0][index] * 100

        # ส่งผลลัพธ์กลับ
        return {
            "class": klass,
            "probability": probability,
            "image_path": f"static/uploads/{filename}"
        }

    except Exception as e:
        print(f"Error during processing: {str(e)}")
        return {"error": str(e)}
