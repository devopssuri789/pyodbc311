import sys
sys.path.append('/opt/python')
import pyodbc
def lambda_handler(event, context):
    SERVER = 'database-1.cfokeaw40jtz.ap-south-1.rds.amazonaws.com'
    #DATABASE = 'database-1'
    USERNAME = 'admin'
    PASSWORD = 'admin123'
    
    
    conn = pyodbc.connect(
                'DRIVER={ODBC Driver 18 for SQL Server};'
                f'SERVER={SERVER};'
                f'UID={USERNAME};'
                f'PWD={PASSWORD};'
            )
    print("connection.con")
    
    #connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes'
    #conn = pyodbc.connect(connectionString)
    
    cursor = conn.cursor()
    cursor.execute("SELECT NAME FROM SYS.DATABASES;")
    
    records = cursor.fetchall()
    print("Printing DATABASES")
    for r in records:
        print(r[0])

        cursor.execute(f"SELECT TABLE_NAME FROM {r[0]}.information_schema.tables;")
        recordsa = cursor.fetchall()
        print(f"Listing tables for {r[0]}")
        for r in recordsa:
            print(r)