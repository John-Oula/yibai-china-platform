
#### ROUTES IMPORTS ####
# -*- coding: utf-8 -*-


import base64
import binascii
#### MODELS IMPORTS ####
import datetime
import hashlib
import hmac
import json
import logging
import os
import random
import re
import socket
from functools import wraps

from flask_admin.menu import MenuLink
from flask_share import Share
from flask_admin import Admin,BaseView, expose

import filetype
from PIL import Image
from flask import Flask, render_template, url_for, flash, redirect, session, request, jsonify, abort
from flask_login import login_user, login_required, current_user, logout_user,AnonymousUserMixin, UserMixin, LoginManager
from flask_mail import Mail, Message
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from flask_wtf.file import FileRequired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.utils import secure_filename
from wtforms import *
from wtforms.validators import Required
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
import os.path as op
from wtforms.widgets import TextArea


#from alipaySDK.alipay.aop.api.AlipayClientConfig import AlipayClientConfig
#from alipaySDK.alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
#from alipaySDK.alipay.aop.api.domain.AlipayTradeWapPayModel import AlipayTradeWapPayModel
#from alipaySDK.alipay.aop.api.request.AlipayTradeWapPayRequest import AlipayTradeWapPayRequest


app = Flask(__name__)

authentication= 'authentication@100chinaguide.com'
csrf = CSRFProtect(app)
# IP address
def get_Host_name_IP(hostname):
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        if host_name == hostname:
            print("Hostname :  ", host_name)
            print("IP : ", host_ip)
            return True
        else:
            return False
    except:
        print("Unable to get Hostname and IP")

    # Driver code

import requests


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a', )
logger = logging.getLogger('')


if get_Host_name_IP('CJAY') == True:
    app_private_key_string = open("/Users/ASUS/Desktop/webApp/keys/appPrivateKey.txt").read()
    alipay_public_key_string = open("/Users/ASUS/Desktop/webApp/keys/alipayPublicKey.txt").read()
    app_public_key_cert_string = open("/Users/ASUS/Desktop/webApp/certs/appCertPublicKey_2021001182663949.crt").read()
    alipay_root_cert_string = open("/Users/ASUS/Desktop/webApp/certs/alipayRootCert.crt").read()
    alipay_public_key_cert_string = open("/Users/ASUS/Desktop/webApp/certs/alipayCertPublicKey_RSA2.pem").read()


else:
    app_private_key_string = open("/var/www/App/keys/appPrivateKey.txt").read()
    alipay_public_key_string = open('/var/www/App/keys/alipayPublicKey.txt').read()
    app_public_key_cert_string = open("/var/www/App/certs/appCertPublicKey_2021001182663949.crt").read()
    alipay_root_cert_string = open("/var/www/App/certs/alipayRootCert.crt").read()
    alipay_public_key_cert_string = open("/var/www/App/certs/alipayCertPublicKey_RSA2.crt").read()

#if get_Host_name_IP('CJAY') == True:
#    app_private_key_string = open("/Users/ASUS/Desktop/webApp/keys/appPrivateKey.txt").read()
#    alipay_public_key_string = open("/Users/ASUS/Desktop/webApp/keys/alipayPublicKey.txt").read()
#    app_public_key_cert_string = open("/Users/ASUS/Desktop/webApp/certs/appCertPublicKey_2021001182663949.crt").read()
#    alipay_root_cert_string = open("/Users/ASUS/Desktop/webApp/certs/alipayRootCert.crt").read()
#    alipay_public_key_cert_string = open("/Users/ASUS/Desktop/webApp/certs/alipayCertPublicKey_RSA2.pem").read()
#
#
#else:
#    app_private_key_string = open("/var/www/App/keys/appPrivateKey.txt").read()
#    alipay_public_key_string = open('/var/www/App/keys/alipayPublicKey.txt').read()
#    app_public_key_cert_string = open("/var/www/App/certs/appCertPublicKey_2021001182663949.crt").read()
#    alipay_root_cert_string = open("/var/www/App/certs/alipayRootCert.crt").read()
#    alipay_public_key_cert_string = open("/var/www/App/certs/alipayCertPublicKey_RSA2.crt").read()
#
#alipay_client_config = AlipayClientConfig()
#alipay_client_config.server_url = 'https://openapi.alipay.com/gateway.do'
#alipay_client_config.app_id ='2021001182663949'
#alipay_client_config.app_private_key = app_private_key_string
#alipay_client_config.alipay_public_key = alipay_public_key_string
#
#client = DefaultAlipayClient(alipay_client_config=alipay_client_config, logger=logger)



UPLOAD_FOLDER = "/videos"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'Adawug;irwugw79536870635785ty0875y03davvavavdey'
appID=200000164
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'yeti'
app.config['WTF_CSRF_ENABLED'] = True
if get_Host_name_IP('CJAY') == True:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@qwerty1234!@localhost/postgres'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://power_user:@poweruserpass@172.16.214.87:5432/100CG'

SecretId = 'JIRMZ6O3Qm5KDwCHsgYnlxatGeXq7dfFcjEk'
SecretKey ='wZn5NeGCqxg4r8XaDum2EMzRhIvWHtcU'


wechatAppSecret = '47fb2c78fa7c63609d12150c986d1875'
wechatAppId = 'wx67fc65e96be93d6d'

#### MODELS ####

db = SQLAlchemy(app)
db.init_app(app)

share = Share(app)
migrate = Migrate(app,db)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['MAIL_SERVER']='smtp.100chinaguide.com'
app.config['MAIL_PORT'] = 80
app.config['MAIL_USERNAME'] = 'authentication@100chinaguide.com'
app.config['FLASKY_ADMIN'] = 'authentication@100chinaguide.com'
app.config['MAIL_PASSWORD'] = 'verify@2020'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
app.config['FLASKY_ADMIN'] = 'sudomin'

mail = Mail(app)

admin = Admin(app, name='Management Panel', template_mode='bootstrap3')
staticPath = op.join(op.dirname(__file__), 'static')

class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)

class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()

class MessageAdmin(ModelView):
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']

    form_overrides = {
        'description': CKTextAreaField
    }

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

followers = db.Table('followers',
                     db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
                     db.Column('followed_id', db.Integer, db.ForeignKey('user.id')))

book = db.Table('book',
                db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                db.Column('post_id', db.Integer, db.ForeignKey('post.id')))
#review = db.Table('review',
#                db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#                db.Column('review_id', db.Integer, db.ForeignKey('reviews.id')))

bookSchedule = db.Table('bookSchedule',
                db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                db.Column('date_id', db.Integer, db.ForeignKey('availableStatus.id')))

likes = db.Table('likes',
                db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                db.Column('series_id', db.Integer, db.ForeignKey('series.id')))
likesEpisode = db.Table('likesEpisode',
                db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                db.Column('episode_id', db.Integer, db.ForeignKey('episode.id')))


skills = db.Table('skills',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('skill_title', db.String(20), db.ForeignKey('skill.skill_title'))
)

experiences = db.Table('experiences',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('exp_title', db.String(40), db.ForeignKey('experience.exp_title'))
)

available = db.Table('available',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('date_id', db.Integer, db.ForeignKey('availableStatus.id'))
)
episodeComment = db.Table('episodeComment',
    db.Column('comment_id', db.Integer, db.ForeignKey('comment.id')),
    db.Column('episode_id', db.Integer, db.ForeignKey('episode.id')),

)
cart = db.Table('cart',
                db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                db.Column('course_id', db.Integer, db.ForeignKey('series.id')))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column('id', db.Integer, primary_key=True)
    roles = db.Column('roles', db.VARCHAR)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    sub_role = db.Column('sub role', db.Integer, default=1)
    fullname = db.Column('fullname', db.String(20))
    username = db.Column('username', db.String(20), unique=True, nullable=True)
    password = db.Column('password',db.String(500), nullable=False)
    image_file = db.Column(db.String(60), nullable=False, default='default.jpg')
    introduction = db.Column('introduction', db.String(500), nullable=True)
    introduction_video = db.Column('introduction_video', db.String(60), nullable=True)
    id_type = db.Column('id_type', db.String(60), nullable=True)
    id_number = db.Column('id_number', db.String(), nullable=True)
    id_document = db.Column('id_document', db.String(60), nullable=True)
    nationality = db.Column('nationality', db.String(60), nullable=True)
    occupation = db.Column('occupation', db.String(60), nullable=True)
    status = db.Column('status', db.String(20), nullable=True)
    email = db.Column('email', db.String(60), nullable=True,unique=True)
    province = db.Column('province', db.String(60), nullable=True)
    city = db.Column('city', db.String(60), nullable=True)
    phone = db.Column('phone', db.BIGINT(), nullable=True)
    posts = db.relationship('Live', backref='author', lazy=True)
    uploads = db.relationship('Upload', backref='uploader', lazy=True)
    series = db.relationship('Series', backref='user_series', lazy=True)
    episode = db.relationship('Episode', backref='user_episode', lazy=True)
    lesson = db.relationship('Lesson', backref=db.backref('user_lessons'))
    comments = db.relationship('Comment', backref='author', lazy='dynamic')
    review = db.relationship('Reviews', backref='user_review', lazy='dynamic')
    skill = db.relationship('Skill',backref='user',secondary=skills,lazy ='dynamic')
    available = db.relationship('Available',backref='user',secondary=available,lazy ='dynamic')
    exp = db.relationship('Experience',backref='user',secondary=experiences,lazy ='dynamic')
    followed = db.relationship('User', secondary=followers,
                               primaryjoin=(followers.c.follower_id == id),
                               secondaryjoin=(followers.c.followed_id == id),
                               backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
#    followed = db.relationship('User', secondary=review,
#                               primaryjoin=(review.c.reviewer_id == id),
#                               secondaryjoin=(review.c.reviewed_id == id),
#                               backref=db.backref('user_review', lazy='dynamic'), lazy='dynamic')
    book = db.relationship('Live', secondary=book,backref=db.backref('bookers', lazy='dynamic'))
    bookSchedule = db.relationship('Available', secondary=bookSchedule,backref=db.backref('userSchedule', lazy='dynamic'))
    likes = db.relationship('Series', secondary=likes,backref=db.backref('liked', lazy='dynamic'))
    likesEpisode = db.relationship('Episode', secondary=likesEpisode,backref=db.backref('userLikedEpisode', lazy='dynamic'))
    cart = db.relationship('Series', secondary=cart,backref='user_cart', lazy='dynamic')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.username == app.config['FLASKY_ADMIN']:
                self.role = Role.query.filter_by(permissions=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    def can(self, permissions):
        return self.role is not None and (self.role.permissions & permissions) == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def is_moderator(self):
        return self.can(Permission.MODERATOR)



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
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0
    def has_liked(self, video):
        if current_user in video.liked:
            return True
        else:
            return False
    def has_likedEpisode(self, video):
        if current_user in video.userLikedEpisode:
            return True
        else:
            return False

    def has_booked(self,schedule):

        if current_user in schedule.userSchedule:
            return True
        else:
            return False
    def in_cart(self,video):

        if current_user in video.user_cart:
            return True
        else:
            return False

    def has_bookedLive(self,live):

        if current_user in live.bookers:
            return True
        else:
            return False

    # is_admin = db.Column(db.Boolean,default=False)

    def followed_posts(self):
        followed = Live.query.join(
            followers, (followers.c.followed_id == Live.user_id)).filter(
            followers.c.follower_id == self.id)
        own = Live.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Live.timestamp.desc())

    def followed_uploads(self):
        followed = Upload.query.join(
            followers, (followers.c.followed_id == Upload.user_id)).filter(
            followers.c.follower_id == self.id)
        own = Upload.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Upload.timestamp.desc())


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False
    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    @staticmethod
    def insert_roles():
        roles = { 'User': (Permission.FOLLOW |
                           Permission.COMMENT |
                           Permission.LIVE_SESSION |
                           Permission.SCHEDULE |
                           Permission.LIVE_SESSION |
                           Permission.LIVE_SESSION |
                           Permission.UPLOAD, True),
                  'Moderator': (Permission.MODERATE, False),
                  'Administrator': (0xff, False)        }
        default_role = 'User'
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm

    def __repr__(self):
        return '<Role %r>' % self.name

