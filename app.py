from flask import Flask, flash, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
import psycopg2 as pg
import csv
from model import model_function

# database initialisation
app = Flask(__name__)
ENV = 'prod'


if ENV == 'dev':
    app.debug = True
    app.secret_key = 'b_5#y2L"F4Q8z\n\xec]/'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/test'
    
else:
    app.debug = False
    app.secret_key = 'b_5#y2L"F4Q8z\n\xec]/'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://wqffheawwyxqhy:aa77bd3b6e207adb85a1a53470516a50ed85530e77b502bf334bf6c40582a4ad@ec2-44-194-113-156.compute-1.amazonaws.com:5432/db31h9p5e5bgg0'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

Host='ec2-44-194-113-156.compute-1.amazonaws.com'
Database="db31h9p5e5bgg0"
User="wqffheawwyxqhy"
Password="aa77bd3b6e207adb85a1a53470516a50ed85530e77b502bf334bf6c40582a4ad"

class customer(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String(50))
    lastname=db.Column(db.String(50))
    gender=db.Column(db.String(50))
    dob=db.Column(db.String(50))
    personphone=db.Column(db.String(50))
    city=db.Column(db.String(50))
    statename=db.Column(db.String(50))
    zip=db.Column(db.Integer)
    primarylanguage=db.Column(db.String(50))
    primaryocc=db.Column(db.String(50))
    maxeducationlevel=db.Column(db.String(50))
    maritalstatus=db.Column(db.String(50))
    productcategory=db.Column(db.String(50))
    annualincome=db.Column(db.String(50))
    leadquality=db.Column(db.String(50))
    datecreated = db.Column(db.DateTime(timezone=True), default=datetime.utcnow())



class users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    First_name = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(50))
    Phone_No = db.Column(db.String(50))
    Username = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(1000), nullable=False)
    Date_Created = db.Column(db.DateTime(timezone=True), default=datetime.now())


#sign up route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        flag=0
        fname=First_name=request.form['first_name']
        email=Email=request.form['email']
        phone_no= Phone_No=request.form['phone_no']
        username = Username=request.form['username']
        password = request.form['password']
        confirm_password = request.form["confirm_password"]

        check_user = users.query.filter_by(Username=username).first()
        check_email = users.query.filter_by(Email=email).first()
        
        if len(password)<8 or len(password)>16:
            flash("password must be between 8 and 16 characters")
            flag=1
        elif len(phone_no)!=10:
            flash("enter a valid phone number")
            flag=1
        elif check_email is not None:
            flash("This email is already registered")
            flag=1
        elif check_user is not None:
            flash("username already exists in the database")
            flag=1
        elif confirm_password!=password:
            flash("passwords do no match")
            flag=1

        if flag==0:
            pw=generate_password_hash(password)
            obj = users(First_name=fname, Email=email,Phone_No=phone_no, Username=username, Password=pw)
            db.session.add(obj)
            db.session.commit()
            return redirect(url_for('Login'))
    return render_template('signup.html')


#login route
@app.route('/', methods=['GET', 'POST'])
def Login():

    if request.method == 'POST':

        username = request.form['username']
        un = users.query.filter_by(Username=username).first()
        if un is None:
            flash("Incorrect Username or This User does not exist in our database")
        elif un.Username == request.form['username'] and check_password_hash(un.Password, request.form['password'])==True:
            return redirect(url_for("user", username=un.Username, name=un.First_name, email=un.Email, phone_no=un.Phone_No))
        elif check_password_hash(un.Password, request.form['password'])==False:
            flash("incorrect password",category="message")
    return render_template('login.html')

