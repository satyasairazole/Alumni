from flask import Flask,render_template,url_for,redirect
from Almod.forms import LoginForm

from  flask_login import LoginManager, login_required,logout_user,login_user
from Almod import app
from Almod.models import alumnidata
#FOR FLASK AUTHENTICATION
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='login_page'


@login_manager.user_loader
def load_user(user_id):
    return alumnidata.query.get(user_id)
#------------------------




@app.route('/',methods=['GET','POST'])
@login_required
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login_page():
    form=LoginForm()
    if form.validate_on_submit():
        user=alumnidata.query.filter_by(username=form.username.data,password=form.password.data).first()
        if user:
            
            login_user(user)
            return redirect(url_for("home"))
    return render_template('login.html',form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login_page'))

@app.route("/reset")
def reset():
    return render_template('reset.html')

#forgot the password
@app.route('/forgot_password')
def forgot():
    return render_template('forgo.html')

#userprofile
@app.route('/user/profile')
def user_profile():
    return render_template('user.html')