class Permission:
    FOLLOW = 0x01
    COMMENT = 0x02
    UPLOAD = 0x04
    LIVE_SESSION = 0x06
    MODERATE = 0x08
    BUY = 0x10
    LIKE = 0x12
    SCHEDULE = 0x12
    VERIFY = 0x14
    ADMINISTER = 0x80



class Skill(db.Model):
    __tablename__ = 'skill'
    id = db.Column('id', db.Integer, primary_key=True)
    skill_title = db.Column(db.String(20),unique=True)

class Experience(db.Model):
    __tablename__ = 'experience'
    id = db.Column('id', db.Integer, primary_key=True)
    exp_title = db.Column(db.String(40),unique=True)

class Available(db.Model):
    __tablename__ = 'availableStatus'
    id = db.Column('id', db.Integer, primary_key=True)
    date_available = db.Column(db.String())
    start_time = db.Column("Start Time", db.String, nullable=True)
    end_time = db.Column('End time', db.String, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    meetingUrl = db.Column('meetingUrl', db.VARCHAR)
    meetingCode = db.Column('MeetingCode', db.BigInteger, nullable=True)
    price = db.Column('price', db.Integer)

class Live(db.Model):
    __tablename__ = 'post'
    id = db.Column('id', db.Integer, primary_key=True)
    meetingCode = db.Column('MeetingCode', db.BigInteger, nullable=True)
    verified = db.Column('verified', db.Integer, default=0, nullable=True)
    title = db.Column('title', db.String(70), nullable=True)
    coverImage = db.Column('coverImage',db.String,nullable=True,default='default.jpg')
    category = db.Column('category', db.String(10), nullable=True)
    description = db.Column('description', db.String(100), nullable=True)
    meetingUrl = db.Column('meetingUrl', db.VARCHAR)
    files = db.Column('file', db.String)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    date = db.Column('Date', db.String, nullable=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=True)
    start_time = db.Column("Start Time", db.String, nullable=True)
    end_time = db.Column('End time', db.String, nullable=True)
    lesson = db.relationship('Lesson', backref=db.backref('lessons'))



class Lesson(db.Model):
    __tablename__ = 'lesson'
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(100), nullable=True)
    description = db.Column('description', db.String(100), nullable=True)
    post_id = db.Column('post_id', db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)




class Upload(db.Model):
    __tablename__ = 'upload'
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(30))
    category = db.Column('category', db.String(30))
    description = db.Column('description', db.VARCHAR)
    price = db.Column('price', db.Integer)
    upload_ref = db.Column('upload_ref', db.VARCHAR)
    coverImage = db.Column('coverImage', db.VARCHAR)
    transcript_ref = db.Column('transcript_ref', db.VARCHAR)
    auido_ref = db.Column('auido_ref', db.VARCHAR)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=True)





class Series(db.Model):
    __tablename__ = 'series'
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(30))
    status = db.Column('status', db.String(7))
    category = db.Column('category', db.String(30))
    views = db.Column('views', db.Integer)
    coverImage = db.Column('coverImage', db.VARCHAR)
    upload_ref = db.Column('upload_ref', db.VARCHAR)
    description = db.Column('description', db.VARCHAR)
    price = db.Column('price', db.Integer)
    approved = db.Column('approved', db.Boolean, default=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
    payment = db.relationship('Payment', backref='userPayment', lazy='dynamic')
    comments = db.relationship('Comment', backref='series', lazy='dynamic')
    episode = db.relationship('Episode', backref='sub', lazy=True)




    def is_series(self):
        if self.status == 'single':
            return False
        elif self.status == 'series':
            return True
        else:
            pass
    def disable_description(self):
        return False


    def fileType(self):
        if self.upload_ref:
            videoList=['mov','mp4','m4a','3gp','3g2','mj2' ,'MOV','MP4']
            for v in videoList:
                #                file_path = os.path.abspath('webapp/static/videos/' + self.upload_ref)
                if self.upload_ref.split('.')[1] == v:
                    return 'video'
                elif self.upload_ref.split('.')[1] == 'mp3':
                    return 'audio'

        else:
            return 'Error loading content'

class Episode(db.Model):
    __tablename__ = 'episode'
    id = db.Column('id', db.Integer, primary_key=True)
    subtitle = db.Column('subtitle', db.String(30))
    views = db.Column('views', db.Integer)
    description = db.Column('description', db.VARCHAR)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    upload_ref = db.Column('upload_ref', db.VARCHAR)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=True)
    series_id = db.Column(db.Integer,db.ForeignKey('series.id'))


    transcript_ref = db.Column('transcript_ref', db.VARCHAR)
    auido_ref = db.Column('auido_ref', db.VARCHAR)

#    def __init__ (self, id,subtitle,views, category, description, upload_ref, transcript_ref,auido_ref ,user_id,series_id):
#        self.id = id
#        self.subtitle = subtitle
#        self.category = category
#        self.views = views
#        self.description = description
#        self.upload_ref = upload_ref
#        self.transcript_ref = transcript_ref
#        self.auido_ref = auido_ref
#        self.user_id = user_id
#        self.series_id = series_id


    def fileType(self):
        if self.upload_ref:
            videoList=['mov','mp4','m4a','3gp','3g2','mj2' ,'MOV','MP4']
            for v in videoList:
                #                file_path = os.path.abspath('webapp/static/videos/' + self.upload_ref)
                if self.upload_ref.split('.')[1] == v:
                    return 'video'
                elif self.upload_ref.split('.')[1] == 'mp3':
                    return 'audio'

        else:
            return 'Error loading content'

class Payment(db.Model):
    __tablename__ = 'payment'
    id = db.Column('id', db.Integer, primary_key=True)
    order_number = db.Column('order_number', db.String(30))
    amount = db.Column('amount', db.INT)
    price = db.Column('price', db.INT)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
    series_id = db.Column('series_id', db.Integer, db.ForeignKey('series.id'), nullable=False)





class Follow(db.Model):
    __tablename__ = 'follows'
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Comment(db.Model):
   __tablename__ = 'comment'
   id = db.Column(db.Integer, primary_key=True)
   content = db.Column(db.Text)
   disabled = db.Column(db.Boolean,default=False)
   timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
   series_id = db.Column(db.Integer, db.ForeignKey('series.id'))
   episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'))
   episodeComment = db.relationship('Episode', secondary=episodeComment,
                                    backref=db.backref('userCommentEpisode', lazy='dynamic'))


class Reviews(db.Model):
   __tablename__ = 'reviews'
   id = db.Column(db.Integer, primary_key=True)
   content = db.Column(db.Text)
   timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140))
    author = db.Column(db.String(32))
    path = db.Column(db.Text, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()
        prefix = self.parent.path + '.' if self.parent else ''
        self.path = prefix + '{:0{}d}'.format(self.id, self._N)
        db.session.commit()

    def level(self):
        return len(self.path) // self._N - 1

class RoleView(BaseView):
    @expose('/')
    def index(self):
        all_users = User.query.all()
        return self.render('admin/live.html',all_users=all_users)

def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)
admin.add_view(ModelView(User, db.session, category="User List"))
admin.add_view(ModelView(Live, db.session, category="Live"))
admin.add_view(ModelView(Series, db.session, category="Course"))
admin.add_view(ModelView(Available, db.session, category="Schedule"))
admin.add_view(ModelView(Comment, db.session, category=""))
admin.add_view(ModelView(Episode, db.session, category="Course"))
admin.add_view(ModelView(Payment, db.session, category=""))
admin.add_view(FileAdmin(staticPath, '/static/', name='Files'))
admin.add_view(RoleView(name="Assign roles", endpoint='roles',category="Roles & Permissions"))
admin.add_sub_category(name="Links", parent_name="Course")
admin.add_sub_category(name="Assign roles", parent_name="Roles & Permissions")
admin.add_sub_category(name="Create roles", parent_name="Roles & Permissions")
admin.add_sub_category(name="Create live", parent_name="Live")
admin.add_link(MenuLink(name='Create live', url='/', category='Live'))
admin.add_link(MenuLink(name='Create roles', url='/', category='Roles & Permissions'))
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

    id_type = SelectField('CATEGORY', choices=[('Identity Card','Identity Card'),('Passport','Passport')])
    id_number = StringField('ID number.', validators=[Required()])
    id_document = StringField('ID document', validators=[Required()])
    email = StringField('Email', validators=[Required()])
    nationality = StringField('Nationality', validators=[Required()])
    province = StringField('Province', validators=[Required()])
    city = StringField('City', validators=[Required()])
    occupation = StringField('Occupation', validators=[Required()])
    experience = StringField('Experience', validators=[Required()])
    phone = IntegerField('Phone', validators=[Required()])
class User_form(FlaskForm):

    introduction = TextAreaField('Introduction', validators=[Required()])
    status = StringField('Status', validators=[Required()])
    introVideo = FileField('Upload an Introduction video')
    fullname = StringField('Fullname', [validators.Length(min=4,max=15)])
    username = StringField('Username', [validators.Length(min=4,max=15)])
    email = StringField('Email', [validators.Length(min=4,max=15)])
    pic = FileField('Update Profile photo')
    password = PasswordField('Password', [validators.Length(min=6)])

    submit = SubmitField('Submit')




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
    submit = SubmitField('Submit')

class UpdateSession_form(FlaskForm):
    update_session_title = StringField('TITLE',[validators.DataRequired()])
    update_session_description = TextAreaField('DESCRIPTION',[validators.DataRequired()])
    update_session_category = SelectField('CATEGORY', choices=[('MANDARIN','MANDARIN'), ('LEGAL', 'LEGAL'), ('CAREER', 'CAREER'), ('BUSINESS', 'BUSINESS'), ('LIVING', 'LIVING')],widget=None)
    update_session_date = DateTimeField("DATE",[validators.DataRequired()])
    update_session_submit = SubmitField('Update')

class Upload_form(FlaskForm):
    upload_title = StringField('Title')
    upload_category = SelectField('Category', choices=[('Mandarin','Mandarin'), ('Communication skills', 'Communication skills'), ('Academics', 'Academics'), ('Visa', 'Visa'), ('Living', 'Living'), ('Talent policy', 'Talent policy'), ('Finance & Law', 'Finance & Law'), ('Entrepreneur', 'Entrepreneur'), ('Others', 'Others')],widget=None)
    upload_description = HiddenField('Description')
    upload_price = StringField('Price')
    upload_fileName = FileField('Upload File',validators=[FileRequired()])
    upload_coverImage = FileField('Cover Image')
    upload_transcript = FileField('Upload')
    upload_audio = FileField('Upload')
    upload_submit = SubmitField('Submit')


class UpdateUploads_form(FlaskForm):
    update_title = StringField('Title')
    update_category = SelectField('Category', choices=[('Mandarin','Mandarin'), ('Communication skills', 'Communication skills'), ('Academics', 'Academics'), ('Visa', 'Visa'), ('Living', 'Living'), ('Talent policy', 'Talent policy'), ('Finance & Law', 'Finance & Law'), ('Entrepreneur', 'Entrepreneur'), ('Others', 'Others')],widget=None)
    update_description = TextAreaField('Description')
    update_price = StringField('Price')
    update_coverImage = FileField('Cover Image')
    update_submit = SubmitField('Update')

