import smtplib
import random

# Данные для SMTP (замени своими)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = "your@email.com"
PASSWORD = "yourpassword"

def send_verification_email(user_email, code):
    subject = "Код подтверждения"
    body = f"Ваш код подтверждения: {code}"
    message = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, user_email, message)
        server.quit()
        print(f"Код {code} отправлен на {user_email}")
    except Exception as e:
        print("Ошибка отправки:", e)

# Тест
email = "user@example.com"
verification_code = random.randint(100000, 999999)
send_verification_email(email, verification_code)

import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Получаем новых юзеров без верификации
cursor.execute("SELECT email FROM users WHERE is_verified = 0")
users = cursor.fetchall()

for user in users:
    email = user[0]
    code = random.randint(100000, 999999)
    send_verification_email(email, code)
    
    # Сохраняем код в базе
    cursor.execute("UPDATE users SET verify_code = ? WHERE email = ?", (code, email))
    conn.commit()

conn.close()

