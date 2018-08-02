from flask import *

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask"

# html webpage
@app.route("/user/<username>")
def user(username):
    return render_template("profile.html", name=username)

# json format api
@app.route("/people")
def people():
    people = {
        "alice":25,
        "jin":[{"age":35},{"email":"pdj@daum.net"}]
    }
    return jsonify(people)

@app.route("/pro48_api/<idol_name>")
def pro48_api(idol_name):

    result = idol_name + " 파이팅!"

    return result

app.run()
