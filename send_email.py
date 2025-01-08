import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "ahmadtw213@gmail.com"
password = "qqbabcpihfnygzjs"

receiver = "app8flask@gmail.com"
my_context = ssl.create_default_context()

message = """
Hi!
How are you?
Bye!
"""
with smtplib.SMTP_SSL(host, port, context=my_context) as server:
    server.login(username, password)
    server.sendmail(username, username, message)