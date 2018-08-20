'''
Created on 2018年6月13日

@author: Administrator
'''

import time
import pymysql
   
def quert_quotation(db, sql):
#     cur = db.cursor()
    cur = db.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        t = time.clock()
        cur.execute(sql)
        results = cur.fetchall()
        t1 = time.clock()
        print('execute t: %f' % (t1 - t))
        
        #遍历结果
#         for row in results:
#             name              = row[0]
#             sale_name         = row[1]
#             quotation_number  = row[2]
#             create_time       = row[3]
#             print(name, sale_name, quotation_number, create_time)
            
        for row in results:
            name              = row['name']
            sale_name         = row['sale_name']
            quotation_number  = row['quotation_number']
            create_time       = row['create_time']
            print(name, sale_name, quotation_number, create_time)
            
    except Exception as e:
        raise e
    finally:
        db.close()
        
if __name__ == '__main__':
    t = time.clock()
    db = pymysql.connect(host="localhost", user="lw", passwd="qazxsw123", db="app_project", port=3306, charset='utf8')
    t1 = time.clock()
    print('connect t: %f' % (t1 - t))
    
    quert_quotation(db, "select * from quotation")
    
    
        