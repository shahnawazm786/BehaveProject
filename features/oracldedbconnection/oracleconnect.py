import oracledb
conn=oracledb.connect(user="scott",password="tiger",dsn="localhost/orcl")
print("successful connection--")
cursor=conn.cursor()
cursor.execute(
    """
    select * from emp
    """
)
for row in cursor:
    print(row)
