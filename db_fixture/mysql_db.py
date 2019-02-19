# coding=utf8
import pymysql.cursors
import os
import configparser as cparser


# ======== Reading db_config.ini setting ===========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"

cf = cparser.ConfigParser()

cf.read(file_path)
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")


# ======== MySql base operating ===================
class DB:

    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # clear table data
    # def clear(self, table_name):
    #     # real_sql = "truncate table " + table_name + ";"
    #     real_sql = "delete from " + table_name + ";"
    #     with self.connection.cursor() as cursor:
    #         cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
    #         cursor.execute(real_sql)
    #     self.connection.commit()

    # insert sql statement
    def insert(self, table_name, table_data):
        # print(type(table_data))
        # print (table_data)
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        # print(type(key))
        # print(key)
        value = ','.join(table_data.values())
        # print(type(value))
        # print(value)
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

    # close database
    def close(self):
        self.connection.close()

    # init data
    def init_data(self, datas):
        for table, data in datas.items():
            #dict.items()后，table是string的库表名字，data是每张表的list[]数据。
            # self.clear(table)
            # print (table,data)
            for d in data:
                self.insert(table, d)
        self.close()


if __name__ == '__main__':

    db = DB()
    table_name = "contentdata"

    data = {'content_id': 'test', 'content_type': 7}
    # data = {'id':14,'match_id':'123','title':'test','brief':'haha','image':'http://image.sports.baofeng.com/63970a88457529ec9ad75c74968ba50a','large_image':'http://image.sports.baofeng.com/63970a88457529ec9ad75c74968ba50a'}
    # table_name2 = "sign_guest"
    # data2 = {'realname':'alen','phone':12312341234,'email':'alen@mail.com','sign':0,'event_id':1}

    # db.clear(table_name)
    db.insert(table_name, data)
    db.close()


