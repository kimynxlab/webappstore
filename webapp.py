from flask import Flask , render_template 
import mysql.connector 
import 
import os 
app = Flask(__name__)


db_config = {
    'user': os.environ['DBUSER'],
    'password': os.environ['DBPASSWORD'], 
    'host': os.environ['DBHOST'],
    'database': os.environ['DB']
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clients')
def clients():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM client")
    rows = cursor.fetchall()

    column_names = [i[0] for i in cursor.description]

    cursor.close()
    conn.close()

    return render_template('index.html', rows=rows, column_names=column_names)
     

if __name__ == "__main__": 
    app.run() 
    