from flask  import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

local_server=True
with open('config.json','r') as c:
	parameters=json.load(c)["parameters"]
	
app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://username:password@localhost/db_name'
if(local_server):
	app.config["SQLALCHEMY_DATABASE_URI"] = parameters['local_uri']
else:
	app.config["SQLALCHEMY_DATABASE_URI"] = parameters['production_uri']
	
db = SQLAlchemy(app)

class LogDet(db.Model):
	USERID= db.Column(db.Integer,primary_key=True)
	USERNAME = db.Column(db.String(50), unique=True, nullable=False)
	PASSWORD = db.Column(db.String(50), unique=True, nullable=False )
	
#def save_to_database(USERNAME,PASSWORD):
	#new_user=LogDet(USERNAME=username, PASSWORD= password) 
	#db.session.add(new_user)
	#db.session.commit()

trainname= "Pune-Kazipeth Superfast Express"
trainno= "22151"
startstation= "Pune"
destination= "Kazipet Junction"
haltingstations =" Daund Junction, Ahmadnagar , Kopargaon, Manmad Junction,\n Bhusaval Junction, Shegaon, Akola Junction, Badnera Junction,\n Dhamangaon, Pulgaon Junction, Wardha Junction,\n Hinghat Junction, Warora, Bhandak, Chandrapur, \n Balharshah , Ramagundam, Peddapalli , Kazipet Junction "
coachesavailable= "2S,\n SL,\n 3A,\n 2A \n"
coachesprices= " NA, \n 475, \n 1255 ,\n  1775 \n"
#coach1=" 2S:- \n"
#coach2=" SL:- \n"
#coach3=" 3A:- \n"
#coach4=" 2A:- \n"

ch1sno="1 \n 2 \n "
ch1pos="1 \n 2 \n "
ch1names="DL1 \n DL2 \n "
ch1nofs=" 78 "

ch2sno="1 \n 2 \n 3 \n 4 \n 5 \n 6 \n 7 \n 8 \n 9 \n 10 \n 11 \n "
ch2pos="9 \n 10 \n 11 \n 12 \n 13 \n 14 \n 15 \n 16 \n 17 \n 18 \n 19 \n "
ch2names="S1 \n S2 \n S3 \n S4 \n S5 \n S6 \n S7 \n S8 \n S9 \n S10 \n S11 \n "
ch2nofs=" 71 "

ch3sno="1 \n 2 \n 3 \n 4 \n 5 \n 6 \n "
ch3pos="3 \n 4 \n 5 \n 6 \n 7 \n 8 \n "
ch3names="B1 \b B2 \n B3 \n B4 \n B5 \n B6 \n"
ch3nofs=" 63 "

ch4sno="1 \n "
ch4pos="20 \n "
ch4names="A1 \n "
ch4nofs=" 45 \n "
  

@app.route("/")
def welcome():
    return render_template('index.html')

@app.route("/about")
def about_us():
    return render_template('about.html')

@app.route("/home")
def home_page():
	
    return render_template('home.html')
    
@app.route("/trains")
def trains_list():
	
	return render_template('trains.html', train_name=trainname, train_no=trainno, start_station=startstation, destination=destination, halting_stations=haltingstations, coachesavailable=coachesavailable , coaches_prices=coachesprices )

@app.route("/signup",methods = ['POST', 'GET'])	
def signup():
	if(request.method=='post'):
		username=request.form.get('username')
		password=request.form.get('password')
		
		entry = LogDet(USERNAME=username, PASSWORD= password )
		db.session.add(entry)
		db.session.commit()
		
		
	return render_template('signup.html')
	
@app.route("/coach1")
def coach1info():
	return render_template('coach1.html', ch1sno=ch1sno, ch1pos=ch1pos, ch1names=ch1names, ch1nofs=ch1nofs )
	
@app.route("/coach2")
def coach2info():
	return render_template('coach2.html' , ch2sno=ch2sno, ch2pos=ch2pos, ch2names=ch2names, ch2nofs=ch2nofs )
	
@app.route("/coach3")
def coach3info():
	return render_template('coach3.html' , ch3sno=ch3sno, ch3pos=ch3pos, ch3names=ch3names, ch3nofs=ch3nofs )
	
@app.route("/coach4")
def coach4info():
	return render_template('coach4.html' , ch4sno=ch4sno, ch4pos=ch4pos, ch4names=ch4names, ch4nofs=ch4nofs )
	
@app.route("/login",methods = ['POST', 'GET'])
def login():
	if(request.method=='POST'):
		username=request.form['username']
    	password=request.form['password']
    	
    
    	user = LogDet.query.filter_by(USERNAME=username).first()
    
    	if user and user.PASSWORD==password :
    		return redirect('/home')
    
    	else:
    		error='Incorrect Login Credentials. Please try again.'
			return render_template('loginmain.html')
    
    
    	

    	
    
	
	
	
	
	
	


app.run(debug=True)# by adding debug=true it will automatically detect any changes and reload the site