#customer main page route
@app.route("/customer",methods={'GET','POST'})
def customer_page():
    if request.method=="POST":
        fname=request.form['fname']
        lname=request.form['lname']
        gender=request.form['gender'] 
        dob=request.form['dob']
        phno=request.form['phno']
        city=request.form['city']
        statename=request.form['statename']
        zip=request.form['zip']
        primarylanguage=request.form['primarylanguage']
        primaryoccupation=request.form['primaryoccupation']
        maxeducation=request.form['maxeducation']
        maritalstatus=request.form['maritalstatus']
        annualincome=request.form['annualincome']
        productcategory=request.form['productcategory']

        conn = pg.connect(database=Database, user=User, host=Host, password=Password)
        scur= conn.cursor()
        query="select max(sno) from customer"
        scur.execute(query)
        SNO=scur.fetchall()
        scur.close()
        conn.close()   

        obj=customer(sno=SNO[0][0]+1,firstname=fname,lastname=lname,gender=gender,dob=dob,personphone=phno,city=city,
        statename=statename,zip=zip,primarylanguage=primarylanguage,primaryocc=primaryoccupation,maxeducationlevel=maxeducation,annualincome=annualincome,maritalstatus=maritalstatus,productcategory=productcategory)
        db.session.add(obj)
        db.session.commit()

        flash("information entered Successfully")

        query = "select * from customer"

        conn = pg.connect(database=Database, user=User, host=Host, password=Password)
        cur = conn.cursor()
        cur.execute(query)

        with open('final_table.csv', 'w') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(("sno","firstname","lastname","gender","dob","personphone","city","statename","zip","primarylanguage","primaryocc","maxeducationlevel","maritalstatus","productcategory","annualincome","leadquality","datecreated"))
            for row in cur.fetchall():
                writer.writerow(row)

        
        o=model_function()
        
        cur.close()

        conn.close()

        conn= pg.connect(database=Database, user=User, host=Host, password=Password)
        cur=conn.cursor()
        if o[0]==2:
            result='Best'
        if o[0]==1:
            result='Average'
        if o[0]==3:
            result='Poor'
        
        result1 = result

        cur.execute(f"update customer set leadquality='{result1}' where sno={SNO[0][0]+1}")
        conn.commit()
        cur.close()
        conn.close()

        redirect(url_for(Login))
    return render_template("customer.html")


#main page route
@app.route('/home/<username>/<name>/<email>/<phone_no>', methods={'GET', 'POST'})
def user(username, name, email, phone_no):

    query="select * from customer order by datecreated  limit 1000"

    con=pg.connect(database=Database, user=User, host=Host, password=Password)
    cur=con.cursor()
    cur.execute(query)
    detail=cur.fetchall()

    if request.method == 'POST':
        fname=request.form['fname']
        lname=request.form['lname']
        gender=request.form['gender'] 
        dob=request.form['dob']
        phno=request.form['phno']
        city=request.form['city']
        statename=request.form['statename']
        zip=request.form['zip']
        primarylanguage=request.form['primarylanguage']
        primaryoccupation=request.form['primaryoccupation']
        maxeducation=request.form['maxeducation']
        maritalstatus=request.form['maritalstatus']
        annualincome=request.form['annualincome']
        productcategory=request.form['productcategory']

        conn = pg.connect(database=Database, user=User, host=Host, password=Password)
        scur= conn.cursor()
        query="select max(sno) from customer"
        scur.execute(query)
        SNO=scur.fetchall()
        scur.close()
        conn.close()

        obj=customer(sno=SNO[0][0]+1,firstname=fname,lastname=lname,gender=gender,dob=dob,personphone=phno,city=city,
        statename=statename,zip=zip,primarylanguage=primarylanguage,primaryocc=primaryoccupation,maxeducationlevel=maxeducation,annualincome=annualincome,maritalstatus=maritalstatus,productcategory=productcategory)
        db.session.add(obj)
        db.session.commit()

        flash("information entered Successfully")

        query = "select * from customer"

        conn = pg.connect(database=Database, user=User, host=Host, password=Password)
        cur = conn.cursor()
        cur.execute(query)

        with open('final_table.csv', 'w') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(("sno","firstname","lastname","gender","dob","personphone","city","statename","zip","primarylanguage","primaryocc","maxeducationlevel","maritalstatus","productcategory","annualincome","leadquality","datecreated"))
            for row in cur.fetchall():
                writer.writerow(row)

        
        o=model_function()
        
        cur.close()

        conn.close()

        conn= pg.connect(database=Database, user=User, host=Host, password=Password)
        cur=conn.cursor()
        if o[0]==2:
            result='Best'
        if o[0]==1:
            result='Average'
        if o[0]==3:
            result='Poor'
        
        result1 = result

        cur.execute(f"update customer set leadquality='{result1}' where sno={SNO[0][0]+1}")
        conn.commit()
        cur.close()
        conn.close()
       

        return redirect(url_for("results",result=result))    

    return render_template("Index.html", name=name, userid=username, email=email, phone_no=phone_no,people=detail)



@app.route("/results/<result>")
def results(result): 
    return render_template("results.html",result=result)


if __name__ == '__main__':
    app.run(port=3000)
