import mysql.connector as mysql
from modules import emailSender

#mysql connection form my database
connect = mysql.connect(
    host = '127.0.0.1',
    port=3306,
    user = 'uros',
    password = 'uros',
    database = 'script',
    auth_plugin='mysql_native_password'
)

def executeQuery(data):

    # Try and catche database mistakes
    mysqlcursos = connect.cursor()

    # INSERT IGNORE je da se ne bi pravili duplikati imena u bazi
    sql = "Insert IGNORE into guitars(name,price,created) values(%s,%s,%s)"

    mysqlcursos.executemany(sql,data)

    connect.commit()

    connect.close()

    emailSender.scraperMail(mysqlcursos.rowcount)