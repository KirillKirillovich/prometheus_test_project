# prometheus_test_project
Simple app for test prometheus + grafana + alertmanager. 'request_script.py' will send ten 404(telegram bot will send u alert). Every 10 seconds 'request_script.py' will make a random request. You can check all requests info in presetuped grafana flask dashboard.

Open Telegram application then search for @BotFather
Click Start
Click Menu -> /newbot or type /newbot and hit Send
Follow the instruction until we get message like so 
```
Done! Congratulations on your new bot. You will find it at t.me/new_bot.
You can now add a description.....

Use this token to access the HTTP API:
74xxxxxx71:AAFoxxxxn0hwA-2TVSxxx9bhA
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api
```
```
bot_token: '74xxxxxx71:AAFoxxxxn0hwA-2TVSxxx9bhA'
```
Next go to:
```
https://api.telegram.org/bot74xxxxxx71:AAFoxxxxn0hwA-2TVSxxx9bhA/getUpdates
```
And find 'chat_id' <br>
```
chat_id: 46xxxxx82
```
Change bot data in 'alertmanager.yml':
```
receivers:
  - name: 'telegram'
    telegram_configs:
      - send_resolved: true
        bot_token: 'xxxxxxx'
        chat_id: xxxxx
        message: |
          {{ range .Alerts }}
            *Alert:* {{ .Annotations.summary }} 
            *Description:* {{ .Annotations.description }} 
            *Status:* {{ .Status }} 
            *Starts At:* {{ .StartsAt }}
          {{ end }}
```

usage:

1) docker compose up --build -d
2) http://localhost:5000 - flask app include routes:
+ /main - return page with 200 status code
+ /2x-code - return page with 200 status code
+ /4x-code - return page with 404 status code
+ /5x-code - return page with 500 status code
3) http://localhost:3000 - grafana page (username: admin, password: admin - for login)
4) http://localhost:9090 - prometheus page