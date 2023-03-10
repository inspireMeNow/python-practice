import pymysql
# import dbutils

def create_pool():
    from dbutils.pooled_db import PooledDB
    poll=PooledDB(
        creator=pymysql,
        maxconnections=5,
        mincached=2,
        maxcached=4,
        host='localhost',
        user='root',
        password='796184@.cnCN',
        database='csms',
        charset='utf8mb4'
    )
    return poll
