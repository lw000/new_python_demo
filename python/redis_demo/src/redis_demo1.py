'''
Created on 2018年7月11日

@author: liwei
'''

import redis
import demjson as json

if __name__ == '__main__':
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
    r = redis.Redis(connection_pool=pool)
    
    s = json.encode({'a':'aa', 'b':'ccc'})
    r.set('liwei', s)
    g = r.get('liwei').decode()
    s1 = json.decode(g)
    print(s1)
    
    r.mset(liwei2='11111', liwei3='33333', liwei4='44444')
    s2 = r.mget('liwei2','liwei3','liwei4')
    print(s2)
    print(r.get('liwei2').decode())
    print(r.get('liwei3').decode())
    print(r.get('liwei4').decode())
    