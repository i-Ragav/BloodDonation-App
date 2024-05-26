from flask import Flask, make_response, render_template, request, redirect, jsonify
import mysql.connector

app = Flask(__name__, static_folder='./static')

def get_db_connection():
    with open('admin.csv') as f:
        contents = [ i.split(",") for i in f.read().split('\n')]
        admin_data = { i[0]:i[1] for i in contents }

    return mysql.connector.connect(
        host = admin_data["host"],
        user = admin_data["user"],
        password = admin_data["password"],
        database = admin_data["database"],
        port = admin_data["port"],
    )

@app.route('/add_donor', methods=['POST'])
def add_donor():
    req = request.json
    name = req['name']
    age = req['age']
    gender = req['gender']
    blood_type = req['bloodType']
    contact_info = req['contactInfo']
    last_donation_date = req['lastDonationDate']
    medical_history = req['medicalHistory']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Donor (Name, Age, Gender, Blood_Type, Contact_Info, Last_Donation_Date, Medical_History)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', (name, age, gender, blood_type, contact_info, last_donation_date, medical_history))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({ "res": 200, "message": "Perfectly added donor" })

@app.route('/search_recipients', methods=['POST'])
def search_recipients():
    req= request.json
    blood_type = req['bloodType']
    print(blood_type)
    print(f'SELECT * FROM Recipient WHERE Blood_Type ={blood_type}')
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM donor WHERE Blood_Type = "{str(blood_type)}" ;')
    
    recipients = cursor.fetchall()
    print(recipients) 
    cursor.close()
    conn.close()
    
    return jsonify(recipients)

@app.route("/",methods=['POST','GET'])
@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form['password']
        #print(username,password)
        print(username)
        print(password)
        print(f'SELECT * FROM user WHERE username = {username} and password = {password}')
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f'SELECT * FROM user WHERE username = "{username}" and password = "{password}" ;')
        if cursor.fetchall():
            resp = make_response(redirect('/main')) 
            resp.set_cookie('username', username)
            return resp 
    return redirect("/signup")

@app.route("/signup",methods=['POST','GET'])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"INSERT INTO user (username, password, gmail) values ('{username}', '{password}', '{email}') ;")
        conn.commit()
        cursor.close()
        conn.close()
    return redirect("/login")

@app.route("/main")
def main():
    return render_template("index.html")

def add_user():
    req = request.json
    username = req['username']
    password = req['password']
    mail = req['email']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO user (username, password, gmail)
        VALUES (%s, %s, %s)
    ''', (username, password, mail))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect("/")
    
      

if __name__ == '__main__':
    app.run(debug=True)
