import os
import requests
import urllib.parse
import re

from flask import *

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

SECRETS_PATH = os.path.join(ROOT_DIR, 'secrets/secrets.json')
YOUTUBE_SECRET_KEY = json.loads(open(SECRETS_PATH).read())["YOUTUBE_SECRET_KEY"]

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
        "alice": 25,
        "jin": [{"age": 35}, {"email": "pdj@daum.net"}]
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


@app.route("/pro48_vote_api/", methods=['GET', 'POST'])
def pro48_vote_api(idol_name="모두"):
    if request.method == 'POST':
        data = request.get_json()

        result = str(data['name']) + " 에게 " + str(data['vote_cnt']) + " 투표 완료"

    else:
        result = idol_name + "에게 기본 1표가 투표되었습니다."

    return result

@app.route("/pro48_vote_task_api/", methods=['POST'])
def pro48_vote_task_api():
    header = request.headers
    entities_str = urllib.parse.unquote(header["X-Kaa-Userentity"])

    # 값만 파싱
    entities_str = entities_str[2:].split("&")
    entities_val = [x.split("=")[::-2][0] for x in entities_str]

    result = entities_val[0] + " 에게 " + entities_val[1] + " 투표 완료"

    return result


@app.route("/pro48_youtube_api/<query>")
def pro48_youtube_api(query):

    # 수정할것 있음
    youtube_base_url = "https://www.googleapis.com/youtube/v3/search?part=snippet&&key="+YOUTUBE_SECRET_KEY+"&q="
    youtube_api_url = youtube_base_url + query

    result = requests.get(youtube_api_url).json()
    youtube_video_id = result["items"][0]["id"]["videoId"]

    return "https://www.youtube.com/watch?v="+youtube_video_id


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
