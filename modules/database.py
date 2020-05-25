import mysql.connector as mysql
from modules import emailSender
from modules import loggingScrape

#mysql connection form my database
try:
    connect = mysql.connect(
        host = '127.0.0.1',
        port=3306,
        user = 'uros',
        password = 'uros',
        database = 'script',
        auth_plugin='mysql_native_password'
    )
except Exception as e:
    loggingScrape.logging.error(f'Database error: {e}')

def executeQuery(data):

    # Try and catche database mistakes
    mysqlcursos = connect.cursor()

    # INSERT IGNORE je da se ne bi pravili duplikati imena u bazi
    sql = "Insert IGNORE into guitars(name,price,created) values(%s,%s,%s)"

    mysqlcursos.executemany(sql,data)

    connect.commit()

    connect.close()

    emailSender.scraperMail(mysqlcursos.rowcount)