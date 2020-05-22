
#### ROUTES IMPORTS ####
# -*- coding: utf-8 -*-




from hashlib import sha256
import json
import random
import os
import re
from os import urandom
from PIL.Image import Image
from flask import Flask,render_template, url_for, flash, redirect, session, request, send_from_directory
from flask_migrate import Migrate
from flask_login import login_user, login_required, current_user, logout_user,UserMixin, LoginManager
from flask_mail import Mail
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import Required
from flask_wtf.file import FileField
import binascii


### Tencent live video imports ###

import requests
import datetime
import hashlib
from hashlib import sha1
import hmac
import base64
import  urllib
import urllib3


#### FORMS IMPORTS ####


#### MODELS IMPORTS ####
import datetime
import time
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import psycopg2
import base64
app = Flask(__name__)



UPLOAD_FOLDER = "/videos"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'Adawug;irwugw79536870635785ty0875y03davvavavdey'
appID=200000164
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://power_user:@poweruserpass@172.16.214.87:5432/100CG'
SecretId = 'JIRMZ6O3Qm5KDwCHsgYnlxatGeXq7dfFcjEk'
SecretKey ='wZn5NeGCqxg4r8XaDum2EMzRhIvWHtcU'

mail = Mail(app)
#### MODELS ####
db = SQLAlchemy(app)
db.init_app(app)

migrate = Migrate(app,db)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

followers = db.Table('followers',
                     db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
                     db.Column('followed_id', db.Integer, db.ForeignKey('user.id')))

book = db.Table('book',
                db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                db.Column('post_id', db.Integer, db.ForeignKey('post.id')))

