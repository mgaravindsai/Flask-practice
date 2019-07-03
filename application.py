from flask import Flask,url_for, request ,render_template

app = Flask(__name__)

post_id=1

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/hello')
@app.route("/hello/<name>")
def home(name=None):
    return render_template("hello.html",name=name)
    
@app.route('/user/<username>')
def profile(username):
    return f"Projects {username}"

@app.route('/about/<int:number>')
def number(number):
    return f"<h1> About {number} </h1>"


@app.route('/projects/')
def projects():
    return "projects"

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        return render_template("hello.html",username=username)
    else:
        return "Show the login page"

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next='/'))
    print(url_for('profile',username='Sai')) 
    

