## CodingQuest 슬랙봇

※공사중...※
### 개발 일지
#### 2024-04-03
  - 작업 내용 : 
    - 예약된 시간에 메시지 전송, 봇 호출 시 호출한 사용자에게 인사하는 기능 테스트
    - 토큰과 같은 민감한 정보 관리 위해 config.ini 파일 추가, gitignore 설정
  - 변경 사항 : 작업 내용과 동일
  - 해결한 문제 : 없음
  - 다음 단계 :
    - 코딩테스트 사이트에서 문제 랜덤 하나 뽑아오기
    - 문제 개수 범위 내에서 랜덤 숫자 뽑아서 링크 생성해 보내주는 방법도 생각해보자
    - 서버에 어떻게 올릴 것인지 고민
    - 멘션이나 호출이 가능하게 할 것인지 고민

### 파이참 환경 설정
- python 3.8 환경에서 개발 중
- slack_sdk, slack_bolt, schedule 라이브러리 설치
```
pip install slack_sdk
pip insatll slack_bolt
pip install schedule
```

### 슬랙 환경 설정
해당 사이트들 참고
- [이벤트 처리](https://getitall.tistory.com/entry/Python-%EC%8A%AC%EB%9E%99-Slack-%EB%A9%94%EC%8B%A0%EC%A0%80-%EB%B4%87-%EB%A7%8C%EB%93%A4%EA%B8%B0-%EC%BD%94%EB%93%9C-%ED%8F%AC%ED%95%A8-%EC%B4%88%EA%B0%84%EB%8B%A8-%EC%BD%94%EB%94%A9)
- [단순 메시지 전송](https://yunwoong.tistory.com/129)

#### 설정한 권한 목록
```
app_mentions:read, channels:history, channels:read, chat:write, groups:history, groups:read, im:history, im:read, mpim:history, mpim:read
```
### 구현 내용


### 개발 기간
2024-04-03 ~ ing