likes = db.Table('likes',
                db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                db.Column('upload_id', db.Integer, db.ForeignKey('upload.id')))


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column('id', db.Integer, primary_key=True)
    role = db.Column('role', db.Integer, default=0)
    sub_role = db.Column('sub role', db.Integer, default=1)
    fullname = db.Column('fullname', db.String(20))
    username = db.Column('username', db.String(20), unique=True, nullable=True)
    password = db.Column('password', db.String, nullable=False)
    image_file = db.Column(db.String(60), nullable=False, default='default.jpg')
    id_type = db.Column('id_type', db.String(60), nullable=True)
    id_number = db.Column('id_number', db.String(), nullable=True)
    id_document = db.Column('id_document', db.String(60), nullable=True)
    nationality = db.Column('nationality', db.String(60), nullable=True)
    occupation = db.Column('occupation', db.String(60), nullable=True)
    email = db.Column('email', db.String(60), nullable=True,unique=True)
    province = db.Column('province', db.String(60), nullable=True)
    city = db.Column('city', db.String(60), nullable=True)
    phone = db.Column('phone', db.BIGINT(), nullable=True)
    posts = db.relationship('Post', backref='author', lazy=True)
    uploads = db.relationship('Upload', backref='uploader', lazy=True)
    lesson = db.relationship('Lesson', backref=db.backref('user_lessons'))
    comments = db.relationship('Comment', backref='author', lazy='dynamic')

    followed = db.relationship('User', secondary=followers,
                               primaryjoin=(followers.c.follower_id == id),
                               secondaryjoin=(followers.c.followed_id == id),
                               backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
    book = db.relationship('Post', secondary=book,backref=db.backref('bookers', lazy='dynamic'))
    likes = db.relationship('Upload', secondary=likes,backref=db.backref('liked', lazy='dynamic'))


    def get_reset_token(self,expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'],expires_sec)
        return s.dumps({'id':self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            id = s.loads(token)['id']
        except:
            return None
        return User.query.get(id)

    #   def book(self,post):
    #       if not self.booked(post):
    #           self.has_booked.append(post)
    #   def unbook(self,post):
    #       if self.has_booked(post):
    #           self.booked.remove(post)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0

    # is_admin = db.Column(db.Boolean,default=False)

    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
            followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())

    def __repr__(self, user_id, role, sub_role, fullname, username, password, image_file, id_type, id_number,
                 id_document, nationality, occupation, email, province, city, phone):
        self.user_id = user_id
        self.role = role
        self.sub_role = sub_role
        self.fullname = fullname
        self.username = username
        self.password = password
        self.image_file = image_file

        self.id_type = id_type
        self.id_number = id_number
        self.id_document = id_document
        self.nationality = nationality
        self.occupation = occupation
        self.email = email
        self.province = province
        self.city = city
        self.phone = phone


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column('id', db.Integer, primary_key=True)
    meetingCode = db.Column('MeetingCode', db.BigInteger, nullable=True)
    verified = db.Column('verified', db.Integer, default=0, nullable=True)
    title = db.Column('title', db.String(70), nullable=True)
    category = db.Column('category', db.String(10), nullable=True)
    description = db.Column('description', db.String(100), nullable=True)
    files = db.Column('file', db.String)
    date = db.Column('Date', db.String, nullable=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=True)
    start_time = db.Column("Start Time", db.String, nullable=True)
    end_time = db.Column('End time', db.String, nullable=True)
    lesson = db.relationship('Lesson', backref=db.backref('lessons'))

    def __repr__(self, id,meetingCode, verified, title, category, description, files, date, user_id, start_time,
                 end_time):
        self.id = id
        self.meetingCode = meetingCode
        self.verified = verified
        self.title = title
        self.category = category
        self.files = files
        self.description = description
        self.date = date
        self.user_id = user_id
        self.start_time = start_time
        self.end_time = end_time

class Lesson(db.Model):
    __tablename__ = 'lesson'
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(100), nullable=True)
    description = db.Column('description', db.String(100), nullable=True)
    post_id = db.Column('post_id', db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self, id, title, description, post_id):
        self.id = id
        self.title = title
        self.description = description
        self.post_id = post_id


class Upload(db.Model):
    __tablename__ = 'upload'
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(30))
    category = db.Column('category', db.String(30))
    description = db.Column('description', db.String(600))
    price = db.Column('price', db.Integer)
    upload_ref = db.Column('upload_ref', db.VARCHAR)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', backref='upload', lazy='dynamic')

    def __repr__(self, id, title, category, description, price, upload_ref, user_id):
        self.id = id
        self.title = title
        self.category = category
        self.description = description
        self.price = price
        self.upload_ref = upload_ref
        self.user_id = user_id


#

class Follow(db.Model):
    __tablename__ = 'follows'
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Comment(db.Model):
   __tablename__ = 'comment'
   id = db.Column(db.Integer, primary_key=True)
   content = db.Column(db.Text)
   timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
   upload_id = db.Column(db.Integer, db.ForeignKey('upload.id'))




### FORMS ###

class Signup_form(FlaskForm):
    email = StringField('EMAIL', [validators.Email()])
    username = StringField('USERNAME', [validators.Length(min=4,max=15) , validators.NoneOf(values=[' '],message="No whitespace allowed")])
    password = PasswordField('PASSWORD', [validators.DataRequired(),validators.Length(min=6)])
    confirm_password = PasswordField('CONFIRM PASSWORD',[validators.DataRequired(),validators.EqualTo('password',message='Password must much')])
    submit = SubmitField('Submit')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken')
        elif " " in username.data:
            raise ValidationError('Whitespace not allowed')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email already exists')





class Login_form(FlaskForm):
    username = StringField('USERNAME', [validators.Length(min=4,max=15)])
    password = PasswordField('PASSWORD', [validators.DataRequired()])
    submit = SubmitField()

    def check_username(self,username):
        user = User.query.filter_by(username=username.data)
        if username not in user.username:
            raise ValidationError('That username does not exist')

    def check_password(self,password,username):
        user = User.query.filter_by(username=username.data)
        if password.data != user.password:
            raise ValidationError('Incorrect password')

class Verify_form(FlaskForm):

    id_type = StringField('ID type', validators=[Required()])
    id_number = StringField('ID number.', validators=[Required()])
    id_document = StringField('ID document', validators=[Required()])
    email = StringField('Email', validators=[Required()])
    nationality = StringField('Nationality', validators=[Required()])
    province = StringField('Province', validators=[Required()])
    city = StringField('City', validators=[Required()])
    occupation = StringField('Occupation', validators=[Required()])
    phone = IntegerField('Phone', validators=[Required()])


class Payment_form(FlaskForm):

    card_number = IntegerField('Card number', validators=[Required()])
    cardholder = StringField('Cardholders name' , validators=[Required()])
    exp_date = DateField('Expiry Date', validators=[Required()])
    cvc = IntegerField('CVC', validators=[Required()])
    zip = StringField('ZIP', validators=[Required()])
    address = StringField('Address', validators=[Required()])


class UpdateAccount(FlaskForm):

    fullname = StringField('FULLNAME', [validators.Length(min=4,max=15)])
    username = StringField('USERNAME', [validators.Length(min=4,max=15)])
    email = StringField('EMAIL', [validators.Length(min=4,max=15)])
    pic = FileField('Update Profile photo')
    password = PasswordField('PASSWORD', [validators.DataRequired()])

    submit = SubmitField('Submit')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username has been taken')


class Session_form(FlaskForm):
    title = StringField('TITLE',[validators.DataRequired()])
    description = TextAreaField('DESCRIPTION',[validators.DataRequired()])
    category = SelectField('CATEGORY', choices=[('MANDARIN','MANDARIN'), ('LEGAL', 'LEGAL'), ('CAREER', 'CAREER'), ('BUSINESS', 'BUSINESS'), ('LIVING', 'LIVING')],widget=None)
    date = DateTimeField("DATE",[validators.DataRequired()])
class Upload_form(FlaskForm):
    title = StringField('Title')
    category = SelectField('Category', choices=[('Mandarin','Mandarin'), ('Communication skills', 'Communication skills'), ('Academics', 'Academics'), ('Visa', 'Visa'), ('Living', 'Living'), ('Talent policy', 'Talent policy'), ('Finance & Law', 'Finance & Law'), ('Entrepreneur', 'Entrepreneur'), ('Others', 'Others')],widget=None)
    description = StringField('Description')
    price = StringField('Price')
    upload = FileField('Upload')
    submit = SubmitField('Submit')


class Lesson_form(FlaskForm):
    title = StringField()
    description = TextAreaField()

class Comment_form(FlaskForm):
    content = StringField()
    submit = SubmitField('Submit')




class Request_reset(FlaskForm):
    email = StringField('EMAIL', [validators.Email()])
    submit = SubmitField()

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('THere is no email registered')

class Reset_password(FlaskForm):
    password = PasswordField('PASSWORD', [validators.DataRequired(),validators.Length(min=6)])
    confirm_password = PasswordField('CONFIRM PASSWORD',[validators.DataRequired(),validators.EqualTo('password',message='Password must much')])
    submit = SubmitField('Reset')



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile')
@login_required
def profile():
#   if session['loggedin']:
#       mycursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#       mycursor.execute(" SELECT * FROM user WHERE   userid= %s ", [session['id']])
#       account = mycursor.fetchone()


#       return render_template('USER_BASE.html',account=account)

    flash('Please verify your account')
    return render_template('USER_BASE.html')


@app.route('/discover_h', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def discover_h(req_path):

    # Permission

    BASE_DIR = '/var/www/App/webapp/static'

    # Joining the base and the requested path
    abs_path = os.path.join(BASE_DIR, req_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return os.abort()

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_from_directory(abs_path)

    # Show directory contents
    upload = os.listdir(abs_path)
    uploads = Upload.query.all()


#    uploads = send_from_directory(directory='videos',filename='videos')
    return render_template('discover_h.html',user=user,uploads=uploads)

@app.route('/event')
def event():
    return render_template('EVENTS.html')

@app.route('/consult')
def consult():
    all_posts = Post.query.all()

    return render_template('CONSULT.html',all_posts=all_posts)

@app.route('/unitalk')
def unitalk():
    return render_template('UNITALK.html')

@app.route('/about')
def about():
    return render_template('ABOUT.html')


@app.route('/coronavirus')
def corona():
    return render_template('corona.html')

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

@app.route('/signup',methods=['POST','GET'])
def signup():
    form = Signup_form(request.form)
    if form.validate_on_submit() and request.method == "POST":
        flash('True')
        hashed_password = hash_password(form.password.data)
        user = User(email=form.email.data,
                    username= form.username.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))


    return render_template('signup.html', form=form)


@app.route('/login',methods=['POST','GET'])
def login():
        form = Login_form()
        if form.validate_on_submit() and request.method == 'POST':
            user = User.query.filter_by(username = form.username.data).first()
            if user and verify_password(user.password,form.password.data) == True:
                login_user(user)
                session['known'] = True
                session['known'] = form.username.data
                display_name = User.query.filter_by(username = form.username.data).first()
                session['known'] = display_name.id
                if current_user.role == 1 and current_user.sub_role == 0:
                    return redirect(url_for('session_admin',id = current_user.id))
                elif current_user.role == 1 and current_user.sub_role == 1:
                        return redirect(url_for('video_admin',id = current_user.id))
                elif current_user.role == 1 and current_user.sub_role == 2:
                    return redirect(url_for('info_admin',id = current_user.id))
                elif current_user.role == 1 and current_user.sub_role == 3:
                    return redirect(url_for('payment_admin',id = current_user.id))
                elif current_user.role == 1 and current_user.sub_role == 4:
                    return redirect(url_for('badge_admin',id = current_user.id))
                else:
                    return redirect(url_for('user_profile', username=current_user.username))
            else:
                pass
        return render_template('LOGIN.html', form=form)





#PROFILE FUNCTIONS

@app.route('/prefer')
@login_required
def prefer():
    return render_template('PREFER.html')

@app.route('/dashboard/<username>')
@login_required
def dashboard(username):
    user_role = current_user.role
    user = User.query.filter_by(username=username).first_or_404()
    uploads = Upload.query.all()

    all_users = User.query.all()
    total_users = len(all_users)
    all_posts = len(Post.query.all())
    data = Post.query.all()
    user_posts = len(current_user.posts)
    book_posts = len(current_user.book)
    booked = all_users
#    post_schema = PostSchema( many=True)
#    output = post_schema.dump(all_users)
#    return jsonify({output.data })
#    print(output)
    for booked in current_user.book:
        post_dict={
            "title": booked.title  ,
        "date": booked.date ,
        "start": booked.start_time
        }
        print(post_dict)
        f = open("package.json", "a")
        f.write(str(post_dict),)
        f.close()
    my_posts = len(current_user.posts)
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
#    for event in data:
#
#       #open and read the file after the appending: event._sa_instance_state = None
#       f = open("demofile2.txt", "r") new_event= (jsonpickle.encode(data, unpicklable=False))
#       print(f.read() print(new_event)
#    print(current_user.username ,'has',len(current_user.posts),'posts',all_posts)
    return render_template('Dashboard.html',uploads= uploads,user=user,my_posts=my_posts,book_posts=book_posts,total_users=total_users,user_role=user_role,all_users=all_users,user_posts = user_posts,image_file=image_file)




def reverse_admin():
    user = User.query.filter_by(role=1).first()
    user.role = 0
    db.session.commit()










def time():
    date = Post.query.all()
    for time in date:
        start = time.start_time
        x = re.split(r'([T+])', start)






@app.route('/update_admin/<int:id>')
@login_required
def update_to_admin(id):
    user = User.query.filter_by(id=id).first()
    user.role = 1
    db.session.commit()
    return redirect(url_for('user_profile',username=current_user.username))

@app.route('/update_session/<int:id>')
def assign_session(id):
    user = User.query.filter_by(id=id).first()

    user.sub_role = 0
    db.session.commit()
    return redirect(url_for('user_profile',username=current_user.username))

@app.route('/update_video_role/<int:id>')
def assign_video(id):
    user = User.query.filter_by(id=id).first()
    user.sub_role = 1
    db.session.commit()
    return redirect(url_for('user_profile',username=current_user.username))

@app.route('/update_info_role/<int:id>')
def assign_info(id):
    user = User.query.filter_by(id=id).first()
    user.sub_role = 2
    db.session.commit()
    return redirect(url_for('user_profile',username=current_user.username))

@app.route('/update_payment/<int:id>')
def assign_payment(id):
    user = User.query.filter_by(id=id).first()
    user.sub_role = 3
    db.session.commit()
    return redirect(url_for('user_profile',username=current_user.username))

@app.route('/update_badge/<int:id>')
def assign_badge(id):
    user = User.query.filter_by(id=id).first()
    user.sub_role = 4
    db.session.commit()
    return redirect(url_for('user_profile',username=current_user.username))






@app.route('/settings/<username>',methods=['GET','POST'])
@login_required
def settings(username):
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    all_users = User.query.all()
    user = User.query.filter_by(username=username).first_or_404()

    form = UpdateAccount()
    if request.method == 'POST':
        if form.pic.data:
            pic_file = save_pic(form.pic.data)
            current_user.image_file = pic_file
        current_user.username = form.username.data
        current_user.password = form.password.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Updated!')
        return redirect(url_for('settings', username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.password.data = current_user.password
        form.email.data = current_user.email
    return render_template('SETTINGS.html',user=user,all_users = all_users,user_role=user_role,form=form,image_file=image_file)


@app.route('/verify/<username>',methods=['POST','GET'])
@login_required
def verify(username):
    form = Verify_form()
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    user = User.query.filter_by(username=username).first_or_404()
    if request.method == 'POST':
        current_user.id_type = form.id_type.data
        current_user.id_number = form.id_number.data
        current_user.id_document = form.id_document.data
        current_user.nationality = form.nationality.data
        current_user.occupation = form.occupation.data
        current_user.email = form.email.data
        current_user.province = form.province.data
        current_user.phone = form.phone.data
        db.session.commit()
        return redirect(url_for('user_profile',username=current_user.username))
    return render_template('VERIFY.html',image_file=image_file,form=form,user=user)



@app.route('/logout')
@login_required
def  logout():

    logout_user()
    session['known'] = False
    print(session)

    return redirect(url_for('login'))


@app.route('/<username>')
@login_required
def user_profile(username):

    user = User.query.filter_by(username=username).first_or_404()
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    followed_posts=Post.query.join(followers, (followers.c.followed_id == Post.user_id)).all()

    all_posts = Post.query.all()

    all_users = User.query.all()
    author = db.session.query(Post.title).join(User.posts)
    user_role = current_user.role
    session['username'] = username



    return render_template('USER.html',followed_posts=followed_posts,user=user,user_role=user_role,all_users=all_users,all_posts = all_posts,author=author, image_file = image_file)
#    return redirect(url_for('login'))

#TRAINER PROFILE FUNCTIONS




#LOGIC FUNCTIONS



@app.route('/user/<username>')
@login_required
def user(username):

    user = User.query.filter_by(username=username).first_or_404()
    image_file = url_for('static', filename ='profile_pics/' + user.image_file)

    all_posts = Post.query.all()
    all_lessons = Lesson.query.all()


#    uploads = url_for('static', filename='videos/' + current_user.uploads)
#    followed_posts = Post.query(User).join(Post)
#    print(followed_posts)
    return render_template('USER_BASE.html',user=user,image_file=image_file,all_posts=all_posts,all_lessons = all_lessons)




@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username))
    return redirect(url_for('user', username=username))

@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username))
    return redirect(url_for('user', username=username))




