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


@app.route("/pro48_api/")
@app.route("/pro48_api/<path:idol_name>")
def pro48_api(idol_name="다 같이"):
    try:
        result = idol_name + " 파이팅!"
    except:
        result = "예외란다"

    return result


# slack outgoing webhook
# @app.route("/slack", methods=['POST'])
# def slack():
#     username = request.form.get('user_name')
#     token = request.form.get('token')
#     text = request.form.get('text')
#
#     if "날씨" in text:
#         summary = forecast()
#         send_slack(summary)
#
#     print(username, token, text)


if __name__ == '__main__':
    app.run()



