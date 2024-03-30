import os
import secrets
from flask import render_template, request, redirect, url_for, flash
from tut3 import app, db, bcrypt
from tut3.models import User , Booking , SeatBookings
from tut3.forms import regform, loginform , updateaccform , bookform,deletebookingform
from flask_login import login_user , current_user , logout_user
# Load database parameters from config.json
# with open('config.json', 'r') as c:
#     parameters = json.load(c)["parameters"]

# Configure database URI
# if (local_server):
#     app.config["SQLALCHEMY_DATABASE_URI"] = parameters['local_uri']
# else:
#     app.config["SQLALCHEMY_DATABASE_URI"] = parameters['production_uri']

trainname = "Pune-Kazipeth Superfast Express"
trainno = "22151"
startstation = "Pune"
destination = "Kazipet Junction"
haltingstations = "Daund Junction, Ahmadnagar, Kopargaon, Manmad Junction,\nBhusaval Junction, Shegaon, Akola Junction, Badnera Junction,\nDhamangaon, Pulgaon Junction, Wardha Junction,\nHinghat Junction, Warora, Bhandak, Chandrapur,\nBalharshah, Ramagundam, Peddapalli, Kazipet Junction"
coachesavailable = "2S,\nSL,\n3A,\n2A\n"
coachesprices = "NA,\n475,\n1255,\n1775\n"

ch1sno = "1\n2\n"
ch1pos = "1\n2\n"
ch1names = "DL1\nDL2\n"
ch1nofs = "78"

ch2sno = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n"
ch2pos = "9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n"
ch2names = "S1\nS2\nS3\nS4\nS5\nS6\nS7\nS8\nS9\nS10\nS11\n"
ch2nofs = "71"

ch3sno = "1\n2\n3\n4\n5\n6\n"
ch3pos = "3\n4\n5\n6\n7\n8\n"
ch3names = "B1\nB2\nB3\nB4\nB5\nB6\n"
ch3nofs = "63"

ch4sno = "1\n"
ch4pos = "20\n"
ch4names = "A1\n"
ch4nofs = "45\n"

@app.route("/")
def welcome():
    return render_template('index.html',title='MainPage')

@app.route("/about")
def about_us():
    return render_template('about.html',title='About Us')

@app.route("/home")
def home_page():
    return render_template('home.html',title='Home Page')

@app.route("/trains")
def trains_list():
    return render_template('trains.html', train_name=trainname, train_no=trainno, start_station=startstation, destination=destination, halting_stations=haltingstations, coachesavailable=coachesavailable, coaches_prices=coachesprices, title='All about Trains')

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
    form = regform()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. Go to Login to login to your account!', 'success')
        return redirect(url_for('home_page'))
    return render_template('register.html', title='Register', form=form)

@app.route("/coach1")
def coach1info():
    return render_template('coach1.html', ch1sno=ch1sno, ch1pos=ch1pos, ch1names=ch1names, ch1nofs=ch1nofs)

@app.route("/coach2")
def coach2info():
    return render_template('coach2.html', ch2sno=ch2sno, ch2pos=ch2pos, ch2names=ch2names, ch2nofs=ch2nofs)

@app.route("/coach3")
def coach3info():
    return render_template('coach3.html', ch3sno=ch3sno, ch3pos=ch3pos, ch3names=ch3names, ch3nofs=ch3nofs)

@app.route("/coach4")
def coach4info():
    return render_template('coach4.html', ch4sno=ch4sno, ch4pos=ch4pos, ch4names=ch4names, ch4nofs=ch4nofs)
    
@app.route("/coach4seat")
def coach4seat():
	return render_template('coach4st.html')
	
@app.route("/coach3seat")
def coach3seat():
	return render_template('coach3st.html')
	
@app.route("/coach2seat")
def coach2seat():
	return render_template('coach2st.html')
	
@app.route("/coach1seat")
def coach1seat():
	return render_template('coach1st.html')

@app.route("/DL1")
def DL1seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='DL1').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('DL1.html', booked_seats=booked_seats)

@app.route("/DL2")
def DL2seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='DL2').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('DL2.html', booked_seats=booked_seats)

