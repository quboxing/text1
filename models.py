from exts import db
from datetime import datetime
class User(db.Model):#Modek是M是大写
    __tablename__='user'
    # id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(3),primary_key=True,nullable=False)
    phone=db.Column(db.String(11),nullable=False)
    username=db.Column(db.String(11),nullable=False)
    password=db.Column(db.String(11),nullable=False)
class Text(db.Model):
    __tablename__='text'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(100),nullable=False)
    content=db.Column(db.Text,nullable=False)
    time=db.Column(db.DateTime,default=datetime.now)
    author_name=db.Column(db.String(3),db.ForeignKey('user.name'))
    author=db.relationship('User',backref=db.backref('text'))
class Pinglun(db.Model):
    __tablename__='pinglun'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    pinglun=db.Column(db.Text,nullable=False)
    text_id=db.Column(db.Integer,db.ForeignKey('text.id'))
    time=db.Column(db.DateTime,default=datetime.now)
    author_name=db.Column(db.String(3),db.ForeignKey('user.name'))
    text=db.relationship('Text',backref=db.backref('pinglun1'))
    user=db.relationship('User',backref=db.backref('pinglun2'))

