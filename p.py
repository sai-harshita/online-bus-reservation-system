from flask import Flask, render_template,request, url_for,redirect,send_file
from flask_sqlalchemy import SQLAlchemy
from io import BytesIO
from base64 import b64encode



print("golu")
from datetime import datetime
today=datetime.now
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:@localhost/BUSSERVISENEW'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



print('jhgj')
db = SQLAlchemy(app)

class Posts(db.Model):
    ID=db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname=db.Column(db.String(50), unique=False, nullable=True)
    lastname=db.Column(db.String(50), unique=False, nullable=True)
    email=db.Column(db.String(50), unique=False, nullable=True)
    password=db.Column(db.String(50), unique=False, nullable=True)
    confirm_password=db.Column(db.String(50), unique=False, nullable=True)
    month=db.Column(db.String(10), unique=False, nullable=True)
    day=db.Column(db.String(40),unique=False, nullable=True)
    gender=db.Column(db.String(4),unique=False, nullable=True)
    year=db.Column(db.String(10),unique=False, nullable=True)
    date=db.Column(db.String(40),unique=False, nullable=True)

    ima=db.Column(db.LargeBinary)
@app.route('/index')
def image():
    event = Posts.query.filter_by(lastname='bajpai').first()
    image = b64encode(event.ima)
    return render_template('index.html', data=list, image=image)

app.run(debug=True)