def save_pic(form_pic):

    random_hex = urandom(8).hex()
    _,f_ext = os.path.splitext(form_pic.filename)
    pic_fn = random_hex + f_ext
    pic_path = os.path.join(app.root_path,'static/profile_pics',pic_fn)
    output_size = (500,500)
    i = Image.open(form_pic)
    i.thumbnail(output_size)
    i.save(pic_path)
    return pic_fn



UPLOADS_URL = 'http://121.40.119.211/static/videos'


@app.route('/discover/<username>', defaults={'req_path': ''})
@app.route('/<path:req_path>')
@login_required
def discover(req_path,username):
    user = User.query.filter_by(username=username).first_or_404()

    session['username'] = current_user.username
    username= session['username']
    # Profile pic
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)

    # Permission
    user_role = current_user.role

    BASE_DIR = '/var/www/App/webapp/static'

    # Joining the base and the requested path
    abs_path = os.path.join(BASE_DIR, req_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return os.abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_from_directory(abs_path)

    # Show directory contents
    upload = os.listdir(abs_path)
    uploads = Upload.query.all()



#    uploads = send_from_directory(directory='videos',filename='videos')
    return render_template('Discover.html',user=user,uploads=uploads,user_role=user_role,image_file=image_file)

@app.route('/book/<int:id>')
@login_required
def book(id):
    post=Post.query.filter_by(id=id).first()
    post.bookers.append(current_user)
    db.session.commit()

    return redirect(url_for('user_profile',username=current_user.username))

@app.route('/unbook/<int:id>')
@login_required
def unbook(id):
    post=Post.query.filter_by(id=id).first()
    post.bookers.remove(current_user)
    db.session.commit()

    return redirect(url_for('user_profile',username=current_user.username))


@app.route('/post/<int:id>')
@login_required
def  post(id):
    post = Post.query.get_or404(id)
    return redirect(url_for('login'))

@app.route('/videos/<upload_ref>' , methods=['POST','GET'])
@login_required

def video(upload_ref):
    form = Comment_form()
    video = Upload.query.filter_by(upload_ref=upload_ref).first()
    uploads  = Upload.query.all()
    user = User.query.all()
    comments = Comment.query.all()
    if request.method == 'POST':
        comment = Comment(content = form.content.data,user_id=current_user.id,upload_id=video.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('video',upload_ref=video.upload_ref))


    return render_template('VIDEO.html',comments = comments,video=video,uploads=uploads,user=user,form=form)

@app.route('/like/video=<int:id>')
@login_required
def like(id):
    video = Upload.query.filter_by(id=id).first()
    video.liked.append(current_user)
    db.session.commit()
    return redirect(url_for('video',upload_ref=video.upload_ref))

def unlike():
    video = Upload.query.filter_by(id=id).first()
    video.liked.remove(current_user)
    db.session.commit()

@app.route('/unlike/video=<int:id>')
@login_required
def unlike(id):
    video = Upload.query.filter_by(id=id).first()
    video.liked.remove(current_user)
    db.session.commit()
    return redirect(url_for('video',upload_ref=video.upload_ref))


def createMeeting(title,fulltime,end_time):
    num = random.randint(0, 999999999)
    stamp = int(time.time())

    uri = "/v1/meetings"

    headerString = "X-TC-Key=%s&X-TC-Nonce=%s&X-TC-Timestamp=%s" % (SecretId, num, str(stamp))

    req_body = {
        "userid": str(current_user.username),
        "instanceid": 1,
        "subject": "%s" % (title),
        "type": 0,
        "hosts": [{"userid": str(current_user.username)}],

        "start_time": str(int(fulltime) / 1000),
        "end_time": str(int(end_time) / 1000),
        "settings": {
            "mute_enable_join": True,
            "allow_unmute_self": False,
            "mute_all": False,
            "host_video": True,
            "participant_video": False,
            "enable_record": False,
            "play_ivr_on_leave": False,
            "play_ivr_on_join": False,
            "live_url": False
        }
    }
    req_body = json.dumps(req_body)
    stringToSign = "%s\n%s\n%s\n%s" % ('POST', headerString, uri, req_body)
    print(stringToSign)

    your_secretkey = SecretKey.encode('utf-8')
    stringToSign = stringToSign.encode('utf-8')

    signature = hmac.new(your_secretkey, stringToSign, digestmod=hashlib.sha256).hexdigest()
    print(signature)

    signature = base64.b64encode(signature.encode("utf-8"))

    headers = {'Content-Type': 'application/json', 'X-TC-Key': SecretId, 'X-TC-Timestamp': str(stamp),
               'X-TC-Nonce': str(num), 'AppId': '200000164', 'X-TC-Signature': signature, 'X-TC-Registered': '0'}
    datas = req_body
    r = requests.post("https://api.meeting.qq.com/v1/meetings", data=datas, headers=headers)
    print(r.text)
    print(r.json())

    return r.json()

def inquire(meetingcode,username,instanceid):
    num = random.randint(0, 999999999)
    stamp = int(time.time())

    uri = "/v1/meetings?meeting_code="+str(meetingcode)+"&userid="+username+"&instanceid="+str(instanceid)

    headerString = "X-TC-Key=%s&X-TC-Nonce=%s&X-TC-Timestamp=%s" % (SecretId, num, str(stamp))
    req_body = ""

    stringToSign = "%s\n%s\n%s\n%s" % ('GET', headerString, uri, req_body)
    print(stringToSign)

    your_secretkey = SecretKey.encode('utf-8')
    stringToSign = stringToSign.encode('utf-8')

    signature = hmac.new(your_secretkey, stringToSign, digestmod=hashlib.sha256).hexdigest()
    print(signature)

    signature = base64.b64encode(signature.encode("utf-8"))
    params={
        "meetingCode": str(meetingcode),
        "userid": username,
        "instanceid": instanceid,
    }


    headers = {'Content-Type': 'application/json', 'X-TC-Key': SecretId, 'X-TC-Timestamp': str(stamp),
               'X-TC-Nonce': str(num), 'AppId': '200000164', 'X-TC-Signature': signature, 'X-TC-Registered': '0'}
    r = requests.get("https://api.meeting.qq.com/v1/meetings?meeting_code="+str(meetingcode)+"&userid="+username+"&instanceid="+str(instanceid), headers=headers)
    print(r.ok)
    print(r.text)

    return r.json()


def cancelMeeting(meetingId,username,instanceId):
    num = random.randint(0, 999999999)
    stamp = int(time.time())

    uri = "/v1/meetings/%s/cancel" % (meetingId)

    headerString = "X-TC-Key=%s&X-TC-Nonce=%s&X-TC-Timestamp=%s" % (SecretId, num, str(stamp))
    req_body = {
     "userid" : username,
     "instanceid" : instanceId,
     "reason_code" : 1,
    }
    req_body = json.dumps(req_body)
    stringToSign = "%s\n%s\n%s\n%s" % ('POST', headerString, uri, req_body)
    print(stringToSign)

    your_secretkey = SecretKey.encode('utf-8')
    stringToSign = stringToSign.encode('utf-8')

    signature = hmac.new(your_secretkey, stringToSign, digestmod=hashlib.sha256).hexdigest()
    print(signature)

    signature = base64.b64encode(signature.encode("utf-8"))

    headers = {'Content-Type': 'application/json', 'X-TC-Key': SecretId, 'X-TC-Timestamp': str(stamp),
               'X-TC-Nonce': str(num), 'AppId': '200000164', 'X-TC-Signature': signature, 'X-TC-Registered': '0'}
    datas = req_body
    r = requests.post("https://api.meeting.qq.com/v1/meetings/%s/cancel" % (meetingId), data=datas, headers=headers)
    print(r.ok)
    print(r.json())

    return r.json()

def modifyMeeting(title,fulltime,end_time,meetingId,username,instanceId):
    num = random.randint(0, 999999999)
    stamp = int(time.time())

    uri = "/v1/meetings/%s" % (meetingId)
    headerString = "X-TC-Key=%s&X-TC-Nonce=%s&X-TC-Timestamp=%s" % (SecretId, num, str(stamp))
    req_body = {
        "userid": username,
        "instanceid": instanceId,
        "subject": "%s" % (title),
        "type": 0,
        "hosts": [{"userid": str(current_user.username)}],
        "start_time": str(int(fulltime) / 1000),
        "end_time": str(int(end_time) / 1000),
        "settings": {
            "mute_enable_join": True,
            "allow_unmute_self": False,
            "mute_all": False,
            "host_video": True,
            "participant_video": False,
            "enable_record": False,
            "play_ivr_on_leave": False,
            "play_ivr_on_join": False,
            "live_url": False
        }
    }
    req_body = json.dumps(req_body)
    stringToSign = "%s\n%s\n%s\n%s" % ('PUT', headerString, uri, req_body)
    print(stringToSign)

    your_secretkey = SecretKey.encode('utf-8')
    stringToSign = stringToSign.encode('utf-8')

    signature = hmac.new(your_secretkey, stringToSign, digestmod=hashlib.sha256).hexdigest()
    print(signature)

    signature = base64.b64encode(signature.encode("utf-8"))

    headers = {'Content-Type': 'application/json', 'X-TC-Key': SecretId, 'X-TC-Timestamp': str(stamp),
               'X-TC-Nonce': str(num), 'AppId': '200000164', 'X-TC-Signature': signature, 'X-TC-Registered': '0'}
    datas = req_body
    r = requests.put("https://api.meeting.qq.com/v1/meetings/%s" % (meetingId), data=datas, headers=headers)
    print(r.text)
    print(r.json())

    return r.json()

@app.route('/session/<username>meetingId<int:meetingcode>',methods=['GET','POST'])
@login_required
def meetingInfo(username,meetingcode):
    meeting = inquire(meetingcode,current_user.username,1)
    meeting_info = meeting["meeting_info_list"]
    for item in meeting_info:
        meeting_id = item['meeting_id']
        meetingUrl= item["join_url"]
        meetingTitle= item["subject"]
    user = User.query.filter_by(username=username).first_or_404()
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    followed_posts=Post.query.join(followers, (followers.c.followed_id == Post.user_id)).all()

    all_posts = Post.query.all()


    all_users = User.query.all()
    author = db.session.query(Post.title).join(User.posts)
    user_role = current_user.role


    return render_template('meeting.html',meetingTitle=meetingTitle,meetingUrl=meetingUrl,meeting_id=meeting_id,meetingcode=meetingcode,followed_posts=followed_posts,user=user,user_role=user_role,all_users=all_users,all_posts = all_posts,author=author, image_file = image_file)

@app.route('/cancel/<int:meetingId>Code<int:meetingcode>',methods=['GET','POST'])
@login_required
def cancel_meeting(meetingId,meetingcode):

    cancelMeeting(meetingId,current_user.username,1)
    meeting=Post.query.filter_by(meetingCode=meetingcode).first_or_404()
    db.session.delete(meeting)

    db.session.commit()

    return redirect(url_for('user_profile',username=current_user.username))

@app.route('/modify/<username><int:meetingId><int:id>',methods=['GET','POST','PUT'])
@login_required
def modify_meeting(username,meetingId,id):
    user = User.query.filter_by(username=username).first_or_404()
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    lesson_form = Lesson_form()
    form = Session_form()
    verify_form = Verify_form()
    if request.method == 'POST':
        fulltime = request.form['date-time']
        fullDate = datetime.fromtimestamp(int(fulltime) / 1000).strftime('%Y-%m-%d')
        startTime = datetime.fromtimestamp(int(fulltime) / 1000).strftime('%H:%M')
        end_time = request.form['end-time']
        endTime = datetime.fromtimestamp(int(end_time) / 1000).strftime('%H:%M')

        #        start = re.split(r'([T+])', time)
        #        end = re.split(r'([T+])', end_time)

        meeting = modifyMeeting(form.title.data, fulltime,end_time,meetingId,current_user.username,1 )

        meeting_info = meeting["meeting_info_list"]
        for item in meeting_info:
            meetingCode = item['meeting_code']


        post = Post.query.filter_by(id=id).first_or_404()
        lesson = Lesson(title=request.form['title'], description=request.form['description'])
        verify = User(id_type=verify_form.id_type.data, id_number=verify_form.id_number.data,
                      id_document=verify_form.id_document.data,
                      nationality=verify_form.nationality.data, occupation=verify_form.occupation.data,
                      email=verify_form.email.data, phone=verify_form.phone.data)

        post.title= form.title.data
        post.start_time=startTime
        post.end_time=endTime
        post.date=fullDate

        db.session.commit()

        return redirect(url_for('meetingInfo', meetingcode=meetingCode, username=current_user.username))
    return render_template('modify.html',user=user,user_role = user_role,form=form,verify_form=verify_form,lesson_form=lesson_form,image_file=image_file)
@app.route('/create/<username>',methods=['GET','POST'])
@login_required
def create(username):
    user = User.query.filter_by(username=username).first_or_404()
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    lesson_form = Lesson_form()
    form = Session_form()
    verify_form = Verify_form()
    if request.method =='POST':
        fulltime = request.form['date-time']
        fullDate = datetime.fromtimestamp(int(fulltime)/1000).strftime('%Y-%m-%d')
        startTime = datetime.fromtimestamp(int(fulltime)/1000).strftime('%H:%M')
        end_time =request.form['end-time']
        endTime=datetime.fromtimestamp(int(end_time)/1000).strftime('%H:%M')
        print(fulltime)
        print(end_time)
        print(fullDate)
#        start = re.split(r'([T+])', time)
#        end = re.split(r'([T+])', end_time)

        meeting = createMeeting(form.title.data,fulltime,end_time)

        meeting_info = meeting["meeting_info_list"]
        for item in meeting_info:
            meetingCode = item['meeting_code']

        post = Post(title=form.title.data,category=form.category.data,description=form.description.data,date= fullDate,start_time= startTime ,end_time = endTime, author=current_user,meetingCode=meetingCode)
        lesson = Lesson(title=request.form['title'],description=request.form['description'])
        verify = User(id_type = verify_form.id_type.data,id_number = verify_form.id_number.data,id_document = verify_form.id_document.data,
                     nationality = verify_form.nationality.data,occupation = verify_form.occupation.data,email = verify_form.email.data,phone = verify_form.phone.data)

        db.session.add(post,verify)

        db.session.commit()

        return redirect(url_for('meetingInfo',meetingcode=meetingCode,username=current_user.username))
    return render_template('CREATE1.html',user=user,user_role = user_role,form=form,verify_form=verify_form,lesson_form=lesson_form,image_file=image_file)



@app.route('/uploads/<username>',methods=['POST','GET'])
@login_required
def upload(username):
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    user = User.query.filter_by(username=username).first_or_404()
    form = Upload_form()
    if request.method == 'POST':
#        random_hex = urandom(8).hex()
        file  = request.files['file']
        with open(file,"r") as file:
            content = file.read()
            encoded=base64.b64decode(bytes.fromhex(content))
        _, f_ext = os.path.splitext(file.filename)
        file_hex = encoded
        file_fn = encoded + f_ext
        file.save(os.path.join(app.root_path, 'static/videos/discover videos', file_fn))
        path = os.path.join(file_fn)
        upload = Upload(title=form.title.data,description=form.description.data,category=form.category.data,price= form.price.data,upload_ref=path,uploader=current_user)
        db.session.add(upload)
        db.session.commit()

 #       f.save(os.path.join(app.config['UPLOAD_FOLDER']+f))
        return redirect(url_for('discover',upload_ref=file_hex,username=current_user.username))
    return render_template('UPLOADS.html',user=user,user_role=user_role,form =form,image_file=image_file)


@app.route('/lesson<int:id><username>', methods=['POST','GET'])
@login_required
def lesson(username,id):
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)

    user = User.query.filter_by(username=username).first_or_404()
    form = Lesson_form()
    post = Post.query.filter_by(id=id).first()
    if request.method == 'POST':


        lesson = Lesson(title = request.form['title'],description = form.description.data,post_id=id,user_id=current_user.id)
        db.session.add(lesson)
        db.session.commit()
        return redirect(url_for('user_profile',username=current_user.username))



    return render_template('LESSON.html',user=user,post=post,form=form,image_file=image_file)

