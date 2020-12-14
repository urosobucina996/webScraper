import smtplib
import datetime
import sys
from modules import loggingScrape

#DO NOT NAME email.py becouse email is module in python

#print(dir(smtplib.SMTP()))
''' Send mail to DebuggingServer '''
# command sudo python3 -m smtpd -c DebuggingServer -n localhost:1025


# constants for email testing
SEVER = 'localhost'
# port in DebbugingServer
PORT = 1025

#SEVER = 'smtp.gmail.com'
#PORT = 587

FROM = 'obucina.uros.1@gmail.com'
TO = 'urkeo196@gmail.com'

def scraper_mail(insertednum):
    message = '''\
    FROM = %s
    TO = %s
    Subject = %s

    %s
    ''' % (FROM,TO,'Web scpraper',str(insertednum)+' number of inserted time: '+str(datetime.datetime.now()))

    #help(smtplib.SMTP_SSL)


    try:
        with smtplib.SMTP(SEVER,PORT) as server:
            
            # using gmail
            #server.starttls()
            #server.login('email','password')
            
            server.sendmail(FROM,TO,message)
            
            server.quit()
    except Exception as e:
        loggingScrape.logging.error(f'Email error {e}')