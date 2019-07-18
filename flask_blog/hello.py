from flask import Flask, render_template, url_for

app = Flask(__name__)
posts = [
      {
      'author':'sujay',
      'title':'blog post 1',
      'content':'first blog content',
      'date_posted':"january"
      },
      {
      'author':'Amith',
      'title':'blog post 2',
      'content':'second  blog content',
      'date_posted':"february"
      }   
    ]

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html", title="AboutPage")

if __name__=='__main__':
    app.run(debug=True)