@app.route('/userview/<username>',methods=['GET','POST'])
@login_required
def userview(username):
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    all_users = User.query.all()
    user = User.query.filter_by(username=username).first_or_404()

    return render_template('USER_VIEW.html',user=user,all_users = all_users,user_role=user_role,image_file=image_file)





# Superadmin

@app.route('/superadminview',methods=['GET','POST'])
@login_required
def superview():
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    all_users = User.query.all()

    return render_template('USER_VIEW.html',user=user,all_users = all_users,user_role=user_role,image_file=image_file)

#session role
@app.route('/session_admin/<int:id>',methods=['GET','POST'])
@login_required
def session_admin(id):
    user = User.query.filter_by(id=id).first_or_404()
    all_posts = Post.query.all()

    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    all_users = User.query.all()

    return render_template('session_admin.html',user=user,all_users = all_users,all_posts=all_posts,user_role=user_role,image_file=image_file)

@app.route('/session_view/<int:id>',methods=['GET','POST'])
@login_required
def session_view(id):
    session_post = Post.query.filter_by(id=id).first()
    user = User.query.filter_by(id=id).first_or_404()
    comments = Comment.query.all()
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    all_users = User.query.all()

    return render_template('session_view.html',session_post=session_post,comments=comments,video=video,user=user,all_users = all_users,user_role=user_role,image_file=image_file)

