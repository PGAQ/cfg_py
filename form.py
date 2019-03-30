from flask import Flask, render_template, request
#import from flask library the specific file named "Flask", render template=?, request=?
app = Flask("MyApp")
# I have "Myapp" and i'm calling this "app"
@app.route("/") # any @ is called a decorator. THE CODE BELOW @ROUTE IS JUST FOR A SPECIFIC PART OF MY WEBSITE.
def hello():
    return "Hello World"

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())

@app.route("/signup", methods =["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    return "All OK"

app.run(debug=True) # if i don't tell my app to run it's not going to strat the server. in order for it to work i need to tell it to run.
# debug mode is for errors, tells me what is wrong in my code.

# after coping this to the terminal i can copy the http address and run it on my browser . the file is local!

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_folder='/home/dubspher/mysite/')

@app.route('/')
def static_file():
    return app.send_static_file('templates/index.html')

if __name__ == "__main__":
    app.run()

    app = Flask(__name__, static_url_path="/static", static_folder='/home/dubspher/mysite/static')

@app.route('/')
def static_file():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run()