class Series_form(FlaskForm):
    series_title = StringField('Title')
    series_category = SelectField('Category', choices=[('Mandarin','Mandarin'), ('Communication skills', 'Communication skills'), ('Academics', 'Academics'), ('Visa', 'Visa'), ('Living', 'Living'), ('Talent policy', 'Talent policy'), ('Finance & Law', 'Finance & Law'), ('Entrepreneur', 'Entrepreneur'), ('Others', 'Others')],widget=None)
    series_description = HiddenField('Description')
    series_fileName = FileField('Upload File',validators=[FileRequired()])
    series_coverImage = FileField('Cover Image')
    series_price = StringField('Price')
    series_submit = SubmitField('Submit')



class Episode_form(FlaskForm):
    subtitle = StringField('Subtitle')
    description = HiddenField('Description')
    fileName = FileField('Upload File',validators=[FileRequired()])
    coverImage = FileField('Cover Image')
class UpdateEpisode_form(FlaskForm):
    update_subtitle = StringField('Subtitle')
    update_description = TextAreaField('Description')
    update_fileName = FileField('Upload File',validators=[FileRequired()])
    update_coverImage = FileField('Cover Image')
    update_submit = SubmitField('Update')

class UpdateSeries_form(FlaskForm):
    update_series_title = StringField('Title')
    update_series_category = SelectField('Category', choices=[('Mandarin','Mandarin'), ('Communication skills', 'Communication skills'), ('Academics', 'Academics'), ('Visa', 'Visa'), ('Living', 'Living'), ('Talent policy', 'Talent policy'), ('Finance & Law', 'Finance & Law'), ('Entrepreneur', 'Entrepreneur'), ('Others', 'Others')],widget=None)
    update_series_description = HiddenField('Description')
    update_series_coverImage = FileField('Cover Image')

    update_series_price = StringField('Price')
    update_series_submit = SubmitField('Update')

class Lesson_form(FlaskForm):
    title = StringField()
    description = TextAreaField()

class Comment_form(FlaskForm):
    content = StringField()
    submit = SubmitField('Post')




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




@app.context_processor
def inject_permissions():
    return dict(Permission=Permission)

@app.context_processor
def forms():
    form = Upload_form()
    seriesForm = Series_form()
    episodeForm = Episode_form()
    sessionForm = Session_form()
    UpdateEpisode = UpdateEpisode_form()
    UpdateSeries = UpdateSeries_form()
    UpdateUploads = UpdateUploads_form()
    UpdateSession = UpdateSession_form()
    signupForm = Signup_form()
    userForm = User_form()
    commentForm = Comment_form()

    return dict(commentForm=commentForm,userForm = userForm,signupForm=signupForm,UpdateSession=UpdateSession,UpdateUploads=UpdateUploads,UpdateSeries=UpdateSeries,UpdateEpisode=UpdateEpisode,sessionForm=sessionForm,form=form,seriesForm=seriesForm,episodeForm=episodeForm)

@app.route('/' ,methods=['POST','GET'])
def home():
    page = request.args.get('page', type=int)
#    uploads = Upload.query.order_by(Upload.timestamp.desc()).paginate(per_page=4,error_out=False,page=page)
    form = Upload_form()
    seriesForm = Series_form()
    episodeForm = Episode_form()
    sessionForm = Session_form()
    UpdateEpisode = UpdateEpisode_form()
    UpdateSeries = UpdateSeries_form()
    UpdateUploads = UpdateUploads_form()
    UpdateSession = UpdateSession_form()
    signupForm = Signup_form()
    userForm = User_form()
    commentForm = Comment_form()



    loginForm = Login_form()
    if loginForm.validate_on_submit()  and request.method == 'POST':
        user = User.query.filter_by(username=loginForm.username.data).first()
        if user and verify_password(user.password, loginForm.password.data) == True:
            login_user(user)
            session['known'] = True
            session['known'] = loginForm.username.data
            display_name = User.query.filter_by(username=loginForm.username.data).first()
            session['known'] = display_name.id
            if current_user.role == 1 and current_user.sub_role == 0:
                return redirect(url_for('session_admin', id=current_user.id))
            elif current_user.role == 1 and current_user.sub_role == 1:
                return redirect(url_for('video_admin', id=current_user.id))
            elif current_user.role == 1 and current_user.sub_role == 2:
                return redirect(url_for('info_admin', id=current_user.id))
            elif current_user.role == 1 and current_user.sub_role == 3:
                return redirect(url_for('payment_admin', id=current_user.id))
            elif current_user.role == 1 and current_user.sub_role == 4:
                return redirect(url_for('badge_admin', id=current_user.id))
            else:
                return redirect(url_for('home'))
        else:
            pass


    return render_template('home.html',commentForm=commentForm,userForm = userForm,loginForm = loginForm,signupForm=signupForm,UpdateSession=UpdateSession,UpdateUploads=UpdateUploads,UpdateSeries=UpdateSeries,UpdateEpisode=UpdateEpisode,sessionForm=sessionForm,form=form,page=page,seriesForm=seriesForm,episodeForm=episodeForm)


@app.route('/liveSession')
def liveSession():

    videos = Live.query.order_by(Live.timestamp.desc()).all()
    i = 0
    l = []
    for v in range(len(videos)):
        data ={'id':videos[i].id,'title':videos[i].title,'host':videos[i].author.username,'coverImg': videos[i].coverImage,'userImg':videos[i].author.image_file,'category':videos[i].category,'startTime':videos[i].start_time,'endTime':videos[i].end_time,'date':videos[i].date,'meetingCode':videos[i].meetingCode}
        l.append(data)

        i+=1

    print(l)
    return jsonify({'result':l})

@app.route('/userDetails')
def userDetails():

    username = request.args.get('username', type=str)
    user = User.query.filter_by(username=username).first_or_404()
    if current_user.is_anonymous :
        data = {"id":user.id,"username":user.username,"followers":user.followers.count(),"userImage":user.image_file,"videos":len(user.series),"liveSessions":len(user.posts),"introduction":user.introduction,"Isfollowing":False,"fullname":user.fullname,"status":user.status,'email':user.email,'IntroVid':user.introduction_video}
    else:
        data = {"id":user.id,"username":user.username,"followers":user.followers.count(),"userImage":user.image_file,"videos":len(user.series),"liveSessions":len(user.posts),"introduction":user.introduction,"Isfollowing":current_user.is_following(user),"fullname":current_user.fullname,"status":current_user.status,'email':current_user.email,'IntroVid':current_user.introduction_video}

    l=[]
    i = 0
    for v in user.series:
        userSeries = {'id':v.id, 'title': v.title, 'price': v.price,
                'uploader': v.user_series.username, 'coverImg': v.coverImage,
                'userImg': v.user_series.image_file, 'category': v.category,
                'totalEpisodes': len(v.episode)}
        ep = []
        episodeList = user.series
        for e in v.episode:
            episode = {'episodeId': e.id, 'seriesId': e.sub.id, 'subtitle': e.subtitle, 'video': e.upload_ref}
            ep.append(episode)
        userSeries.update({'episode': ep})
        series = l.append(userSeries)
        i += 1
    data.update({'series': l})
    liveList = []
    for live in user.posts:
        userLive = {'id':live.id, 'title': live.title,
                'host': live.author.username, 'coverImg': live.coverImage,
                'userImg': live.author.image_file, 'category': live.category}
        liveList.append(userLive)
    data.update({'live': liveList})
    videoList = []
    for video in user.series:
        userVideos = {'id': video.id, 'title': video.title, 'price': video.price,'description':video.description,
                    'host': video.user_series.username, 'coverImg': video.coverImage,
                    'userImg': video.user_series.image_file, 'category': video.category,
                    'totalEpisodes': len(video.episode)}
        videoList.append(userVideos)
    data.update({'videosList': videoList})

    scheduleList = []
    for schedule in user.available:
        if current_user.is_authenticated:
            userschedule = {'id': schedule.id,'date': schedule.date_available,'time': schedule.timestamp,'startTime':schedule.start_time,'endTime':schedule.end_time,'hasBooked':current_user.has_booked(schedule)}
        else:
            userschedule = {'id': schedule.id,'date': schedule.date_available,'time': schedule.timestamp,'startTime':schedule.start_time,'endTime':schedule.end_time,'hasBooked':False}
        scheduleList.append(userschedule)
        bookersList = []
        for users in schedule.userSchedule:
            bookers = {'id': users.id, 'username': users.username}
            bookersList.append(bookers)
        userschedule.update({'bookers': bookersList})

    data.update({'schedule': scheduleList})

    reviewList = []
    for r in user.review:
        userReview = {'id': r.id,'review': r.content,'timestamp': r.timestamp,'user-id':r.user_review.id}
        reviewList.append(userReview)
        userList = []
#        for users in r.user_review:
#            u = {'id': users.id, 'username': users.username}
#            userList.append(u)
#        userReview.update({'users': userList})

    data.update({'reviews': reviewList})
    likedSeriesList = []
    for v in user.likes:
        userSeries = {'id':v.id, 'title': v.title, 'price': v.price,
                'uploader': v.user_series.username, 'coverImg': v.coverImage,
                'userImg': v.user_series.image_file, 'category': v.category,
                'totalEpisodes': len(v.episode)}
        ep = []

        for e in v.episode:
            episode = {'episodeId': e.id, 'seriesId': e.sub.id, 'subtitle': e.subtitle, 'video': e.upload_ref}
            ep.append(episode)
        userSeries.update({'episode': ep})
        likedSeries = likedSeriesList.append(userSeries)
        i += 1
    data.update({'likedSeries': likedSeriesList})


    return data



@app.route('/addCart',methods=['DELETE', 'GET'])
@login_required
@csrf.exempt
def addCart():
    upload_id = request.args.get('upload_id', type=int)

    course = Series.query.filter_by(id=upload_id).first_or_404()
    if request.method == 'GET':
        course.user_cart.append(current_user)
        db.session.commit()

        data = jsonify({"id": course.id, "title": course.title, "coverImage": course.coverImage, "price": course.price})
        return data
    elif request.method == 'DELETE':

        course.user_cart.remove(current_user)
        db.session.commit()
        msg = 'removed from cart'

        return msg
    return '',204



@app.route('/episodeComment',methods=['POST', 'GET'])
@login_required
def episodeComment():
    episode_id = request.args.get('episode_id', type=int)
    form = Comment_form()

    episode = Episode.query.filter_by(id=episode_id).first_or_404()

    comment = Comment(content=form.content.data, user_id=current_user.id, episode_id=episode_id)
    episode.userCommentEpisode.append(comment)
    db.session.commit()

    msg = 'Posted successfully'
    return msg


@app.route('/comment',methods=['POST', 'GET'])
@login_required
def comment():
    form = Comment_form()
    series_id = request.args.get('series_id', type=int)
    course = Series.query.filter_by(id=series_id).first_or_404()
    comment = Comment(content=form.content.data, user_id=current_user.id, series_id=course.id)
    course.comments.append(comment)
    db.session.commit()
    msg = 'Posted successfully'
    return {'msg':msg,'totalComments':course.comments.count()}



@app.route('/cart',methods=['POST','GET'])
@login_required
def cart():
    user_id = request.args.get('user_id', type=int)
    user = User.query.filter_by(id=user_id).first_or_404()

    i = 0
    l = []


    for cart in user.cart:
        data = {"id": cart.id, "title": cart.title, "coverImage": cart.coverImage, "price": cart.price}
        l.append(data)
        i+=1
    print(l)

    return jsonify({'result':l})
@app.route('/sent')
def sent():
    msg = Message("Testing",sender=authentication,recipients=["johnoula@icloud.com"])
    mail.send(msg)

    return jsonify({'result':'Success'})

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


@app.route('/discover_h')
def discover_h():

    uploads = Upload.query.all()


    return render_template('discover_h.html',user=user,uploads=uploads)

@app.route('/event')
def event():
    return render_template('EVENTS.html')

@app.route('/consult')
def consult():
    all_posts = Live.query.all()

    return render_template('CONSULT.html',all_posts=all_posts)

