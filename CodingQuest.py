from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import configparser

# 설정 파일 읽기
config = configparser.ConfigParser()
with open("config.ini", 'r', encoding='utf-8') as file:
    config.read_file(file)

# 설정값 가져오기
SLACK_BOT_TOKEN = config['slack']['SLACK_BOT_TOKEN']
SLACK_SIGNING_SECRET = config['slack']['SLACK_SIGNING_SECRET']
SLACK_APP_TOKEN = config['slack']['SLACK_APP_TOKEN']
channel_name = config['slack']['channel_name']

app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET
)


# 각종 이벤트를 annotation 안에 설정하면 된다.
@app.event("message")
@app.event("app_mention")
def message_handler(message, say):
    say(f"Hello <@{message['user']}>")


if __name__ == "__main__":
    # ※ 주의 : APP 토큰이다.
    SocketModeHandler(app, SLACK_APP_TOKEN).start()