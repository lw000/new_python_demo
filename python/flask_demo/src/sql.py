'''
Created on 2018年1月27日

@author: Administrator
'''

import sqlite3

def sqlite3_connect_db(db):
    '''Connects to the specific database.'''
    rv = sqlite3.connect(db)
    rv.row_factory = sqlite3.Row
    return rv

if __name__ == '__main__':
    
    con = sqlite3_connect_db('test.db')
    cur = con.cursor()
    cursor = cur.execute('''CREATE TABLE IF NOT EXISTS COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
    
    print('Table created successfully')
    
    cursor = cur.execute('DELETE FROM COMPANY') 
    cursor = cur.execute("INSERT INTO COMPANY (ID, NAME,AGE, ADDRESS, SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");  
    cursor = cur.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
          VALUES (2, 'Allen', 25, 'Texas', 15000.00 )"); 
    cursor = cur.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
          VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
    cursor = cur.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
          VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");       
    con.commit()
#     cursor = cur.execute('SELECT * FROM COMPANY LIMIT 1')
    cursor = cur.execute('SELECT * FROM COMPANY ORDER BY ID DESC')
#     cursor = cur.execute('SELECT * FROM COMPANY ORDER BY ID ASC')
    
    for c in cursor:
        print('ID: %d, NAME: %s, AGE: %d, ADDRESS: %s, SALARY: %f' % (c[0], c[1], c[2], c[3], c[4]))
    
    con.close()
    