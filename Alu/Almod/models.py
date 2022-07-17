from Almod import db
from flask_login import UserMixin
class alumnidata(db.Model,UserMixin):
    s=db.Column(db.Integer,nullable=False)
    id=db.Column(db.String(10),primary_key=True)
    name=db.Column(db.String(10),nullable=False)
    sec=db.Column(db.String(5),nullable=False)
    gender=db.Column(db.String(6),nullable=False)
    mail=db.Column(db.String(50),nullable=False,unique=True)
    username=db.Column(db.String(30),nullable=False,unique=True)
    password=db.Column(db.String(60),nullable=False)
    image=db.Column(db.String(60),nullable=False)
    imagedir=db.Column(db.String(60),nullable=False)
    #def __repr__(self):
       # return f'Item{self.name}'

