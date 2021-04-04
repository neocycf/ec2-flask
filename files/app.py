from flask import Flask
import mysql.connector

app = Flask(__name__)
 
@app.route("/")
def hello():
    query_db() 
    return "Welcome to Python Flask App!\n"

def query_db():
    cnx = mysql.connector.connect(user='root', password=None,
                              host='127.0.0.1'
                              )
    cursor = cnx.cursor()

    query_data = ("SELECT * FROM mydb.product_versions LIMIT 1")
    
    cursor.execute(query_data)

    for (_, name, version) in cursor:
        print(name + ': ' + version)
    
    cnx.close()


if __name__ == "__main__":
    app.run()

