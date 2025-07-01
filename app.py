from flask import Flask, request, render_template, redirect
import mysql.connector
import time

app = Flask(__name__)

# Kết nối MySQL có retry khi khởi động
for i in range(10):
    try:
        db = mysql.connector.connect(
            host="db",
            user="root",
            password="123456",
            database="flaskdb"
        )
        break
    except mysql.connector.Error as e:
        print(f"⏳ Waiting for MySQL... retrying ({i+1}/10)")
        time.sleep(3)
else:
    print("❌ Failed to connect to database after retries.")
    exit(1)

cursor = db.cursor()

# ✅ Tạo bảng nếu chưa tồn tại
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    );
''')
db.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        db.commit()
        return redirect('/users')
    return render_template('index.html')

@app.route('/users')
def users():
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    return render_template('users.html', users=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

