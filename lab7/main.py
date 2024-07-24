from flask import Flask, render_template, redirect, url_for, flash
from form import RegisterForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, UserMixin, login_required

app = Flask(__name__)

app.config['SECRET_KEY'] = '538jfnrpiwhrlkj534dfogrgrt2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)

#database 

#login manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Email('{self.email}')"


#routes
@app.route('/secret')
@login_required
def secret():
    return render_template('secret.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()
    if form.validate_on_submit():
        user = User(firstname = form.firstname.data, lastname = form.lastname.data, email=form.email.data, password= form.password.data)
        db.session.add(user)
        db.session.commit()
        print("Success")
        return redirect(url_for('thankyou'))

    return render_template('register.html', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('secret'))
        else:
            flash('Invalid email address or password')

    return render_template('login.html', form = form)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)