@app.route('/session_verify/<int:id>',methods=['GET','POST'])
@login_required
def session_verify(id):
    session_post = Post.query.filter_by(id=id).first()
    session_post.verified = 1
    db.session.commit()

    return redirect(url_for('session_admin',id=session_post.id))

@app.route('/session_unverify/<int:id>',methods=['GET','POST'])
@login_required
def session_unverify(id):
    session_post = Post.query.filter_by(id=id).first()
    session_post.verified = 0
    db.session.commit()

    return redirect(url_for('session_admin',id=session_post.id))

@app.route('/video_admin/<int:id>',methods=['GET','POST'])
@login_required
def video_admin(id):
    user = User.query.filter_by(id=id).first_or_404()
    uploads  = Upload.query.all()
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    all_users = User.query.all()

    return render_template('video_admin.html',uploads=uploads,user=user,all_users = all_users,user_role=user_role,image_file=image_file)

@app.route('/video/<upload_ref>',methods=['GET','POST'])
@login_required
def video_view(upload_ref):
    video = Upload.query.filter_by(upload_ref=upload_ref).first()
    user = User.query.all()
    comments = Comment.query.all()
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    all_users = User.query.all()

    return render_template('video_view.html',comments=comments,video=video,user=user,all_users = all_users,user_role=user_role,image_file=image_file)