@app.route("/S1")
def S1seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='S1').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('S1.html', booked_seats=booked_seats)


@app.route("/S2")
def S2seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='S2').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('S2.html', booked_seats=booked_seats)

@app.route("/S3")
def S3seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='S3').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('S3.html', booked_seats=booked_seats)

@app.route("/S4")
def S4seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='S4').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('S4.html', booked_seats=booked_seats)

@app.route("/S5")
def S5seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='S5').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('S5.html', booked_seats=booked_seats)	

@app.route("/S6")
def S6seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='S6').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('S6.html', booked_seats=booked_seats)

@app.route("/S7")
def S7seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='S7').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('S7.html', booked_seats=booked_seats)

@app.route("/S8")
def S8seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='S8').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('S8.html', booked_seats=booked_seats)

@app.route("/S9")
def S9seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='S9').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('S9.html', booked_seats=booked_seats)

@app.route("/S10")
def S10seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='S10').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('S10.html', booked_seats=booked_seats)

@app.route("/S11")
def S11seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='S11').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('S11.html', booked_seats=booked_seats)

@app.route("/B1")
def B1seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='B1').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('B1.html', booked_seats=booked_seats)

@app.route("/B2")
def B2seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='B2').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('B2.html', booked_seats=booked_seats)

@app.route("/B3")
def B3seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='B3').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('B3.html', booked_seats=booked_seats)

@app.route("/B4")
def B4seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='B4').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('B4.html', booked_seats=booked_seats)

@app.route("/B5")
def B5seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='B5').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('B5.html', booked_seats=booked_seats)

@app.route("/B6")
def B6seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='B6').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('B6.html', booked_seats=booked_seats)

@app.route("/A1")
def A1seat():
    # Fetch booked seats for coach S1 from the database
    booked_seats = SeatBookings.query.filter_by(coachname='A1').with_entities(SeatBookings.seatno).all()
    booked_seats = [seat[0] for seat in booked_seats]
    return render_template('A1.html', booked_seats=booked_seats)


@app.route("/login", methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
    form = loginform()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home_page'))
        


        else:
            flash('Incorrect Login Credentials. Please check your Login details', 'danger')
    return render_template('Login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('welcome'))

def savepict(form_picture):
    random_hex = secrets.token_hex(8)
    _,f_ext=os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profilepics', picture_fn )
    form_picture.save(picture_path)

    return picture_fn

@app.route("/account", methods=['POST', 'GET'])
def account():
    form = updateaccform()
    if form.validate_on_submit():
        if form.picture.data:
            pictfile=savepict(form.picture.data)
            current_user.image_file= pictfile
             
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account information has been updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data=current_user.username
        form.email.data=current_user.email
    image_file = url_for('static',filename='profilepics/' + current_user.image_file) 
    return render_template('account.html', title='Account' , image_file=image_file , form=form )

@app.route("/book",methods=['POST','GET'])
def booknow():
    form = bookform()
    
    if form.validate_on_submit():
            if SeatBookings.query.filter_by(seatno=form.seatno.data, coachname=form.coachname.data).first():
                flash('Seat number already booked. Please choose a different seat.', 'danger')
            else:
                seat_bookings = SeatBookings(username=form.username.data, email=form.email.data, seatno=form.seatno.data , startstation=form.startstation.data , endstation = form.endstation.data , coachname=form.coachname.data)
                db.session.add(seat_bookings)
                db.session.commit()
                flash('Your seat has been successfully booked. Have a Safe Journey!', 'success')
                return redirect(url_for('booknow'))
                    
            
    
    return render_template('book.html', title='Book', form=form)

@app.route("/deletebooking",methods=['POST','GET'])
def deletebooking():
    form = deletebookingform()

    booking=SeatBookings.query.filter_by(username=form.username.data,email=form.email.data,seatno=form.seatno.data,coachname=form.coachname.data).first()

    if form.validate_on_submit():
        if booking:
            db.session.delete(booking)
            db.session.commit()
            flash('Your seat booking has been successfully deleted!','success')
        else:
            flash('No such booking found.Please try again !','danger')
            return redirect(url_for('trains_list'))
        
    return render_template('deleteseat.html',title= 'Delete Seat',form=form)



          


    