@app.route('/unitalk')
def unitalk():
    return render_template('UNITALK.html')

@app.route('/about')
def about():
    return render_template('ABOUT.html')

@app.route('/live')
def live():
    return render_template('live.html')


@app.route('/liveInfo')
def liveInfo():
    return render_template('liveDetails.html')


@app.route('/userProfile')
def profilePage():
    form = Upload_form()
    seriesForm = Series_form()
    episodeForm = Episode_form()
    sessionForm = Session_form()
    UpdateEpisode = UpdateEpisode_form()
    UpdateSeries = UpdateSeries_form()
    UpdateUploads = UpdateUploads_form()
    UpdateSession = UpdateSession_form()
    signupForm = Signup_form()
    userForm = User_form()
    commentForm = Comment_form()
    return render_template('profile.html',commentForm=commentForm,userForm = userForm,UpdateSession=UpdateSession,UpdateUploads=UpdateUploads,UpdateSeries=UpdateSeries,UpdateEpisode=UpdateEpisode,sessionForm=sessionForm,form=form,seriesForm=seriesForm,episodeForm=episodeForm)

@app.route('/videoInfo')
def videoInfo():
    commentForm = Comment_form()
    return render_template('videoDetails.html',commentForm=commentForm)

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


@app.route('/register', methods=['POST', 'GET'])
def register():
    signupForm = Signup_form(request.form)
    if signupForm.validate_on_submit() and request.method == "POST":
        hashed_password = hash_password(signupForm.password.data)
        user = User(email=signupForm.email.data,
                    username=signupForm.username.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('signIn'))

    return render_template('register.html', signupForm=signupForm)


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


@app.route('/signIn',methods=['POST','GET'])
def signIn():
        loginForm = Login_form()
        if loginForm.validate_on_submit() and request.method == 'POST':
            user = User.query.filter_by(username = loginForm.username.data).first()
            if user and verify_password(user.password,loginForm.password.data) == True:
                login_user(user)
                session['known'] = True
                session['known'] = loginForm.username.data
                display_name = User.query.filter_by(username = loginForm.username.data).first()
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
                    return redirect(url_for('home'))
            else:
                pass
        return render_template('signIn.html',loginForm=loginForm)


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
    all_posts = len(Live.query.all())
    data = Live.query.all()
    user_posts = len(current_user.posts)
    book_posts = len(current_user.book)
    booked = all_users
#    post_schema = PostSchema( many=True)
#    output = post_schema.dump(all_users)
#    return jsonify({output.data })
#    print(output)
#   for booked in current_user.book:
#       post_dict={
#           "title": booked.title  ,
#       "date": booked.date ,
#       "start": booked.start_time
#       }
#       print(post_dict)
#       f = open("package.json", "a")
#       f.write(str(post_dict),)
#       f.close()
    my_posts = len(current_user.posts)
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)

    seriesId = Series.query.all()
    for seriesId in seriesId:
        seriesIdNum = int(seriesId.id) + 1
    return render_template('Dashboard.html',seriesIdNum=seriesIdNum,uploads= uploads,user=user,my_posts=my_posts,book_posts=book_posts,total_users=total_users,user_role=user_role,all_users=all_users,user_posts = user_posts,image_file=image_file)

def reverse_admin():
    user = User.query.filter_by(role=1).first()
    user.role = 0
    db.session.commit()



def time():
    date = Live.query.all()
    for time in date:
        start = time.start_time
        x = re.split(r'([T+])', start)

