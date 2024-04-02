import schedule
import time

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from datetime import datetime
import configparser

# 설정 파일 읽기
config = configparser.ConfigParser()
with open("config.ini", 'r', encoding='utf-8') as file:
    config.read_file(file)

# 설정값 가져오기
slack_token = config['slack']['SLACK_BOT_TOKEN']
channel_name = config['slack']['channel_name']
text = config['slack']['text']
reservation = config['slack']['reservedTime']

# 슬랙 웹 클라이언트
slack_client = WebClient(token=slack_token)


# 메시지 전송, 실패 시 오류 메시지 출력
def send_message():
    try:
        slack_client.chat_postMessage(
            channel=channel_name,
            text=text
        )
        print("메시지를 성공적으로 전송했습니다.", datetime.now())
    except SlackApiError as e:
        print(f"메시지 전송 실패: {e.response['error']}")


# 매일 특정 시각 메시지 전송 예약
def job():
    print("메시지 전송을 예약합니다. 예약 시간 : ", reservation)
    schedule.every().day.at(reservation).do(send_message)


def main():
    job()

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()

