from flaskblog import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)





# from datetime import datetime
# from flask import Flask, render_template, url_for, flash, redirect
# from flask_sqlalchemy import SQLAlchemy
# from forms import RegistrationForm,LoginForm
# app = Flask(__name__)

# app.config['SECRET_KEY'] = '01b385dd834398f503b0be5f5743d58f'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(20), unique = True, nullable=False)
#     email = db.Column(db.String(120), unique = True, nullable=False)
#     image_file = db.Column(db.String(20),nullable = False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)
#     posts = db.relationship('Post',backref='author', lazy=True)

#     #dunder / magic methods
#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

#     def __repr__(self):
#         return f"Post('{self.title}','{self.date_posted}')"


# #dummy data
# posts= [
#     {
#         'author': 'Sujal Vaishnav',
#         'title': 'Blog post 1',
#         'content':'First post content',
#         'date_posted':'March 17, 2025'
#     },
#     {
#         'author': 'Hiren Vaishnav',
#         'title': 'Blog post 2',
#         'content': 'Second Blog post content',
#         'date_posted': 'March 18, 2025'
#     }
# ]

# @app.route("/")
# @app.route("/home")
# def home():
#     return render_template('home.html',posts=posts)

# @app.route("/about")
# def about():
#     return render_template('about.html', title='About')

# @app.route("/register",methods=['GET','POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('register.html', title='Register', form=form)

# @app.route("/login",methods=['GET','POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!','success')
#             return redirect(url_for('home'))
#         else:
#             flash('Login unsuccessful. Please check username and password', 'danger')
#     return render_template('login.html', title='Login', form=form)

# if __name__ == "__main__":
#     app.run(debug=True)