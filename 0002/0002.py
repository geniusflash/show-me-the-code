import mysql.connector

def activationcode2sql():
    # 打开数据库链接
    con=mysql.connector.connect(host='localhost',port='3306',user='root',password='123456',database='test')
    cursor=con.cursor() #使用cursor方法创建一个cursor对象
    # cursor.execute("create table act_code(id int auto_increment primary key, code varchar(50) not null)")
    f=open("../0001/youhuiquan.txt")
    for line in f.readlines():
        print(line.strip())
        cursor.execute("insert into act_code(code) values ('%s')" % line.strip())    #通过dict方式插入（利用%（字段）s作为占位符）
        
    con.commit()
    f.close()
    cursor.close()

if __name__=='__main__':
    activationcode2sql()
