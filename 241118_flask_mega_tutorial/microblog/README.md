# Flask Mega Tutorial

> Date: 2024-11-18

## 설치

#### 가상 환경 구성

`venv` 이용하여 가상환경을 구성

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

#### Python 패키지 설치

```bash
$ pip install -r requirements.txt
```

## 설정

### 이메일 전송 설정

`DEBUG` 모드가 아닐 때, 발생한 오류를 관리자의 이메일로 전송하는 기능

-   아래의 1, 2번 중 택 1

#### 1. 가짜 SMTP 서버 구성

`aiosmtpd` 을 이용하여 가짜 SMTP 서버를 구성하는 방식으로
이메일을 수신하지만 실제로 전송하지는 않고 `logs` 폴더에 로그 파일 생성

-   설치 및 실행 방법

```bash
$ pip install aiosmtpd
$ aiosmtpd -n -c aiosmtpd.handlers.Debugging -l localhost:8025
```

#### 2. Google 계정으로 이메일 전송

오류 발생 시 실제로 이메일을 전송하는 방식

-   `config.py`

    -   `ADMINS`: 오류 로그를 받을 관리자 이메일로 변경

-   환경 변수

    -   `{GMAIL_ID}`: Google ID
    -   `{GMAIL_APP_PASSWORD}`: 2단계 인증을 한 계정으로 앱 비밀번호를 생성

```bash
export MAIL_SERVER=localhost
export MAIL_PORT=8025
export MAIL_SERVER=smtp.googlemail.com
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_USERNAME={GMAIL_ID}@gmail.com
export MAIL_PASSWORD={GMAIL_APP_PASSWORD}
```

## 테스트

### API 테스트

-   `HTTPie` 설치

```
pip install httpie
```

-   공통

```
http -A bearer --auth <tokens> {HTTP_METHOD} http://localhost:5000/{API_ENDPOINT}
```

-   Auth

    -   토큰 생성: `POST /tokens`
        ```
        http --auth <username>:<password> POST http://localhost:5000/api/tokens
        ```
    -   토큰 만료: `DELETE /tokens`

-   User
    -   회원 조회: `GET /users/:id`
    -   회원 목록: `GET /users`
    -   회원 등록: `POST /users`
    -   회원 수정: `PUT /users/:id`
-   Follow
    -   팔로워 목록: `GET /users/:id/followers`
    -   팔로잉 목록: `GET /users/:id/following`
