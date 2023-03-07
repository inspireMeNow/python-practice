import sys
import mariadb
from user import User




if __name__ == "__main__":
    try:
        conn = mariadb.connect(
            user="root",
            password="796184@.cnCN",
            host="127.0.0.1",
            port=3306,
            database="csms"
        )

        user=User()
        print("登录系统：")
        user.login(conn)
        print("修改用户密码：")
        password=input("请重新输入你的密码：")
        user.setPassword(conn,password)
        
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    sys.exit()