@app.route('/dashboard',methods=['GET','POST'])
@login_required
def video_admin_dashboard():
    total_videos = Upload.query.all()
    comments = Comment.query.all()
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    total_users = User.query.all()

    return render_template('video_admin_dashboard.html',comments=comments,total_videos=len(total_videos),user=user,total_users = len(total_users) ,image_file=image_file)

@app.route('/admin/payment/<int:id>',methods=['GET','POST'])
@login_required
def payment_admin():
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    all_users = User.query.all()

    return render_template('Payment_admin.html',user=user,all_users = all_users,user_role=user_role,image_file=image_file)

@app.route('/admin/info_admin/<int:id>',methods=['GET','POST'])
@login_required
def info_admin():
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    all_users = User.query.all()

    return render_template('Information_admin.html',user=user,all_users = all_users,user_role=user_role,image_file=image_file)

@app.route('/admin/badge/<int:id>',methods=['GET','POST'])
@login_required
def badge_admin():
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    all_users = User.query.all()

    return render_template('Badge_admin.html',user=user,all_users = all_users,user_role=user_role,image_file=image_file)






@app.route('/reset_password/<token>' , methods=['POST','GET'])
def reset_token(token):
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token','warning')
        return redirect(url_for('reset_request'))
    form = Reset_password()
    if form.validate_on_submit() and request.method == "POST":

        hashed_password =form.password.data
        user.password = hashed_password
        db.session.commit()
        flash('Updated')

        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)

