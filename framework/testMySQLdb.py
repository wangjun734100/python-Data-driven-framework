import pymysql.cursors
from framework import readConfigFile

class Mysql(object):
    config = readConfigFile.ReadConfig()
    host = config.get_db("host")
    port = config.get_db("port")
    username = config.get_db("username")
    password = config.get_db("password")
    database = config.get_db("database")
    port = int(port)

    def get_sql(self, sql):
        connection = pymysql.connect(host=self.host, port=self.port, user=self.username, passwd=self.password, db=self.database,
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        try:
            cursor = connection.cursor()
            sql = sql
            cursor.execute(sql)
            results = cursor.fetchall()
            for data in results:
                return data

        except Exception:
            print("失败")
        cursor.close()
        connection.close()



if __name__=='__main__':
    sql="select * from emplayee"
    p = Mysql().get_sql(sql)
    print(p)
