from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="1468",database="python_db")
def insert(id,name,age,city):
    res = con.cursor()
    sql="insert into users(id,name,age,city) values(%s,%s,%s,%s)"
    user=(id,name,age,city)
    res.execute(sql,user)
    con.commit()
    print("data insert success")
def update(id,name,age,city):
    res = con.cursor()
    sql = "update users set name=%s,age=%s,city=%s where id=%s"
    user = (id, name, age, city)
    res.execute(sql, user)
    con.commit()
    print("data update success")
def select():
    res=con.cursor()
    sql="select id,name,age,city from users"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["id","name","age","city"]))
def delete(id):
    res = con.cursor()
    sql = "delete from users where id=%s"
    user = (id,)
    res.execute(sql, user)
    con.commit()
    print("data delete successfully")
while True:
    print("1.Insert data")
    print("2.Update data")
    print("3.select data")
    print("4.delete data")
    print("5.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        id=input("enter your id:")
        name=input("enter your name:")
        age=input("enter your age:")
        city=input("enter your city:")
        insert(id,name,age,city)
    elif choice==2:
        id = input("enter your id:")
        name = input("enter your name:")
        age = input("enter your age:")
        city = input("enter your city:")
        update(name, age, city,id)
    elif choice==3:
        select()
    elif choice==4:
        id=input("enter your id:")
        delete(id)
    elif choice==5:
        quit()
    else:
        print("invalid choice")






