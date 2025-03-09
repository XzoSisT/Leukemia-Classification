# Secret Key สำหรับเซสชันและความปลอดภัย
SECRET_KEY = 'your-very-secure-secret-key'

# โฟลเดอร์เก็บไฟล์ที่อัปโหลด
UPLOAD_FOLDER = 'uploads/'

# จำกัดขนาดไฟล์ที่สามารถอัปโหลดได้ (16 MB)
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# ตั้งค่า URI ของฐานข้อมูล (ตัวอย่างเป็น SQLite)
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
