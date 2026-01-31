from flask import Flask, render_template,request, url_for,redirect,send_file,session,abort
from flask_sqlalchemy import SQLAlchemy
from io import BytesIO
from sqlalchemy.orm import scoped_session,sessionmaker
from base64 import b64encode
import base64
from sqlalchemy import func
import sqlite3
from sqlalchemy.sql import text


#from flaskblog import 
#from flaskblog.models import User, Posts
#from flaskblog.forms import RegistrationForm, LoginForm
import os
#import login_user 
#from flask import flask_login
#from flask import Login_Manager, logged_in,login_user,logout_user,current_user,login_required
from sqlalchemy import or_




print("golu")
#from flask.ext.login import LoginManager

#lm = LoginManager()
#lm.init_app(app)
#lm.login_view = 'login'

#from app.admin import admin_blueprint
from datetime import datetime
today=datetime.now
print(today)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:@localhost/busservisenew'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE']='filesystem'
app.secret_key = '_5#y2L"F4Q8z\n\xec]/qaaan'
#login_manager=Login_Manager()



print('jhgj')
db = SQLAlchemy(app)

class Posts(db.Model):
    ID=db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname=db.Column(db.String(50), unique=False, nullable=True)
    lastname=db.Column(db.String(50), unique=False, nullable=True)
    email=db.Column(db.String(50), unique=False, nullable=True)
    password=db.Column(db.String(50), unique=False, nullable=True)
    month=db.Column(db.String(10), unique=False, nullable=True)
    day=db.Column(db.String(40),unique=False, nullable=True)
    gender=db.Column(db.String(4),unique=False, nullable=True)
    year=db.Column(db.String(10),unique=False, nullable=True)
    date=db.Column(db.String(40),unique=False, nullable=True)


    ima=db.Column(db.LargeBinary,unique=False, nullable=True)


