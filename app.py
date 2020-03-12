'''
Copyright (c) Project TemperStat. All rights reserved.
by Aditya Borgaonkar & Sahil Gothoskar, 2020.

https://github.com/adityaborgaonkar
https://github.com/SahilGothoskar

'''

#import csv
#import smtplib
#from email.mime.multipart import MIMEMultipart
#from email.mime.base import MIMEBase
#from email.mime.text import MIMEText
#from email.utils import COMMASPACE
#from email import encoders

from flask import render_template, url_for, request
import Adafruit_DHT
pin = 17
sensor = Adafruit_DHT.DHT11


from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    temperature, humidity = sensor_1()
    return render_template("index.html",temperature=temperature, humidity=humidity)

def sensor_1():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        return temperature, humidity


if __name__ == "__main__":
    app.run(debug=True)

'''
time, temperature, humidity = "12:45","30 Deg Cel","45%"

with open('readings.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "Temperature", "Humidity"])
    writer.writerow([time, temperature, humidity])
    writer.writerow(["12:46", "32 Deg Cel", "51 %"])
    writer.writerow(["12:47", "33 Deg Cel", "65 %"])


# sgothoskar967@gmail.com
# borg.aditya@gmail.com

SUBJECT = 'IOT Project :: TemperStat Readings'
FILENAME = 'readings.csv'
FILEPATH = 'readings.csv'
MY_EMAIL = 'temperstat@gmail.com'
MY_PASSWORD = input()
TO_EMAIL = 'ksanket1998@gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

msg = MIMEMultipart()
msg['From'] = MY_EMAIL
msg['To'] = COMMASPACE.join([TO_EMAIL])
msg['Subject'] = SUBJECT

part = MIMEBase('application', "octet-stream")
part.set_payload(open(FILEPATH, "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename=FILENAME)
msg.attach(part)

smtpObj = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(MY_EMAIL, MY_PASSWORD)
smtpObj.sendmail(MY_EMAIL, TO_EMAIL, msg.as_string())
smtpObj.quit()

'''