@app.route('/verify_payment/<int:token>')
@login_required
def verify_payment(token):
    course_id = request.args.get('course_id', type=int)
    user = request.args.get('user', type=str)
    order_number = request.args.get('user', type=int)
    amount = request.args.get('amount', type=int)
    price = request.args.get('price', type=int)
    user_id = request.args.get('user_id', type=int)

    course = Series.query.filter_by(id = course_id).first()
    payment = Payment(order_number=order_number,amount=amount,price=price,user_id=user_id)
    db.session.add(payment)
    db.session.commit()

    return redirect(url_for('home'))




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
    seriesId = Series.query.all()
    for seriesId in seriesId:
        seriesIdNum = int(seriesId.id) + 1
    form = UpdateAccount()
    if request.method == 'POST':
        if form.pic.data:
            pic_file = save_pic(form.pic.data)
            current_user.image_file = pic_file
        current_user.username = form.username.data
        current_user.password = hash_password(form.password.data)
        current_user.email = form.email.data
        db.session.commit()
        flash('Updated!')
        return redirect(url_for('settings', username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.password.data = current_user.password
        form.email.data = current_user.email
    return render_template('SETTINGS.html',seriesIdNum=seriesIdNum,user=user,all_users = all_users,user_role=user_role,form=form,image_file=image_file)


@app.route('/updateInfo',methods=['GET','POST','PUT'])
@login_required
def updateInfo():
#    username = request.args.get('username', type=str)
#    user = User.query.filter_by(username=username).first_or_404()
    form = User_form()

    if request.method == 'POST':
#        if form.pic.data:
#            pic_file = save_pic(form.pic.data)
#            current_user.image_file = pic_file
        if form.pic.data:
            pic_file = save_pic(form.pic.data)
            current_user.image_file = pic_file
        if form.introVideo.data:
            introVid_file = save_pic(form.introVideo.data)
            current_user.introduction_video = introVid_file
        current_user.introduction = form.introduction.data
        current_user.fullname = form.fullname.data
        current_user.username = form.username.data
        current_user.password = form.password.data
        current_user.status = form.status.data
        current_user.email = form.email.data
        if form.introVideo.data == '':
           current_user.introduction_video = current_user.introduction_video

#        current_user.introduction_video = saveFile(form.introVideo.data, 'videos')

        db.session.commit()
        msg = 'Saved changes'
        return msg
    elif request.method == 'PUT':
        if form.pic.data:
            pic_file = save_pic(form.pic.data)
            current_user.image_file = pic_file
        if form.introVideo.data:
            introVid_file = save_pic(form.introVideo.data)
            current_user.introduction_video = introVid_file
        current_user.introduction = form.introduction.data
        current_user.fullname = form.fullname.data
        current_user.username = form.username.data
        current_user.password = form.password.data
        current_user.status = form.status.data
        current_user.email = form.email.data
        db.session.commit()
        msg = 'Saved changes'
        return msg
    elif request.method == 'GET':
        data = {"id": current_user.id, "username": current_user.username, "followers": current_user.followers.count(),
                    "userImage": current_user.image_file, "videos": len(current_user.series), "liveSessions": len(current_user.posts),
                    "introduction": current_user.introduction,
                    "fullname": current_user.fullname, "status": current_user.status, 'email': current_user.email,
                    "password": current_user.password, 'IntroVideo': current_user.introduction_video}

        return data
    return '', 204
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

    return redirect(url_for('home'))


@app.route('/session/<username>')
@login_required
def user_profile(username):

    user = User.query.filter_by(username=username).first_or_404()
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    followed_posts=Live.query.join(followers, (followers.c.followed_id == Live.user_id)).all()

    all_posts = Live.query.all()
    posts = Live.query.all()
    postNum=len(all_posts)

    all_users = User.query.all()
    author = db.session.query(Live.title).join(User.posts)
    user_role = current_user.role
    session['username'] = username
    seriesId=Series.query.all()
    for seriesId in seriesId:
        seriesIdNum = int(seriesId.id) + 1



    return render_template('sessions.html', seriesIdNum=seriesIdNum,posts=posts, postNum=postNum, followed_posts=followed_posts, user=user, user_role=user_role, all_users=all_users, all_posts = all_posts, author=author, image_file = image_file)

@app.route('/<username>')
@login_required
def my_profile(username):

    user = User.query.filter_by(username=username).first_or_404()
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    followed_posts=Live.query.join(followers, (followers.c.followed_id == Live.user_id)).all()

    all_posts = Live.query.all()
    postNum=len(all_posts)

    all_users = User.query.all()
    author = db.session.query(Live.title).join(User.posts)
    user_role = current_user.role
    session['username'] = username
    seriesId=Series.query.all()
    for seriesId in seriesId:
        seriesIdNum = int(seriesId.id) + 1



    return render_template('USER.html',seriesIdNum=seriesIdNum,postNum=postNum,followed_posts=followed_posts,user=user,user_role=user_role,all_users=all_users,all_posts = all_posts,author=author, image_file = image_file)

@app.route('/feed/<username>')
@login_required
def feed(username):

    user = User.query.filter_by(username=username).first_or_404()
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
#    followed_posts=Live.query.join(followers, (followers.c.followed_id == Live.user_id)).all()
    suggestUser = User.query.filter_by(id=3).first_or_404()
    form = Upload_form()
    all_users = User.query.all()
    followed_posts = current_user.followed_posts()


    author = db.session.query(Live.title).join(User.posts)
    user_role = current_user.role
    session['username'] = username
    seriesId=Series.query.all()
    for seriesId in seriesId:
        seriesIdNum = int(seriesId.id) + 1



    return render_template('feed.html',form=form,suggestUser=suggestUser,seriesIdNum=seriesIdNum,followed_posts=followed_posts,user=user,user_role=user_role,all_users=all_users,author=author, image_file = image_file)


#TRAINER PROFILE FUNCTIONS



#LOGIC FUNCTIONS



@app.route('/user/<username>')
@login_required
def user(username):

    user = User.query.filter_by(username=username).first_or_404()
    image_file = url_for('static', filename ='profile_pics/' + user.image_file)
    suggestUser = User.query.filter_by(id=3).first_or_404()

    all_posts = Live.query.all()
    all_lessons = Lesson.query.all()
    seriesId=Series.query.all()
    for seriesId in seriesId:
        seriesIdNum = int(seriesId.id) + 1

#    uploads = url_for('static', filename='videos/' + current_user.uploads)
#    followed_posts = Live.query(User).join(Live)
#    print(followed_posts)
    return render_template('USER_BASE.html',suggestUser=suggestUser,seriesIdNum=seriesIdNum,user=user,image_file=image_file,all_posts=all_posts,all_lessons = all_lessons)


def followerCount(user):
    count = 0
    for followers in user.followed:
        followers.username
        count += 1
    return count


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
    current_user.followed.append(user)
    db.session.commit()
    followers = user.followers.count()
    flash('You are following {}!'.format(username))
    return jsonify({'result':'success','followers':followers})

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
    current_user.followed.remove(user)
    db.session.commit()
    followers = user.followers.count()

    flash('You are not following {}.'.format(username))
    return jsonify({'result':'success','followers':followers})




def save_pic(form_pic):

    random_hex = binascii.hexlify(os.urandom(8))
    _,f_ext = os.path.splitext(form_pic.filename)
    pic_fn = str(random_hex) + f_ext
    pic_path = os.path.join(app.root_path,'static/profile_pics',pic_fn)
    output_size = (500,500)
    i = Image.open(form_pic)
    i.thumbnail(output_size)
    i.save(pic_path)

    return pic_fn



UPLOADS_URL = 'http://121.40.119.211/static/videos'


@app.route('/discover/<username>')
@login_required
def discover(username):
    page = request.args.get('page', type=int)
    user = User.query.filter_by(username=username).first_or_404()

    session['username'] = current_user.username
    username= session['username']
    # Profile pic
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)

    # Permission
    user_role = current_user.role



    uploads = Upload.query.order_by(Upload.timestamp.desc()).paginate(per_page=4,error_out=False,page=page)

    series= Series.query.order_by(Series.timestamp.desc()).paginate(per_page=2,error_out=False,page=page)
    episodes=Episode.query.all()
    seriesInfo = db.session.query(Episode.subtitle).join(Series.episode)
    seriesId = Series.query.all()
    for seriesId in seriesId:
        seriesIdNum = int(seriesId.id) + 1

#    uploads = send_from_directory(directory='videos',filename='videos')
    return render_template('Discover.html',user=user,page=page,seriesIdNum=seriesIdNum,seriesInfo=seriesInfo,episodes=episodes,series=series,uploads=uploads,user_role=user_role,image_file=image_file)

@app.route('/book/<int:id>')
@login_required
def book(id):
    type = request.args.get('type', type=str)

    if type == 'schedule':
        schedule = Available.query.filter_by(id=id).first()
        schedule.userSchedule.append(current_user)
        db.session.add(schedule)

        db.session.commit()
    elif type == 'live':
        post=Live.query.filter_by(id=id).first()
        post.bookers.append(current_user)
        db.session.commit()

    return jsonify({'result':'success'})

@app.route('/unbook/<int:id>')
@login_required
def unbook(id):
    type = request.args.get('type', type=str)
    username = request.args.get('username', type=str)
    user = User.query.filter_by(username=username).first()

    if type == 'schedule':
        schedule = Available.query.filter_by(id=id).first()
        schedule.userSchedule.remove(current_user)


        db.session.commit()
    elif type == 'live':
        post = Live.query.filter_by(id=id).first()
        post.bookers.remove(current_user)
        db.session.commit()

    return jsonify({'result': 'success'})


@app.route('/post/<int:id>')
@login_required
def  post(id):
    post = Live.query.get_or404(id)
    return redirect(url_for('login'))




@app.route('/videos' , methods=['POST','GET'])
def video():

    videos = Series.query.order_by(Series.timestamp.desc()).all()
    i = 0
    l = []
    for v in range(len(videos)):
        data = {'id': videos[i].id, 'title': videos[i].title, 'username': videos[i].user_series.username,
                'userImg': videos[i].user_series.image_file, 'category': videos[i].category, 'price': videos[i].price, 'coverImage': videos[i].coverImage,'approved': videos[i].approved,'likes':videos[i].liked.count(),'comments':videos[i].comments.count(),'isSeries':videos[i].is_series()}
        l.append(data)

        i += 1

    return jsonify({'result': l})

@app.route('/videoDetails' , methods=['POST','GET'])
def videoDetails():
#    video = request.args.get('video', type=str)
    videoId= request.args.get('videoId', type=int)
    videos = Series.query.filter_by(id=videoId).first()
    relatedVideos = Series.query.filter_by(category=videos.category).all()
    relatedList = []
    commentsList = []
    for r in relatedVideos:

        data = {'id': r.id, 'coverImg': r.coverImage, 'title': r.title, 'isSeries': r.is_series(),
                'videoRef': r.upload_ref, 'type': r.fileType(), 'description': r.description,
                'price': r.price, 'userId': r.user_series.id, 'username': r.user_series.username,
                'userImg': r.user_series.image_file, 'category': r.category, 'likes': r.liked.count(),
                'comments': r.comments.count()}
        relatedList.append(data)

    for c in videos.comments:
        data= {'id':c.id,'content':c.content,'timestamp':c.timestamp,'username':c.author.username,'proPic':c.author.image_file,'userId':c.author.id}
        commentsList.append(data)

    if videos.is_series() == True:
        i = 0
        l = []


        data ={'id': videos.id,'coverImg':videos.coverImage, 'title': videos.title,'isSeries':videos.is_series(),'videoRef':videos.upload_ref,'type':videos.fileType(),'description':videos.description,'price':videos.price,'userId':videos.user_series.id,'username': videos.user_series.username,'userImg': videos.user_series.image_file, 'category': videos.category,'likes':videos.liked.count(),'comments':videos.comments.count()}
        ep = []
        for e in videos.episode:
            if current_user.is_authenticated:
                episode = {'episodeId':e.id,'seriesId':e.sub.id,'subtitle':e.subtitle,'description':e.description,'videoRef':e.upload_ref,'hasLikedEpisode': current_user.has_likedEpisode(e),'likes':e.userLikedEpisode.count()}
            else:
                episode = {'episodeId':e.id,'seriesId':e.sub.id,'subtitle':e.subtitle,'description':e.description,'videoRef':e.upload_ref,'hasLikedEpisode': False,'likes':e.userLikedEpisode.count()}
            ep.append(episode)

        data.update({'episode':ep})
        data.update({'relatedVideos': relatedList})

#        l.append(data)

        if current_user.is_authenticated:
            data.update({'hasLiked': current_user.has_liked(videos),'inCart': current_user.in_cart(videos)})

        return jsonify({'result':data})

    elif videos.is_series() == False:

        data = {'id': videos.id, 'title': videos.title,'coverImg':videos.coverImage,'isSeries':videos.is_series(),'videoRef':videos.upload_ref,'type':videos.fileType(),'description':videos.description,'price':videos.price,'userId':videos.user_series.id,'username': videos.user_series.username,'userImg': videos.user_series.image_file, 'category': videos.category,'likes':videos.liked.count(),'totalComments':videos.comments.count()}
        data.update({'relatedVideos': relatedList})
        data.update({'comments': commentsList})
        if current_user.is_authenticated:
            data.update({'hasLiked': current_user.has_liked(videos),'inCart': current_user.in_cart(videos)})


        return jsonify({'result':data})
    else:
        pass

    return '', 204



@app.route('/liveDetails' , methods=['POST','GET'])
def liveDetails():
    liveId= request.args.get('liveId', type=int)
    live = Live.query.filter_by(id=liveId).first()
    scheduleList = []
    if current_user.is_authenticated:
        data = {'id': live.id, 'title': live.title,'startTime': live.start_time,'endTime': live.end_time,'date': live.date,'coverImage': live.coverImage,'description':live.description,'category': live.category,'meetingCode':live.meetingCode,'meetingUrl':live.meetingUrl,'hasBooked':current_user.has_bookedLive(live)}
    else:
        data = {'id': live.id, 'title': live.title,'startTime': live.start_time,'endTime': live.end_time,'date': live.date,'coverImage': live.coverImage,'description':live.description,'category': live.category,'meetingCode':live.meetingCode,'meetingUrl':live.meetingUrl,'hasBooked':False}
    host = {'userId':live.author.id,'host': live.author.username,'userImg': live.author.image_file,'introduction':live.author.introduction,'followers':live.author.followers.count()}
    for s in live.author.available:
        schedule = {'id': s.id,'date': s.date_available,'startTime':s.start_time,'endTime':s.start_time,'time': s.timestamp}
        scheduleList.append(schedule)
    data.update({'schedule':scheduleList})
    data.update({'host':host})
    return data


@app.route('/series/<int:seriesid>Id<int:id>video<upload_ref>' , methods=['POST','GET'])
@login_required
def series(upload_ref,id,seriesid):
    form = Comment_form()
    video = Episode.query.filter_by(upload_ref=upload_ref).first()
    uploads  = Upload.query.all()
    episodes = Episode.query.filter_by(series_id=seriesid)

    comments = Comment.query.all()
    seriesId = Series.query.all()
    videoId=id
    videoRef=upload_ref
    for seriesId in seriesId:
        seriesIdNum = int(seriesId.id) + 1
    if request.method == 'POST':
        comment = Comment(content = form.content.data,user_id=current_user.id,upload_id=video.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('series',upload_ref=video.upload_ref))


    return render_template('series.html',episodes=episodes,videoRef=videoRef,videoId=videoId,seriesIdNum=seriesIdNum,comments = comments,video=video,uploads=uploads,user=user,form=form)


@app.route('/like/video<int:id>')
@login_required
def like(id):
    video = Series.query.filter_by(id=id).first()
    video.liked.append(current_user)
    db.session.commit()
    likes= video.liked.count()
    return jsonify({'result':'success','likes':likes})

def unlike():
    video = Series.query.filter_by(id=id).first()
    video.liked.remove(current_user)
    db.session.commit()

@app.route('/unlike/video<int:id>')
@login_required
def unlike(id):
    video = Series.query.filter_by(id=id).first()
    video.liked.remove(current_user)
    db.session.commit()
    likes= video.liked.count()
    return jsonify({'result':'success','likes':likes})

@app.route('/like/episode<int:id>')
@login_required
def likeEpisode(id):
    video = Episode.query.filter_by(id=id).first()
    video.userLikedEpisode.append(current_user)
    db.session.commit()
    likes= video.userLikedEpisode.count()
    return jsonify({'result':'success','likes':likes})


@app.route('/unlike/episode<int:id>')
@login_required
def unlikeEpisode(id):
    video = Episode.query.filter_by(id=id).first()
    video.userLikedEpisode.remove(current_user)
    db.session.commit()
    likes= video.userLikedEpisode.count()
    return jsonify({'result':'success','likes':likes})

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

    signature = base64.b64encode(signature.encode("utf-8"))
    params={
        "meetingCode": str(meetingcode),
        "userid": username,
        "instanceid": instanceid,
    }


    headers = {'Content-Type': 'application/json', 'X-TC-Key': SecretId, 'X-TC-Timestamp': str(stamp),
               'X-TC-Nonce': str(num), 'AppId': '200000164', 'X-TC-Signature': signature, 'X-TC-Registered': '0'}
    r = requests.get("https://api.meeting.qq.com/v1/meetings?meeting_code="+str(meetingcode)+"&userid="+username+"&instanceid="+str(instanceid), headers=headers)


    return r.json()
def participants(meetingId,userId):
    num = random.randint(0, 999999999)
    stamp = int(time.time())

    uri = "/v1/meetings/"+str(meetingId)+"/participants?"+"userid="+userId

    headerString = "X-TC-Key=%s&X-TC-Nonce=%s&X-TC-Timestamp=%s" % (SecretId, num, str(stamp))
    req_body = ""

    stringToSign = "%s\n%s\n%s\n%s" % ('GET', headerString, uri, req_body)
    print(stringToSign)

    your_secretkey = SecretKey.encode('utf-8')
    stringToSign = stringToSign.encode('utf-8')

    signature = hmac.new(your_secretkey, stringToSign, digestmod=hashlib.sha256).hexdigest()

    signature = base64.b64encode(signature.encode("utf-8"))
    params={
        "meeting_id": str(meetingId),
        "userid": userId,

    }


    headers = {'Content-Type': 'application/json', 'X-TC-Key': SecretId, 'X-TC-Timestamp': str(stamp),
               'X-TC-Nonce': str(num), 'AppId': '200000164', 'X-TC-Signature': signature, 'X-TC-Registered': '0'}
    r = requests.get("https://api.meeting.qq.com" + uri, headers=headers)


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

@app.route('/session/<int:post_id><username>meetingId<int:meetingcode>',methods=['GET','POST'])
@login_required
def meetingInfo(username,meetingcode,post_id):
    meeting = inquire(meetingcode,current_user.username,1)
    meeting_info = meeting["meeting_info_list"]
    for item in meeting_info:
        meeting_id = item['meeting_id']
        meetingUrl= item["join_url"]
        meetingTitle= item["subject"]
        meetingStart = datetime.fromtimestamp(int(item['start_time'])).strftime('%H:%M')
        meetingEnd = datetime.fromtimestamp(int(item['end_time'])).strftime('%H:%M')
    user = User.query.filter_by(username=username).first_or_404()
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    followed_posts=Live.query.join(followers, (followers.c.followed_id == Live.user_id)).all()

    all_posts = Live.query.all()
    postId=post_id

    all_users = User.query.all()
    author = db.session.query(Live.title).join(User.posts)
    user_role = current_user.role
    seriesId = Series.query.all()
    for seriesId in seriesId:
        seriesIdNum = int(seriesId.id) + 1

    return render_template('meeting.html',seriesIdNum=seriesIdNum,meetingStart=meetingStart,meetingEnd=meetingEnd,meetingTitle=meetingTitle,postId=postId,meetingUrl=meetingUrl,meeting_id=meeting_id,meetingcode=meetingcode,followed_posts=followed_posts,user=user,user_role=user_role,all_users=all_users,all_posts = all_posts,author=author, image_file = image_file)

@app.route('/cancel/<int:meetingId>Code<int:meetingcode>',methods=['GET','POST'])
@login_required
def cancel_meeting(meetingId,meetingcode):

    cancelMeeting(meetingId,current_user.username,1)
    meeting=Live.query.filter_by(meetingCode=meetingcode).first_or_404()
    db.session.delete(meeting)

    db.session.commit()

    return redirect(url_for('user_profile',username=current_user.username))

@app.route('/<username>/<int:meetingId>id<int:post_id>',methods=['GET','POST'])
@login_required
def modify_meeting(username,meetingId,post_id):
    user = User.query.filter_by(username=username).first_or_404()
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    lesson_form = Lesson_form()
    form = Session_form()
    verify_form = Verify_form()
    seriesId = Series.query.all()
    for seriesId in seriesId:
        seriesIdNum = int(seriesId.id) + 1
    if request.method == 'POST':
        fulltime = request.form['date-time']
        fullDate = datetime.fromtimestamp(int(fulltime) / 1000).strftime('%Y-%m-%d')
        startTime = datetime.fromtimestamp(int(fulltime) / 1000).strftime('%H:%M')
        end_time = request.form['end-time']
        endTime = datetime.fromtimestamp(int(end_time) / 1000).strftime('%H:%M')

        #        start = re.split(r'([T+])', time)
        #        end = re.split(r'([T+])', end_time)#382a2a1a

        meeting = modifyMeeting(form.title.data, fulltime,end_time,meetingId,current_user.username,1 )

        meeting_info = meeting["meeting_info_list"]
        for item in meeting_info:
            meetingCode = item['meeting_code']


        post = Live.query.filter_by(id=post_id).first_or_404()
        lesson = Lesson(title=request.form['title'], description=request.form['description'])
        verify = User(id_type=verify_form.id_type.data, id_number=verify_form.id_number.data,
                      id_document=verify_form.id_document.data,
                      nationality=verify_form.nationality.data, occupation=verify_form.occupation.data,
                      email=verify_form.email.data, phone=verify_form.phone.data)

        post.title= form.title.data
        post.description= form.description.data
        post.start_time=startTime
        post.end_time=endTime
        post.date=fullDate

        db.session.commit()


        return redirect(url_for('meetingInfo', meetingcode=meetingCode, username=current_user.username,post_id=post_id))
    return render_template('modify.html',seriesIdNum=seriesIdNum,user=user,user_role = user_role,form=form,verify_form=verify_form,lesson_form=lesson_form,image_file=image_file)
@app.route('/create/<username>',methods=['GET','POST'])
@login_required
def create(username):
    user = User.query.filter_by(username=username).first_or_404()
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    lesson_form = Lesson_form()
    form = Session_form()
    verify_form = Verify_form()
    seriesId = Series.query.all()
    for seriesId in seriesId:
        seriesIdNum = int(seriesId.id) + 1
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


        post = Live(title=form.title.data, category=form.category.data, description=form.description.data, date= fullDate, start_time= startTime, end_time = endTime, author=current_user, meetingCode=meetingCode)
        lesson = Lesson(title=request.form['title'],description=request.form['description'])
        verify = User(id_type = verify_form.id_type.data,id_number = verify_form.id_number.data,id_document = verify_form.id_document.data,
                     nationality = verify_form.nationality.data,occupation = verify_form.occupation.data,email = verify_form.email.data,phone = verify_form.phone.data)

        db.session.add(post,verify)

        db.session.commit()

        return redirect(url_for('meetingInfo',meetingcode=meetingCode,username=current_user.username,post_id=post.id))
    return render_template('CREATE1.html',seriesIdNum=seriesIdNum,user=user,user_role = user_role,form=form,verify_form=verify_form,lesson_form=lesson_form,image_file=image_file)

@app.route('/available/<username>',methods=['GET','POST'])
@login_required
def available(username):
    user = User.query.filter_by(username=username).first_or_404()
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    user_role = current_user.role

    verify_form = Verify_form()
    seriesId = Series.query.all()
    for seriesId in seriesId:
        seriesIdNum = int(seriesId.id) + 1
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




        available = Available(date_available=fullDate)
        verify = User(id_type = verify_form.id_type.data,id_number = verify_form.id_number.data,id_document = verify_form.id_document.data,
                     nationality = verify_form.nationality.data,occupation = verify_form.occupation.data,email = verify_form.email.data,phone = verify_form.phone.data)

        db.session.add(available)

        db.session.commit()

        return redirect(url_for('my_profile',username=current_user.username))
    return render_template('available.html',seriesIdNum=seriesIdNum,user=user,user_role = user_role,form=form,verify_form=verify_form,image_file=image_file)


def fileRef(name):
    _, f_ext = os.path.splitext(name.filename)
    file_hex =binascii.b2a_hex(os.urandom(15))
    file_fn = file_hex + f_ext
    f = name.save(os.path.join(app.root_path, 'static/videos', file_fn))

    return f

def fileRefServer(name):

    _, f_ext = os.path.splitext(name.filename)
    file_hex =binascii.b2a_hex(os.urandom(8))
    file_fn = file_hex + f_ext
    f = name.save(os.path.join(app.root_path, 'static/videos', file_fn))

    return f

def token_bytes(nbytes):
    """Return a random byte string containing *nbytes* bytes.
    If *nbytes* is ``None`` or not supplied, a reasonable
    default is used
    >>> token_bytes(16)  #doctest:+SKIP.

    b'\\xebr\\x17D*t\\xae\\xd4\\xe3S\\xb6\\xe2\\xebP1\\x8b'
    """
    return os.urandom(nbytes)

def token_hex(nbytes):
    """Return a random text string, in hexadecimal.
    The string has *nbytes* random bytes, each byte converted to two
    hex digits.  If *nbytes* is ``None`` or not supplied, a reasonable
    default is used
    >>> token_hex(16)  #doctest:+SKIP.

    'f9bf78b9a18ce6d46a0cd2b0b86df9da'
    """
    return binascii.hexlify(token_bytes(nbytes)).decode('ascii')

@app.route('/quickuploads/<username>',methods=['POST','GET'])
@login_required
def quickupload(username):
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    user = User.query.filter_by(username=username).first_or_404()
    form = Upload_form()

    seriesId = Series.query.all()
    for seriesId in seriesId:
        seriesIdNum = int(seriesId.id) + 1
    if get_Host_name_IP('CJAY') == True:
        if request.method == 'POST':
            videoFile = request.files['video-file']
            audioFile = request.files['audio-file']
            transcriptFile = request.files['transcript-file']

            file_hex = token_hex(8)
            _, f_ext = os.path.splitext(videoFile.filename)
            file_fn = file_hex + f_ext


            videoFile.save(os.path.join(app.root_path, 'static/videos', file_fn))
            path = os.path.join(file_fn)

            upload = Upload(title=form.title.data,description=form.description.data,category=form.category.data,price= form.price.data,upload_ref=path,uploader=current_user)
            db.session.add(upload)
            db.session.commit()

            return redirect(url_for('discover', username = current_user.username))
        return render_template('quickUpload.html', user=user, seriesIdNum=seriesIdNum, user_role=user_role, form=form,
                               image_file=image_file)

    else:
        if request.method == 'POST':
            videoFile = request.files['video-file']
            audioFile = request.files['audio-file']
            transcriptFile = request.files['transcript-file']


            file_hex = token_hex(8)
            _, f_ext = os.path.splitext(videoFile.filename)
            file_fn = file_hex + f_ext
            videoFile.save(os.path.join(app.root_path, 'static/videos', file_fn))
            path = os.path.join(file_fn)
            upload = Upload(title=form.title.data,description=form.description.data,category=form.category.data,price= form.price.data,upload_ref=path,uploader=current_user)
            db.session.add(upload)

            db.session.commit()
            redirect(url_for('discover', username = current_user.username))
        return render_template('quickUpload.html',user=user,seriesIdNum=seriesIdNum,user_role=user_role,form =form,image_file=image_file)

def saveFile(fileData,location):
    file = secure_filename(fileData.filename)

    file_hex = token_hex(8)
    _, f_ext = os.path.splitext(file)
    file_fn = file_hex + f_ext

    fileData.save(os.path.join(app.root_path, 'static/'+location, file_fn))
    path = os.path.join(file_fn)
    return path



@app.route('/createcourse',methods=['POST','GET'])
@login_required
def createCourse():

    form = Upload_form()
    status = request.args.get('status', type=str)
    seriesForm = Series_form()
    episodeForm = Episode_form()
    if seriesForm.series_price.data == '':
        seriesForm.series_price.data = int(0)
        price = seriesForm.series_price.data
    else:
        seriesForm.series_price.data
        price = seriesForm.series_price.data
    if form.upload_price.data == '':
        form.upload_price.data = 0
    else:
        int(form.upload_price.data)

    if request.method == 'POST' and status == 'single':

        amount = int(form.upload_price.data)
        print(type(amount))
        print(amount)
        if  amount == 0:
            upload = Series(title=form.upload_title.data,
                            coverImage=saveFile(form.upload_coverImage.data, 'coverImages'),
                            description=form.upload_description.data, category=form.upload_category.data, status=status,
                            price=str(form.upload_price.data), upload_ref=saveFile(form.upload_fileName.data, 'videos'),
                            user_series=current_user,approved = True)
            db.session.add(upload)

            db.session.commit()
            msg = 'uploaded succsesfully'

            return msg
        elif amount > 0 :
            upload = Series(title=form.upload_title.data,
                            coverImage=saveFile(form.upload_coverImage.data, 'coverImages'),
                            description=form.upload_description.data, category=form.upload_category.data, status=status,
                            price=str(form.upload_price.data), upload_ref=saveFile(form.upload_fileName.data, 'videos'),
                            user_series=current_user,approved=False)
            db.session.add(upload)

            db.session.commit()
            msg = 'uploaded succsesfully'

            return msg




    elif request.method == 'POST' and status == 'series':
        series = Series(title=seriesForm.series_title.data, description=seriesForm.series_description.data,
                        coverImage=saveFile(seriesForm.series_coverImage.data,'coverImages'), category=seriesForm.series_category.data,
                        price=seriesForm.series_price.data,status=status, user_series=current_user)
        db.session.add(series)
        db.session.flush()

        episode = Episode(subtitle=episodeForm.subtitle.data, description=episodeForm.description.data,
                          upload_ref=saveFile(episodeForm.fileName.data,'videos'),
                          user_episode=current_user, sub=series, series_id=series.id)

        db.session.add(episode)

        db.session.commit()
        msg = 'uploaded succsesfully'
        return  msg
    return '', 204


@app.route('/verifyCourseList', methods=['POST', 'GET'])
def verifyCourseList():
    videos = Series.query.filter_by(approved = False).order_by(Series.timestamp.desc()).all()
    i = 0
    l = []
    for v in range(len(videos)):
        data = {'id': videos[i].id, 'title': videos[i].title, 'username': videos[i].user_series.username,
                'userImg': videos[i].user_series.image_file, 'category': videos[i].category, 'price': videos[i].price, 'coverImage': videos[i].coverImage,'approved': videos[i].approved,'likes':videos[i].liked.count(),'comments':videos[i].comments.count(),'isSeries':videos[i].is_series()}
        l.append(data)

        i += 1

    print(l)
    return jsonify({'result': l})

@app.route('/verifyCourse', methods=['POST', 'GET'])
def verifyCourse():
    videoId= request.args.get('videoId', type=int)
    videos = Series.query.filter_by(id=videoId).first()
    videos.approved = True
    db.session.commit()
    msg = 'Verified Successfully'
    return msg

@app.route('/disableComment', methods=['POST', 'GET'])
def disableComment():
    comment_id = request.args.get('comment_id', type=int)
    comment = Comment.query.filter_by(id=comment_id).first_or_404()
    comment.disabled = True
    msg = 'Disabled Successfully'
    return msg

@app.route('/enableComment', methods=['POST', 'GET'])
def enableComment():
    comment_id = request.args.get('comment_id', type=int)
    comment = Comment.query.filter_by(id=comment_id).first_or_404()
    comment.disabled = False
    msg = 'Enabled Successfully'
    return msg


@app.route('/checkId', methods=['POST', 'GET'])
@login_required
def checkId():
    seriesId = request.args.get('seriesId', type=str)
    lastSeries = Series.query.order_by(Series.id.desc()).first()
    return jsonify({'id':lastSeries.id})

@app.route('/getSeries', methods=['POST', 'GET'])
@login_required
def getSeries():
    series = Series.query.order_by(Series.timestamp.desc()).all()
    i = 0
    l = []

    for v in range(len(series)):
        data ={'id':series[i].id,'title':series[i].title,'host':series[i].user_series.username,'coverImg': series[i].coverImage,'userImg':series[i].user_series.image_file,'category':series[i].category}
        ep = []
        for e in series[i].episode:
            episode = {'episodeId':e.id,'seriesId':e.sub.id,'subtitle':e.subtitle}
            ep.append(episode)

        data.update({'episode':ep})
        l.append(data)
        print(data)


        i+=1


    return jsonify({'result':l})

@app.route('/getUploads', methods=['POST', 'GET'])
@login_required
def getUploads():
    video = Upload.query.order_by(Upload.timestamp.desc()).all()
    i = 0
    l = []

    for v in range(len(video)):
        data ={'id':video[i].id,'title':video[i].title,'host':video[i].user_series.username,'coverImg': video[i].coverImage,'userImg':video[i].user_series.image_file,'category':video[i].category}
        l.append(data)
        print(data)


        i+=1


    return jsonify({'result':l})

@app.route('/getUserSeries', methods=['POST', 'GET'])
@login_required
def getUserSeries():
    user_id = request.args.get('user_id', type=int)

    series = Series.query.filter_by(user_id = user_id).order_by(Series.timestamp.desc()).all()
    update_form = UpdateSeries_form()



    if request.method == 'GET':
        i = 0
        l = []

        for v in range(len(series)):
            data = {'id': series[i].id, 'title': series[i].title, 'price': series[i].price,
                    'host': series[i].user_series.username, 'coverImg': series[i].coverImage,
                    'userImg': series[i].user_series.image_file, 'category': series[i].category,
                    'totalEpisodes': len(series[i].episode),'likes': series[i].liked.count(),'totalComments': series[i].comments.count(),'isSeries':series[i].is_series()}
            ep = []
            for e in series[i].episode:
                episode = {'episodeId': e.id, 'seriesId': e.sub.id, 'subtitle': e.subtitle, 'video': e.upload_ref}
                ep.append(episode)

            data.update({'episode': ep})
            l.append(data)
            print(data)

            i += 1

    elif request.method == 'POST':
        series.title = update_form.title.data
        series.category = update_form.category.data
        series.description = update_form.description.data

    elif request.method == 'DELETE':
        series


    return jsonify({'result':l})

@app.route('/getEpisode', methods=['POST', 'GET','PUT'])
def getEpisode():
    episode_id = request.args.get('episode_id', type=int)
    episode = Episode.query.filter_by(id = episode_id).first()
    if current_user.is_authenticated:
        data = {'id': episode.id, 'seriesId': episode.sub.id,'type':episode.fileType(), 'subtitle': episode.subtitle, 'video': episode.upload_ref,'description': episode.description,'hasLikedEpisode': current_user.has_likedEpisode(episode),'likes':episode.userLikedEpisode.count()}
    else:
        data = {'id': episode.id, 'seriesId': episode.sub.id,'type':episode.fileType(), 'subtitle': episode.subtitle, 'video': episode.upload_ref,'description': episode.description,'hasLikedEpisode': False,'likes':episode.userLikedEpisode.count()}
    commentList = []
#    for c in episode.userCommentEpisode:
#        data= {'id':c.id,'content':c.content,'timestamp':c.timestamp,'username':c.author.username,'proPic':c.author.image_file,'userId':c.author.id}
#        commentList.append(data)
    data.update({'comments':commentList})
    return jsonify({'result':data})

@app.route('/editSeries', methods=['POST', 'GET','DELETE','PUT'])
@csrf.exempt
def editSeries():
    series_id = request.args.get('series_id', type=int)
    series = Series.query.filter_by(id = series_id).first()
    seriesList = Series.query.filter_by(id = series_id)
    update_form = UpdateSeries_form()
    i = 0
    l = []
    if request.method == 'GET':


        for s in seriesList:
            data = {'id': s.id, 'title': s.title, 'price': s.price,'description':s.description,
                    'host': s.user_series.username, 'coverImg': s.coverImage,
                    'userImg': s.user_series.image_file, 'category': s.category,
                    'totalEpisodes': len(s.episode)}
            ep = []
            for e in seriesList[i].episode:
                episode = {'episodeId': e.id, 'seriesId': e.sub.id,'description':e.description, 'subtitle': e.subtitle, 'video': e.upload_ref}
                ep.append(episode)

            data.update({'episode': ep})
            l.append(data)
            print(data)

            i += 1
        return data
    elif request.method == 'PUT':
        series.title = update_form.update_series_title.data
        series.category = update_form.update_series_category.data
        series.description = update_form.update_series_description.data
        series.price = update_form.update_series_price.data
        db.session.commit()

        msg = 'Updated successfully'
        return msg


    elif request.method == 'DELETE':
        for e in series.episode:
            db.session.delete(e)
            i += 1
        db.session.delete(series)
        db.session.commit()

        msg = 'Deleted Successfully'

        return msg


    return jsonify({'result':l})

@app.route('/editSchedule', methods=['POST', 'GET','DELETE','PUT'])
@csrf.exempt
def editSchedule():
    schedule_id = request.args.get('schedule_id', type=int)
    user_id = request.args.get('user_id', type=int)
    schedule = Available.query.filter_by(id = schedule_id).first()

    user = User.query.filter_by(id = user_id).first()
    i = 0
    l = []
    if request.method == 'GET':

        data = {'id': schedule.id,'date': schedule.date_available,'time': schedule.timestamp}
        bookersList=[]
        for users in schedule.userSchedule:
            bookers = {'id': users.id, 'username': users.username, 'profPic': users.image_file}
            bookersList.append(bookers)
        data.update({'bookers': bookersList})


        return jsonify({'result': data})
    elif request.method == 'POST':

        return jsonify({'result': 'updated'})

    elif request.method == 'PUT':
            meeting = inquire(schedule.meetingCode, current_user.username, 1)
            meeting_info = meeting["meeting_info_list"]
            for item in meeting_info:
                meeting_id = item['meeting_id']
            fulltime = request.form['date-time']
            fullDate = datetime.fromtimestamp(int(fulltime) / 1000).strftime('%Y-%m-%d')
            startTime = datetime.fromtimestamp(int(fulltime) / 1000).strftime('%H:%M')
            end_time = request.form['end-time']
            endTime = datetime.fromtimestamp(int(end_time) / 1000).strftime('%H:%M')

            meeting = modifyMeeting('Consultation',fulltime=fulltime,meetingId=meeting_id, username=current_user.username, end_time=end_time,instanceId=1)

            meeting_info = meeting["meeting_info_list"]
            for item in meeting_info:
                meetingCode = item['meeting_code']



            schedule.date=fullDate
            schedule.start_time=startTime
            schedule.end_time=endTime,
            schedule.meetingCode=meetingCode

            msg = 'Updated successfully'


            db.session.commit()
            return msg

    elif request.method == 'DELETE':
        schedule.user.remove(current_user)
        meeting = inquire(schedule.meetingCode,current_user.username,1)
        meeting_info = meeting["meeting_info_list"]
        for item in meeting_info:
            meeting_id = item['meeting_id']

        cancelMeeting(meeting_id, current_user.username, 1)
        db.session.delete(schedule)
        db.session.commit()
        msg = 'Deleted successfully'


        return msg



    return jsonify({'result':l})

@app.route('/editLive', methods=['POST','PUT', 'GET','DELETE'])
@csrf.exempt
def editLive():
    live_id = request.args.get('live_id', type=int)
    live = Live.query.filter_by(id = live_id).first()
    update_form = UpdateSession_form()

    if request.method == 'GET':

        data = {'id': live.id, 'title': live.title,'description': live.description, 'host': live.author.username,
                'coverImg': live.coverImage, 'userImg': live.author.image_file,
                'category': live.category, 'startTime': live.start_time, 'endTime': live.end_time,
                'date': live.date, 'meetingCode': live.meetingCode}
        bookersList=[]
        for users in live.bookers:
            bookers = {'id': users.id, 'username': users.username, 'profPic': users.image_file}
            bookersList.append(bookers)
        data.update({'bookers': bookersList})
        return jsonify({'result': data})
    elif request.method == 'PUT':
            meeting = inquire(live.meetingCode, current_user.username, 1)
            meeting_info = meeting["meeting_info_list"]
            for item in meeting_info:
                meeting_id = item['meeting_id']
            fulltime = request.form['date-time']
            fullDate = datetime.fromtimestamp(int(fulltime) / 1000).strftime('%Y-%m-%d')
            startTime = datetime.fromtimestamp(int(fulltime) / 1000).strftime('%H:%M')
            end_time = request.form['end-time']
            endTime = datetime.fromtimestamp(int(end_time) / 1000).strftime('%H:%M')

            meeting = modifyMeeting(title=update_form.update_session_title.data,fulltime=fulltime,meetingId=meeting_id, username=current_user.username, end_time=end_time,instanceId=1)

            meeting_info = meeting["meeting_info_list"]
            for item in meeting_info:
                meetingCode = item['meeting_code']


            live.title=update_form.update_session_title.data
            live.category=update_form.update_session_category.data
            live.description=update_form.update_session_description.data
            live.date=fullDate
            live.start_time=startTime
            live.end_time=endTime,
            live.meetingCode=meetingCode

            msg = 'Updated successfully'


            db.session.commit()
            return msg

    elif request.method == 'DELETE':
        meeting = inquire(live.meetingCode,current_user.username,1)
        meeting_info = meeting["meeting_info_list"]
        for item in meeting_info:
            meeting_id = item['meeting_id']

        cancelMeeting(meeting_id, current_user.username, 1)
        db.session.delete(live)
        db.session.commit()
        msg ="Deleted Successfully"


        return msg


    return '',204

@app.route('/editVideo', methods=['POST', 'GET','DELETE'])
@csrf.exempt
def editVideo():
    video_id = request.args.get('video_id', type=int)
    videos = Upload.query.filter_by(id = video_id).first()
    update_form = UpdateSeries_form()

    if request.method == 'GET':
        data = {'id': videos.id, 'title': videos.title, 'videoRef': videos.upload_ref, 'description': videos.description,
             'price': videos.price, 'userId': videos.uploader.id, 'username': videos.uploader.username,
             'userImg': videos.uploader.image_file, 'category': videos.category, 'likes': videos.liked.count(),
             'comments': videos.comments.count()}

        return jsonify({'result': data})
    elif request.method == 'POST':
        video.title = update_form.title.data
        video.category = update_form.category.data
        video.description = update_form.description.data
        return jsonify({'result': 'updated'})

    elif request.method == 'DELETE':
        db.session.delete(videos)
        db.session.commit()



        return jsonify({'result': 'deleted'})


    return jsonify({'result':'done'})


@app.route('/getUserLive', methods=['POST', 'GET','PUT'])
@login_required
def getUserLive():
    user_id = request.args.get('user_id', type=int)

    form = Session_form()
    series = Live.query.filter_by(user_id = user_id).order_by(Live.timestamp.desc()).all()
    i = 0
    l = []
    for v in range(len(series)):
        data ={'id':series[i].id,'title':series[i].title,'description':series[i].description,'host':series[i].author.username,'coverImg': series[i].coverImage,'userImg':series[i].author.image_file,'category':series[i].category,'startTime':series[i].start_time,'endTime':series[i].end_time,'date':series[i].date,'meetingCode':series[i].meetingCode,'room':series[i].meetingUrl}
        l.append(data)

        i+=1

    print(l)
    if request.method == 'POST':
        fulltime = request.form['date-time']
        fullDate = datetime.fromtimestamp(int(fulltime) / 1000).strftime('%Y-%m-%d')
        startTime = datetime.fromtimestamp(int(fulltime) / 1000).strftime('%H:%M')
        end_time = request.form['end-time']
        endTime = datetime.fromtimestamp(int(end_time) / 1000).strftime('%H:%M')


        meeting = createMeeting(form.title.data, fulltime, end_time)

        meeting_info = meeting["meeting_info_list"]
        for item in meeting_info:
            meetingCode = item['meeting_code']
            meetingUrl = item['join_url']


        post = Live(title=form.title.data, category=form.category.data, description=form.description.data,
                    date=fullDate, meetingUrl = meetingUrl, start_time=startTime, end_time=endTime, author=current_user, meetingCode=meetingCode)

        db.session.add(post)
        db.session.commit()
        msg='Created successfully'
        return msg


    return jsonify({'result':l})

@app.route('/getUserSchedule', methods=['POST', 'GET','PUT'])
@login_required
def getUserSchedule():
    user_id = request.args.get('user_id', type=int)
    user = User.query.filter_by(id = user_id).first()

    i = 0
    l = []
    for date in user.available:
        data ={'id':date.id,'date':date.date_available,'start_time':date.start_time,'end_time':date.end_time,'timestamp':date.timestamp,'meetingCode':date.meetingCode,'meetingUrl':date.meetingUrl}
        l.append(data)

        i+=1


    print(l)
    if request.method == 'POST':
        fulltime = request.form['date-time']
        fullDate = datetime.fromtimestamp(int(fulltime) / 1000).strftime('%Y-%m-%d')
        startTime = datetime.fromtimestamp(int(fulltime) / 1000).strftime('%H:%M')
        end_time = request.form['end-time']
        endTime = datetime.fromtimestamp(int(end_time) / 1000).strftime('%H:%M')

        meeting = createMeeting('Consultation', fulltime, end_time)

        meeting_info = meeting["meeting_info_list"]
        for item in meeting_info:
            meetingCode = item['meeting_code']
            meetingUrl = item['join_url']

        schedule = Available(start_time = startTime,end_time=endTime,date_available=fullDate,meetingCode=meetingCode,meetingUrl=meetingUrl)
        schedule.user.append(current_user)
        db.session.add(schedule)

        db.session.commit()
        msg = "Created successfully"
        return  msg
    return jsonify({'result':l})


@app.route('/getUserBookedSchedule', methods=[ 'GET'])
@login_required
def getUserBookedSchedule():
    user_id = request.args.get('user_id', type=int)
    user = User.query.filter_by(id = user_id).first()

    i = 0
    l = []
    for date in user.bookSchedule:
        data ={'id':date.id,'date':date.date_available,'start_time':date.start_time,'end_time':date.end_time,'timestamp':date.timestamp,'meetingCode':date.meetingCode,'meetingUrl':date.meetingUrl}
        l.append(data)

        i+=1

    print(l)

    return jsonify({'result':l})

@app.route('/getUserBookedLive', methods=[ 'GET'])
@login_required
def getUserBookedLive():
    user_id = request.args.get('user_id', type=int)
    user = User.query.filter_by(id = user_id).first()

    i = 0
    l = []
    for live in user.book:
        data ={'id': live.id, 'title': live.title,'startTime': live.start_time,'endTime': live.end_time,'date': live.date,'coverImage': live.coverImage,'description':live.description,'category': live.category,'meetingCode':live.meetingCode,'meetingUrl':live.meetingUrl}
        l.append(data)

        i+=1

    print(l)

    return jsonify({'result':l})


@app.route('/addEpisode', methods=['POST', 'GET','PUT'])
@csrf.exempt
def addEpisode():
    series_id = request.args.get('series_id', type=int)
    series = Series.query.filter_by(id = series_id).first()



    episodeForm = UpdateEpisode_form()
    episode = Episode(subtitle=episodeForm.update_subtitle.data, description=episodeForm.update_description.data,
                      upload_ref=saveFile(episodeForm.update_fileName.data,'videos'),
                      user_episode=current_user, sub=series, series_id=series.id)
    db.session.add(episode)
    series.status = 'series'
    db.session.commit()
    msg = 'Uploaded successfully'
    return msg





@app.route('/uploads/<username>',methods=['POST','GET'])
@login_required
def upload(username):
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    user = User.query.filter_by(username=username).first_or_404()
    seriesId = Series.query.all()
    for seriesId in seriesId:
        seriesIdNum = int(seriesId.id) + 1

        return render_template('UPLOADS.html',user=user,user_role=user_role,seriesIdNum=seriesIdNum,image_file=image_file)


@app.route('/series_uploads/<int:id>id<username>',methods=['POST','GET'])
@login_required
def series_upload(username,id):
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    user = User.query.filter_by(username=username).first_or_404()
    seriesForm = Series_form()
    episodeForm = Episode_form()
    seriesId = Series.query.all()
    for seriesId in seriesId:
        seriesIdNum = int(seriesId.id) + 1
    if get_Host_name_IP('CJAY') == True:
        if request.method == 'POST':
            videoFile = request.files['video-file']
            audioFile = request.files['audio-file']
            transcriptFile = request.files['transcript-file']

            if videoFile is not None:
                videoPath = fileRef(videoFile)

            if audioFile is not None:
                audioPath = fileRef(audioFile)

            if transcriptFile is not None :
                transcriptPath = fileRef(transcriptFile)




            series = Series(title=seriesForm.title.data, description=seriesForm.description.data,
                            category=seriesForm.category.data, price=seriesForm.price.data, user_series=current_user)
            db.session.add(series)

            episode = Episode(subtitle=episodeForm.subtitle.data, description=episodeForm.description.data,
                              upload_ref=videoPath,transcript_ref= transcriptPath,auido_ref=audioPath,user_episode=current_user, series_id=id)
            db.session.add(episode)

            db.session.commit()
            return redirect(url_for('discover', username = current_user.username))
        return render_template('seriesUpload.html',user=user,seriesIdNum=seriesIdNum,user_role=user_role,form =form,seriesForm=seriesForm,episodeForm=episodeForm,image_file=image_file)

    else:
        if request.method == 'POST':

            videoPath = fileRefServer('video-file')
            audioPath = fileRefServer('audio-file')
            transcriptPath = fileRefServer('transcript-file')
            #        upload = Upload(title=form.title.data,description=form.description.data,category=form.category.data,price= form.price.data,upload_ref=path,uploader=current_user)
            series = Series(title=seriesForm.title.data, description=seriesForm.description.data,
                            category=seriesForm.category.data, price=seriesForm.price.data, user_series=current_user)
            db.session.add(series)
            db.session.flush()
            episode = Episode(subtitle=episodeForm.subtitle.data, description=episodeForm.description.data,
                              upload_ref=videoPath,auido_ref = audioPath,transcript_ref=transcriptPath, user_episode=current_user, series_id=id)
            db.session.add(episode)

            db.session.commit()
            return redirect(url_for('discover', username = current_user.username))
        return render_template('seriesUpload.html',user=user,seriesIdNum=seriesIdNum,user_role=user_role,form =form,seriesForm=seriesForm,episodeForm=episodeForm,image_file=image_file)


@app.route('/lesson<int:id><username>', methods=['POST','GET'])
@login_required
def lesson(username,id):
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)

    user = User.query.filter_by(username=username).first_or_404()
    form = Lesson_form()
    post = Live.query.filter_by(id=id).first()
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
    all_posts = Live.query.all()

    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    all_users = User.query.all()

    return render_template('session_admin.html',user=user,all_users = all_users,all_posts=all_posts,user_role=user_role,image_file=image_file)

