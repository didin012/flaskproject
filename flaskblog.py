from flask import Flask, render_template, url_for

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 25, 2023'
    },
    {
        'author': 'Aldrin Astronomo',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Feb 27, 2023'
    }
]

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
    