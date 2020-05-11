import smtplib
import datetime

#DO NOT NAME email.py becouse email is module in python

#print(dir(smtplib.SMTP()))
''' Send mail to DebuggingServer '''
# command sudo python3 -m smtpd -c DebuggingServer -n localhost:1025


# constants for email
SEVER = 'localhost'
# port in DebbugingServer
PORT = 1025

FROM = 'mydevice@mail.com'
TO = 'reveicer@mail.com'

def scraperMail(insertednum):
    message = '''\
    FROM = %s
    TO = %s
    Subject = %s

    %s
    ''' % (FROM,TO,'Web scpraper',str(insertednum)+' number of inserted time: '+str(datetime.datetime.now()))

    #help(smtplib.SMTP_SSL)


    try:
        with smtplib.SMTP(SEVER,PORT) as server:
            server.sendmail(FROM,TO,message)
            server.quit()
    except Exception as e:
        print(e)