class Busesdata(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    busname=db.Column(db.String(50), unique=False, nullable=True)
    seats=db.Column(db.String(50), unique=False, nullable=True)
    ticket_per_seat=db.Column(db.String(50), unique=False, nullable=True)
    date=db.Column(db.String(50), unique=False, nullable=True)
    city=db.Column(db.String(50), unique=False, nullable=True)
    type=db.Column(db.String(10), unique=False, nullable=True)
    ima=db.Column(db.LargeBinary)
    day=db.Column(db.String(20),nullable=True)
    monday=db.Column(db.String(20),nullable=True)
    tuesday=db.Column(db.String(20),nullable=True)
    wednesday=db.Column(db.String(20),nullable=True)
    thursday=db.Column(db.String(20),nullable=True)
    friday=db.Column(db.String(20),nullable=True)
    saterday=db.Column(db.String(20),nullable=True)
	
	
	

@app.route("/")
def hello():

  
    return render_template('index.html')


@app.route("/name",methods=['GET','POST'])
def home():
     if (request.method == 'POST'):
         FIRST=request.form.get('firstname')
         LAST=request.form.get('lastname')
         EMAIL=request.form.get('email')
         Month=request.form.get('month')
         DAY=request.form.get('day')
         YEAR=request.form.get('year')
         GANDER=request.form.get('gender')
         PASSWORD=request.form.get('password')
         file=request.files['ima']
         if FIRST==" " or  LAST==" " or EMAIL==" " or Month==" " or GANDER==" " or PASSWORD==" " or file==" ":
             return render_template('name.html' ,error=error)
         else:
             entry=Posts(day=DAY,year=YEAR,gender=GANDER,month=Month,firstname=FIRST,lastname=LAST,email=EMAIL,password=PASSWORD,ima=file.read(),date=today)
             db.session.add(entry)
             db.session.commit()
             return render_template('name.html')




     return render_template('name.html')
@app.route('/busesdata' ,methods=['GET','POST'])
def busesdata():
    added="BUS SUCESSFULLY ADDED"
    selectall="PLEASE SELECT ALL"
    if request.method=="POST":
        BUSNAME=request.form.get('busname')
        SEATS=request.form.get('seats')
        TICKECT_PER_SEAT=request.form.get('ticket_per_seat')
        DATE=request.form.get('date')
        CITY=request.form.get('city')
        TYPE=request.form.get('type')
        file=request.files['ima']
        DAY=request.form.get("son")
        MONDAY=request.form.get("mon")
        TUESADAY=request.form.get("tue")
        WEDNESDAY=request.form.get("wed")
        THURSDAY=request.form.get("thu")
        FRIDAY=request.form.get("fri")
        SATERDAY=request.form.get("sat")
        if BUSNAME==None or SEATS==None or TICKECT_PER_SEAT==None or file==None :
            return render_template('busesdata',selectall=selectall)
        else:

            print(MONDAY)
            entry1=Busesdata(busname=BUSNAME,seats=SEATS,ticket_per_seat=TICKECT_PER_SEAT,date=DATE, city=CITY,type=TYPE,ima=file.read(),day=DAY,monday=MONDAY,tuesday=TUESADAY,wednesday=WEDNESDAY,friday=FRIDAY,saterday=SATERDAY)
            db.session.add(entry1)
            db.session.commit()
            return render_template('busesdata.html', added=added)

    return render_template('busesdata.html')



@app.route('/index')
def image():
    event = Posts.query.filter_by(firstname='ghar').first()
    image = b64encode(event.ima)
    image = base64.b64encode(event.ima).decode('ascii')
    return render_template('index.html',data=list, image=image)


@app.route('/loginreal', methods=['POST','GET'])
def loginreal():
    invalid="invlid username of password"
    if request.method=='POST':
       username=request.form['username']
       password=request.form['password']
       ragisted=Posts.query.filter_by(firstname=username,password=password).first()

       if ragisted is None:
            return render_template('loginreal.html',invalid=invalid)
       else:
            session['ragisted']=True
            event = Posts.query.filter_by(firstname=username).first()
            #image = b64encode(event.ima)
            image = base64.b64encode(event.ima).decode('ascii')
            return render_template('index.html',data=list, image=image,username=username)
            #return render_template('/index.html')
    return render_template('loginreal.html')
@app.route('/loginpage', methods=['POST','GET'])
#@loginreal():
def loginpage():
    if request.method=="POST":
        #return render_template('loginreal.html')
            loginreal()




    return render_template('loginreal.html')

@app.route('/booking', methods=["POST","GET"])
def booking1():
    global person
    noperson="no person selected "
    person=request.form.get('person')
    city = request.form.get('city')
    date1=Busesdata.query.filter_by(city=city).all()
    for date in date1:
        print(date.date, date.id)
        day=(date.day)
        monday=print(date.monday)
        tuesday=print(date.tuesday)
        wednesday=print(date.wednesday)
        friday=print(date.friday)
        saterday=print(date.saterday)
        if date.day=='sunday':
            import datetime
            today = datetime.date.today()
            sunday = today + datetime.timedelta((6 - today.weekday() % 7))
            print(sunday)
            entry1 = Busesdata(date=sunday)
            update5 = Busesdata.query.filter_by(id=date.id).update({Busesdata.day:sunday})
            db.session.commit()
        if date.monday=='monday':
            import datetime
            today = datetime.date.today()
            monday = today + datetime.timedelta((0 - today.weekday() % 7))
            if monday<today:
                monday=today+datetime.timedelta(7+today.weekday()%7)
            print(monday)
            entry1 = Busesdata(date=monday)
            update5 = Busesdata.query.filter_by(id=date.id).update({Busesdata.monday:monday})
            db.session.commit()
        if date.tuesday=='tuesday':
            import datetime
            today = datetime.date.today()
            tuesday = today + datetime.timedelta((1 - today.weekday() % 7))
            print(tuesday)
            entry1 = Busesdata(date=tuesday)
            db.session.commit()
            update5 = Busesdata.query.filter_by(id=date.id).update({Busesdata.tuesday:tuesday})
        if date.thursday=='thursday':
            import datetime
            today = datetime.date.today()
            thursday = today + datetime.timedelta((3 - today.weekday() % 7))
            print(thursday)
            entry1 = Busesdata(date=thursday)
            update5 = Busesdata.query.filter_by(id=date.id).update({Busesdata.thursday:thursday})
            db.session.commit()
        if date.wednesday=='wednesday':
            import datetime
            today = datetime.date.today()
            wednesday = today + datetime.timedelta((2 - today.weekday() % 7))
            print(wednesday)
            entry1 = Busesdata(date=wednesday)
            update5 = Busesdata.query.filter_by(id=date.id).update({Busesdata.wednesday:wednesday})
            db.session.commit()
        if date.friday=='friday':
            import datetime
            today = datetime.date.today()
            friday = today + datetime.timedelta((4 - today.weekday() % 7))
            print(friday)
            entry1 = Busesdata(date=friday)
            update5 = Busesdata.query.filter_by(id=date.id).update({Busesdata.friday:friday})
            db.session.commit()
        if date.saterday=='saterday':
            import datetime
            today = datetime.date.today()
            saterday = today + datetime.timedelta((5 - today.weekday() % 7))
            print(saterday)
            update5 = Busesdata.query.filter_by(id=date.id).update({Busesdata.saterday:saterday})
            db.session.commit()


        error="select person"
    if request.method=="POST":
        #return redirect(url_for('mybooking1',id=id))
        #busname=request.form['busname']
        date=request.form['date']
        global z
        city=request.form.get('city')
        person=request.form.get('person')
        if person=='0':
            return render_template('booking.html',noperson=noperson)
        else:
            id=Bookingdata.query.all()
            seat=Busesdata.query.filter_by(city=city).filter(or_(Busesdata.day == date,Busesdata.monday == date,Busesdata.tuesday == date,Busesdata.wednesday == date,Busesdata.thursday == date,Busesdata.friday == date,Busesdata.saterday == date)).all()
            for seat1 in seat:
                if seat1==None:
                    return render_template('booking.html', rows=seat)
                else:
                    return render_template('booking.html', rows=seat,date=date)

                    #(int(float((seat1.seats)))-(float(result1)))
					#return redirect(url_for(booking))

						#print(x)
						#if x<1:
						   #error="NO BUS AVELABLE"
						   #return render_template('booking.html',error=error)
					#print(x)
					#name=seat.busname
					#date=seat.date
					#prise=seat.ticket_per_seat
					#city=seat.city
					#type=seat.type
	    #return render_template('booking.html', rows=seat)
    return render_template('booking.html')
class Bookingdata(db.Model):
    id=db.Column(db.String(20) ,primary_key=True ,nullable=True)
    busname=db.Column(db.String(50), unique=False, nullable=True)
    seats=db.Column(db.String(50), unique=False, nullable=True)
    collection=db.Column(db.String(50), unique=False, nullable=True)
    bookingdate=db.Column(db.String(50), unique=False, nullable=True)
    #day=db.Column(db.String(20),nullable=True)
    
	
@app.route('/booking', methods=["POST","GET"])
@app.route('/mybooking/<string:id>/<string:date>',methods=['POST','GET'])
def mybooking1(id,date):
    sucessfull="BOOKED SUCESSFULLY"
    today = datetime.now().strftime("%Y-%m-%d")
    seat1=Busesdata.query.filter_by(id=id).all()
    for seat in seat1:
        print('g')
    if person==0:
        x=request.form.get('person')
        print(x)

    x=seat.seats-int(person)
    today2=seat.date
    print(today2)
    X = int(person) * int(seat.ticket_per_seat)
    if today2 != today:
        update5 = Busesdata.query.filter_by(id=id).update({Busesdata.seats: '50'})
        update5 = Busesdata.query.filter_by(id=id).update({Busesdata.date: today})
        #delete=Booking.query.filter_by(id=id).delete()
        db.session.commit()


		
    

    if request.method=="POST":
        seatfill=int(person)
        money=int(X)
        PERSON=person
        BUSNAME=seat.busname
        TYPE=seat.type
        ID=seat.id
        Bookingdate = request.form.get('bookingdate')
        update5=Busesdata.query.filter_by(id=id).update({Busesdata.seats:x})
        entry1=Bookingdata(seats=PERSON,id=ID,busname=BUSNAME,collection=X,bookingdate=Bookingdate)
        db.session.add(entry1)
        db.session.commit()
        return render_template('mybooking.html',X=X,date=date,sucessfull=sucessfull)
    return render_template('mybooking.html',X=X,date=date)
	
	    
	
@app.route('/schedule1')
def viewbookingdata():
    buses=Busesdata.query.all()
    booking=Bookingdata.query.all()
    #for buses in buses:
      # n=(int(float(buses.totelseats)-int(float(buses.seats))))
       #print(n)

    return render_template('schedule1.html' ,buses=buses,booking=booking)

@app.route('/schedule2/<string:id>')
def viewbookingdata2(id):
    buses=Busesdata.query.all()
    b=Bookingdata.query.with_entities(func.sum(Bookingdata.seats)).filter_by(id = id).first()
    for b in b:
        print(b)
    collection=Bookingdata.query.with_entities(func.sum(Bookingdata.collection)).filter_by(id = id).first()
    for collection in collection:
        print('a')
    #number_trained = db.session.execute(text("select sum seats from Bookingdata where location=id").first())
   
    #print(sum)
	
    #booking=Bookingdata.query.all()
    name1= Bookingdata.query.filter_by(id=id).first()
    
	
    name=name1.busname
    date=name1.bookingdate
    #for buses in buses:
      # n=(int(float(buses.totelseats)-int(float(buses.seats))))
       #print(n)

    return render_template('schedule2.html',date=date ,buses=buses,b=b,name=name,collection=collection)

@app.route('/admin' ,methods=['GET','POST'])
def login():

    error = None
    if request.method == 'POST':
        if request.form['user'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
             session['logged_in']=True

             return render_template('welcomeadmin.html')
    #app.secret_key=os.unrandom(12)


    return render_template('admin.html', error=error)
@app.route('/dataediting')
def dataediting():
    event = Busesdata.query.all()
	
    
    return render_template('dataediting.html',event=event)
@app.route('/dataediting/<string:id>')
def dataediting1(id):
    delete1=Busesdata.query.filter_by(id=id).delete()
    db.session.commit()
    print(delete1)
    print(id)
    print('golu')
    return redirect (url_for('dataediting'))


@app.route('/busesdata1/<string:id>',methods=['POST','GET'])
def busesdata1(id):
    added="BUS EDITED SUCESSFULLY"
    select=Busesdata.query.filter_by(id=id).first()
    global busname
    global ticket_per_seat
    global city
    global day
    global type
    busname1=select.busname
    ticket_per_seat1=select.ticket_per_seat
    seat1=select.seats
    city1=select.city
    day1=select.day
    type1=select.type
    if request.method=="POST":
        BUSNAME = request.form.get('busname')
        CITY = request.form.get('city')
        SEAT = request.form.get('seats')
        TICKET_PER_SEAT = request.form.get('ticket_per_seat')

        update=Busesdata.query.filter_by(id=id).update({Busesdata.busname:BUSNAME})#,{city:CITY},{seat:SEAT},{day:DAY},{ticket_per_seat:TICKER_PER_SEAT})
        update1=Busesdata.query.filter_by(id=id).update({Busesdata.city:CITY})
        update2=Busesdata.query.filter_by(id=id).update({Busesdata.seats:SEAT})
        update3=Busesdata.query.filter_by(id=id).update({Busesdata.ticket_per_seat:TICKET_PER_SEAT})
        db.session.commit()
        return render_template('busesdata1.html',added=added)
    return render_template('busesdata1.html', busname1=busname1, ticket_per_seat1=ticket_per_seat1, seat1=seat1, city1=city1,day1=day1, type1=type1)
@app.route('/busesdata1',methods=['POST','GET'])
def updated():
    BUSNAME=request.form.get('busname')
    CITY=request.form.get('city')
    SEAT=request.form.get('seats')
    DAY=request.form.get('day')
    TICKER_PER_SEAT=request.form.get('ticket_per_seat')


	

@app.route('/download')
def download():
     file_data=Posts.query.filter_by(ID=1).first()
     return send_file(BytesIO(file_data.ima),attachment_filename='sak.PNG' ,as_attachment=True)














@app.route("/newlogin")
def loginsubmit():
    return render_template('newlogin.html')
@app.route("/schedule")
def schedule():
    
     event2=Busesdata.query.all()
     for event in event2:
         image = b64encode(event.ima)
         image = base64.b64encode(event.ima).decode('ascii')
         
        
       
    
     return render_template('schedule.html' ,rows=event2,data=list,image=image)


app.run(debug=True)
