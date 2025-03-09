from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# สร้าง SQLAlchemy instance
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # โหลดการตั้งค่าจากไฟล์ config
    app.config.from_pyfile('instance/config.py')

    # เริ่มต้นฐานข้อมูล
    db.init_app(app)

    # ลงทะเบียน Blueprint
    from .routes import main
    app.register_blueprint(main)

    return app
