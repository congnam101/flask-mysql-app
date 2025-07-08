from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    try:
        connection = pymysql.connect(
            host='db',
            user='root',
            password='root',
            database='mydb'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT 'Connected to MySQL!'")
        result = cursor.fetchone()
        return render_template("index.html", message=result[0])
    except Exception as e:
        return f"Database connection failed: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
