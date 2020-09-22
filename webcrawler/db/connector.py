import pymysql


def insert(conn, data) :
    db = pymysql.connect(user=conn['user'],passwd=conn['passwd'],host=conn['host'],db=conn['db'],charset=conn['charset'])
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = "select count(*) from location where city = %s and district = %s and name = %s"
    cursor.execute(sql, #### 넣기)
    result = cursor.fetchall()
    if reulst[0] != 0 :
        return False
    else :
        sql = "insert into location values in  "#### 만들기
        cursor.execute(sql, ###넣기)
        db.commit()