@app.route('/session_view/<int:id>',methods=['GET','POST'])
@login_required
def session_view(id):
    session_post = Live.query.filter_by(id=id).first()
    user = User.query.filter_by(id=id).first_or_404()
    comments = Comment.query.all()
    image_file = url_for('static', filename ='profile_pics/' + current_user.image_file)
    user_role = current_user.role
    all_users = User.query.all()

    return render_template('session_view.html',session_post=session_post,comments=comments,video=video,user=user,all_users = all_users,user_role=user_role,image_file=image_file)

@app.route('/session_verify/<int:id>',methods=['GET','POST'])
@login_required
def session_verify(id):
    session_post = Live.query.filter_by(id=id).first()
    session_post.verified = 1
    db.session.commit()

    return redirect(url_for('session_admin',id=session_post.id))

@app.route('/session_unverify/<int:id>',methods=['GET','POST'])
@login_required
def session_unverify(id):
    session_post = Live.query.filter_by(id=id).first()
    session_post.verified = 0
    db.session.commit()

    return redirect(url_for('session_admin',id=session_post.id))

@app.route('/video_admin/<int:id>',methods=['GET','POST'])
@login_required
def video_admin(id):
    user = User.query.filter_by(id=id).first_or_404()
    uploads  = Series.query.all()
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


