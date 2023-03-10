from encrypt import Encrypt
import dbutils


class User:
    id = ''
    password = ''
    email = ''
    idtype = 0

    def __init__(self):
        pass

    def setArg(self, id, password, email, idtype):
        self.id = id
        self.password = password
        self.email = email
        self.idtype = idtype

    def findUser(self, id):
        try:
            connection_poll = dbutils.create_pool()
            conn = connection_poll.connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id,email,idtype FROM id_table WHERE id=?", (id,))
            row = cursor.fetchone()
            if row:
                user = User()
                user.setArg(row[0], '', row[1], row[2])
                conn.close()
                return user
            else:
                conn.close()
                return
        except Exception as e:
            print(str(e))

    def Print(self):
        print(self.id+"\n"+self.password+"\n"+self.email+"\n"+f'{self.idtype}')

    def setPassword(self, password):
        try:
            connection_poll = dbutils.create_pool()
            conn = connection_poll.connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE id_table SET passwd=? WHERE id=?",
                           (Encrypt.md5(password)[0:19], self.id))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)

    def login(self):
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        username = input("请输入用户名：")
        user = User()
        user = user.findUser(username)
        if (user == None):
            print("用户不存在")
        else:
            password = input("请输入密码：")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT passwd FROM id_table WHERE id=?", (user.id,))
            row = cursor.fetchone()
            if row[0] == Encrypt.md5(password)[0:19]:
                print("登录成功")
            else:
                print("登录失败")
        conn.close()

    def register(self):
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        username = input("用户名：")
        email = input("邮箱：")
        password = input("密码：")
        user = User()
        user = user.findUser(username)
        if (user == None):
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO id_table(id,passwd,email,idtype) VALUES(?,?,?,?)", (username, Encrypt.md5(password)[0:19], email, 1))
            conn.commit()
            print("注册成功")
        else:
            print("用户名已存在，请重新注册！")
        conn.close()
