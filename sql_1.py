import mysql.connector

conn = mysql.connector.connect(user='root', password='2786270', database='py_learn')
print(conn)

def create_table():
    sql1 = 'create table User(uid integer primary key auto_increment, username text, password text)'
    try:
        cursor = conn.cursor()
        cursor.execute(sql1)
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def add_data():
    sql2 = 'insert into User(username, password) values("sunny", "2786270")'
    try:
        cursor = conn.cursor()
        cursor.execute(sql2)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def delete_data(uid):
    sql3 = 'delete from User where uid = {0}'.format(uid)
    try:
        cursor = conn.cursor()
        cursor.execute(sql3)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
def update_data(username, password, uid):
    sql4 = 'update User set username="{0}", password="{1}" where uid = {2}'.format(username, password, uid)
    try:
        cursor = conn.cursor()
        cursor.execute(sql4)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
def qry_data(uid):
    sql5 = 'select * from User where uid={0}'.format(uid)
    try:
        cursor = conn.cursor()
        cursor.execute(sql5)
        values = cursor.fetchall()
        print(values)
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def main():
    #add_data()
    #delete_data(3)
    #update_data('sunshine', '123456', 3)
    qry_data(4)

if __name__ == '__main__':
    main()