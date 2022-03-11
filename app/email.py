# from flask import Flask, jsonify
# from flask_mail import Mail, Message
# import os

# from app import app

# mail_setting = {
#     "MAIL_SERVER": 'smtp.gmail.com',
#     "MAIL_PORT": "587",
#     "MAIL_USE_TLS": False,
#     "MAIL_USE_SSL": True,
#     "MAIL_USERNAME": os.environ.get('SENDER_EMAIL'),
#     "MAIL_PASSWORD": os.environ.get('EMAIL_PWD')
    
# }
# app.config.update(mail_setting)
# mail = Mail(app)