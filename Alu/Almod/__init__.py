from flask import Flask,render_template;
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///alumnidata.db'
app.config['SECRET_KEY']='dataofrguktalumni'
db=SQLAlchemy(app)
from Almod import route