from datetime import datetime
import time

# current date






url = 'https://api.meeting.qq.com/v1/meetings'
def create_sign(key,toSign):


    h = hmac.new(key,msg=toSign.encode('utf-8'),digestmod=hashlib.sha256).hexdigest()
    print(type(h))
    print(h)
    base = base64.b64encode(h.encode('utf-8'))
    hash = base.decode('utf-8')
    return hash

def generate_nonce(length=8):
    """Generate pseudorandom number."""
    return ''.join([str(random.randint(0, 9)) for i in range(length)])



def generateHeaders(method,params,uri):
    nonce = generate_nonce()
    timeStamp = int(time.time())

    headerString = "X-TC-Key=" + SecretId + "&X-TC-Nonce=" + str(nonce) + "&X-TC-Timestamp=" + str(timeStamp)
    stringSign= method+"\n"+str(headerString)+"\n"+uri+"\n"+str(params)
    b64 = create_sign(SecretKey,stringSign)



    return {'X-TC-Action':'DescribeInstances','X-TC-Key': SecretId,
            'X-TC-Timestamp': str(timeStamp),
            'X-TC-Nonce': str(nonce),
            'AppId': str(appID),
            'X-TC-Signature': b64.encode('utf-8'),
            'content-type':'application/json',
            'Accept': 'application/json'}







@app.route('/Meeting/<username>', methods=['POST', 'GET'])
def test(username):
    uri = '/v1/meetings'

    print(generateHeaders('GET','',uri))


    response = requests.get("https://api.meeting.qq.com/v1",headers=generateHeaders("GET","",uri))

    print(response.request.headers)
    print(response.url)
    return response.json()




if __name__ == '__main__':

    app.run()

