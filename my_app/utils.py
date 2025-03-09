import tensorflow as tf
import numpy as np
from PIL import Image

# โหลดโมเดลเพียงครั้งเดียวตอนเริ่มต้น
model = tf.keras.models.load_model('D:/study/241-252/Leukemia-Classification/models/model01.h5')

def process_image(uploaded_file):
    try:
        # เปิดไฟล์ที่อัปโหลดโดยใช้ PIL
        image = Image.open(uploaded_file.stream)

        # Resize และ Normalize ภาพ
        image = image.resize((256, 256))  # ปรับขนาดภาพให้ตรงกับโมเดล
        img_array = np.array(image) / 255.0  # Normalize ค่า
        img_array = np.expand_dims(img_array, axis=0)  # เพิ่ม batch dimension

        # ใช้โมเดลทำนายผล
        prediction = model.predict(img_array)

        # แยก class ที่ได้
        predicted_class = "HEM" if prediction[0][0] > 0.5 else "ALL"
        probability = prediction[0][0] if predicted_class == "HEM" else 1 - prediction[0][0]

        return {"class": predicted_class, "probability": f"{probability:.4f}"}
    except Exception as e:
        return {"error": str(e)}
