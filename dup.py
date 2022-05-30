# import datetime


# strTime = datetime.datetime.now().strftime("%H:%M:%S")
# print(strTime)

import smtplib

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(mail, pas)
    server.sendmail(mail, to, content)
    server.close()

with open("in.txt", "r") as m:
    mail = m.readline()
    # print(mail)
with open("p.txt", "r") as p:
    pas = p.readline()
    # print(pas)


try:
    # speak("What should I say?")
    # content = takecommand()
    content = "This is practice mail"
    to = "bhargavshivashankar@gmail.com"
    sendEmail(to, content)
    # speak("Email has been sent!")
    print("Email has been sent!")

except Exception as e:
    print(e)
    # speak("Sorry, I am not able to send this email")
    print("Sorry, I am not able to send this email")
        