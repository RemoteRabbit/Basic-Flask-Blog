from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app =  Flask(__name__)
## Will be an env later with new key
app.config['SECRET_KEY'] = 'e83889d49dabe0e9b204a70e20a0aa90'

post = [
    {
        'author': 'Tristan',
        'title': 'blog post 1',
        'content': 'first post content',
        'dateposted': 'today'
    },
    {
        'author': 'Jim',
        'title': 'blog post 2',
        'content': 'second post content',
        'dateposted': 'yesterday'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = post)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@admin.com' and form.password.data == 'admin':
            flash("You've been logged in!", 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed, please check username and password.', 'danger')
    return render_template('login.html', title = 'Login', form = form)


#############################
if __name__ == "__main__":
    app.run(debug = True)