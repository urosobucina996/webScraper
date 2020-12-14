import mysql.connector as mysql
from modules import emailSender
from modules import loggingScrape
import os


#mysql connection form my database
try:
    connect = mysql.connect(
        host = '127.0.0.1',
        port=3306,
        user = 'uros',
        #ubaci sifru u lokalni enviroment i odatle je izvadi da ne bude transaprentna u kodu
        password = os.environ['DB_PASS'],
        database = 'script',
        auth_plugin='mysql_native_password'
    )
except Exception as e:
    loggingScrape.logging.error(f'Database error: {e}')

def execute_query(data):

    # Try and catche database mistakes

    # pravi se kursor kao u terminalu da bi mu prosledio upit, tj. tekst u varijabli sql
    mysqlcursos = connect.cursor()

    # INSERT IGNORE je da se ne bi pravili duplikati imena u bazi
    sql = "INSERT IGNORE INTO guitars(name,price,created) values(%s,%s,%s)"

    mysqlcursos.executemany(sql,data)

    connect.commit()

    connect.close()

    emailSender.scraper_mail(mysqlcursos.rowcount)
