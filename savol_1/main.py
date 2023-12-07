"""
redis =  kirib kelgan malumotlarni bir qancha vaxt keshda saqlab database ishini tezlashtirishimiz mumkin

celrey  =  background tasklarni bajaradi bizning asosiy  daturga  xalaqit bermagan gholda beckrounda
            buyurilgan malumotlarni bajaradi misol uchun 10000 ta emailga smsm yuborish kerak bolib qolsa  biz asosyiy
            dasturimiz orqali yuborsak ancha kutib qolamiz beckrounda tashlasak dasturimizga xalaqit bermaydi

crontab  =  malum bir vaqtda berilgan cammandani bajaradi

"""
import smtplib
import ssl
import time

from celery import Celery

app = Celery('hello', broker='pyampq://localhost:6379/0')


@app.task
def send_emaile_celery():
    port = 465
    smtplib_server = "smtp.gmail.com"
    from_email = "aralovjavoxir@gmail.com"
    receiver_email = "aralov javoxir"
    password = "klixiawcmtmlvyod"
    message = "assalomu alekum "

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtplib_server, port, context=context) as server:
        print(server.login(from_email, password))
        server.sendmail(from_email, receiver_email, message)
    return message


send = [send_emaile_celery]
for i in send:
    i.delay()
    print(10)
