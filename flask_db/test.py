from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

class Database:
    def __init__(self):
        host = "localhost"
        user = "Sujay"
        password = "laferrar1"
        db = "mydatabase"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()
        
    def list_customers(self):
        self.cur.execute("SELECT * FROM customers")
        self.con.commit()
        result = self.cur.fetchall()
        return result
    
    def insert_customers(self, fname, add, id):
        sql = 'insert into customers(name, address, id) values (%s, %s, %s)'
        val = (fname, add, id)
        self.cur.execute(sql, val)
        self.con.commit()

db = Database()

@app.route('/', methods=['POST', 'GET'])
def employees():
    def db_query():
        emps = db.list_customers()
        return emps
    res = db_query()
    return render_template('test.html', result=res, content_type='application/json')

@app.route('/data', methods=['POST', 'GET'])
def insertion():
    if request.method == 'POST':
        fname = request.form['firstname']
        add = request.form['address']
        id = request.form['id']
        db.insert_customers(fname, add, id)
        return render_template('form.html', fname=fname, add=add, id=id)
    else:
        return render_template('form.html')

if __name__=='__main__':
    app.run(debug=True)