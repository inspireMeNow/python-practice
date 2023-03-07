from encrypt import Encrypt


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

    def findUser(self, conn, id):
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id,email,idtype FROM id_table WHERE id=?", (id,))
        row = cursor.fetchone()
        if row:
            user = User()
            user.setArg(row[0], '', row[1], row[2])
            return user
        else:
            return

    def Print(self):
        print(self.id+"\n"+self.password+"\n"+self.email+"\n"+f'{self.idtype}')

    def setPassword(self, conn, password):
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE id_table SET passwd=? WHERE id=?",
                           (Encrypt.md5(password)[0:19], self.id))
            conn.commit()
        except Exception as e:
            print(e)

    def login(self, conn):
        username = input("请输入用户名：")
        user = User()
        user = user.findUser(conn, username)
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
