from twilio.rest import Client
# 配置twilio给自己手机发送消息

# sid
account_sid = ""
# token
auth_token = ""
client = Client(account_sid, auth_token)

message = client.messages.create(
    # 已经验证过的手机号
    to="",
    # twilio手机号
    from_="",
    # 发送的消息
    body='',
)

print(message.sid)