@app.route('/updateFeed', methods=['GET'])
def updateFeed():
    followed_posts = current_user.followed_posts().all()

    if current_user.id not in current_user.followed_posts().all() :
        pass

    try:
        for post in followed_posts:
            updatedPosts=post
            data = jsonify({'title':updatedPosts.title,'category':updatedPosts.category,'start_time':updatedPosts.start_time,'end_time':updatedPosts.end_time,'uploader': updatedPosts.author.username})
        return data
    except:
        return jsonify({'result':'current user is not following any user'})
    pass

@app.route('/fetchSessions', methods=['GET'])
def fetchSessions():
    followed_posts = current_user.followed_posts().all()

    if current_user.id not in current_user.followed_posts().all():
        pass

    try:
        for post in followed_posts:
            updatedPosts=post
            data = jsonify({'title':updatedPosts.title,'category':updatedPosts.category,'start_time':updatedPosts.start_time,'end_time':updatedPosts.end_time,'uploader': updatedPosts.author.username})
        return data
    except:
        return jsonify({'result':'current user is not following any user'})
    pass

@app.route('/fetchPosts', methods=['GET'])
def fetchPosts():
    followed_uploads = current_user.followed_posts().all()

    if current_user.id not in current_user.followed_uploads().all():
        pass

    try:
        for post in followed_uploads:
            updatedPosts=post
            data = jsonify({'title':updatedPosts.title,'category':updatedPosts.category,'start_time':updatedPosts.start_time,'end_time':updatedPosts.end_time,'uploader': updatedPosts.author.username})
        return data
    except:
        return jsonify({'result':'current user is not following any user'})
    pass

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Requset',
                  sender=authentication,
                  recipients=[user.email])
    url = {url_for('reset_token',token=token,_external=True)}
    message = "Follow the link to reset your password.The link will expire in 5 minutes\n"
    msg.body = "%s\n%s" % (message , url)
    mail.send(msg)

@app.route('/reset_password' , methods=['POST','GET'])
def reset_request():
    form = Request_reset(request.form)
    if  request.method == 'POST':
        user = User.query.filter_by(email = form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent to your mail')
    return render_template('request_reset.html', form =form)

@app.route('/reset_password/<token>' , methods=['POST','GET'])
def password_token(token):
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token','warning')
        return redirect(url_for('reset_request'))
    form = Reset_password()
    if form.validate_on_submit() and request.method == "POST":

        hashed_password = hash_password(form.password.data)
        user.password = hashed_password
        db.session.commit()
        flash('Updated')

        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)


if __name__ == '__main__':

    app.run()

