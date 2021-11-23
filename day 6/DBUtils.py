import pymysql

host = 'localhost'
user = 'root'
password = ''
database = 'bank'

def update(sql, param):
    # 连接mysql
    con = pymysql.connect(host=host, user=user, password=password, database=database)

    # 创建控制台
    cursor = con.cursor()

    # 执行
    cursor.execute(sql, param)

    # 提交到数据库
    con.commit()

    # 关闭资源（后开的先关，先开的后关）
    cursor.close()
    con.close()


def select(sql, param, mode="all", size=1):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, param)

    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)

    con.commit()
    cursor.close()
    con.close()

def create(sql):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    cursor.close()
    con.close()