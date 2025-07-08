from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    try:
        connection = mysql.connector.connect(
            host='db',
            user='root',
            password='root',
            database='testdb'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()
        return f"Hello from Flask! MySQL time: {result[0]}"
    except Exception as e:
        return f"Database error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
