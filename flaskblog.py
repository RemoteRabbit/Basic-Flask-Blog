from flask import Flask, render_template, url_for

app =  Flask(__name__)

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




#############################
if __name__ == "__main__":
    app.run(debug = True)