import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# 보내는 사람 정보
me = "아이디@gmail.com"
my_password = "비번"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보
email_list = ["coookieee99@naver.com", "dana_kim@kakao.com"]

for you in email_list:
    # 메일 기본 정보 설정
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "제목"
    msg['From'] = me
    msg['To'] = you

    # 메일 내용 쓰기
    content = "메일 내용"
    part2 = MIMEText(content, 'plain')
    msg.attach(part2)

    part = MIMEBase('application', "octet-stream")
    with open("articles.xlsx", 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment", filename="추석기사.xlsx")
    msg.attach(part)

# 메일 보내기
s.sendmail(me, you, msg.as_string())

# 다 끝나고 닫기
s.quit()