import mysql.connector as mysql

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

    mysqlcursos = connect.cursor()

    sql = "Insert into guitars(name,price,created) values(%s,%s,%s)"

    mysqlcursos.executemany(sql,data)

    connect.commit()

    print(mysqlcursos.rowcount, "insertovanih")