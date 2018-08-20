'''
Created on 2018年1月9日

@author: Administrator
'''

import os

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Hash import SHA512
from Crypto.Hash import MD5
from Crypto import Random
from Crypto.PublicKey import RSA

def rsa_test():    
    # 伪随机数生成器
    random_generator = Random.new().read
    # rsa算法生成实例
    rsa = RSA.generate(1024, random_generator)
    
    # master的秘钥对的生成
    private_pem = rsa.exportKey()
    
    with open('master-private.pem', 'w') as f:
        f.write(private_pem)
    
    public_pem = rsa.publickey().exportKey()
    with open('master-public.pem', 'w') as f:
        f.write(public_pem)
    
    # ghost的秘钥对的生成
    private_pem = rsa.exportKey()
    with open('master-private.pem', 'w') as f:
        f.write(private_pem)
    
    public_pem = rsa.publickey().exportKey()
    with open('master-public.pem', 'w') as f:
        f.write(public_pem)


if __name__ == '__main__':
    u = os.urandom(24)
    print(u)
    
    md5 = MD5.new()
    md5.update('klgwl.com77889'.encode('utf-8'))
#     print('md5: ', md5.digest())
    print('md5: ', md5.hexdigest())
    
    hash = SHA256.new()
    hash.update('klgwl.com77889'.encode('utf-8'))
#     print('sha256: ', hash.digest())
    print('sha256: ', hash.hexdigest())
    
    hash = SHA512.new() 
    hash.update('klgwl.com77889'.encode('utf-8'))
#     print('sha512: ', hash.digest())
    print('sha512: ', hash.hexdigest())
    
    rsa_test()
    
#     obj = AES.new('111111111', AES.MODE_CBC, 22)
#     message = 'this is message'
#     ciphertext = obj.encrypt(message)
#     print(ciphertext)
#     
#     obj2 = AES.new('111111111', AES.MODE_CBC, 22)
#     ciphertext = obj2.decrypt(ciphertext)
#     print(ciphertext)
