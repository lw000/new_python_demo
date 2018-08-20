'''
Created on 2018年6月8日

@author: Administrator
'''

import copy

class People(object):
    def __init__(self):
        self.__name = ''
        self.__age = 0
        self.__sex = 0
        self.__address = ''
        self.__birthday = ''
        self.__IDcardNo = ''
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age
        
    @property
    def sex(self):
        return self.__sex
    
    @sex.setter
    def sex(self, sex):
        self.__sex = sex
        
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, address):
        self.__address = address
        
    @property
    def birthday(self):
        return self.__birthday
    
    @birthday.setter
    def birthday(self, birthday):
        self.__birthday = birthday
        
    @property
    def IDcardNo(self):
        return self.__IDcardNo
    
    @IDcardNo.setter
    def IDcardNo(self, IDcardNo):
        self.__IDcardNo = IDcardNo
              
    def __str__(self, *args, **kwargs):
        return str({
            'name': self.__name, 
            'age': self.__age, 
            'sex': self.__sex, 
            'address': self.__address, 
            'birthday': self.__birthday,
            'IDcardNo': self.__IDcardNo })
        
if __name__ == '__main__':
    people = People()
    people.name = '李伟'
    people.age = 30
    people.sex = 1
    people.address = '广东省深圳市宝安区西乡芬达科技园对面雅居园11单元1202'
    people.birthday = '19840604'
    people.IDcardNo = '61015198406047512'
    print('people:', people)
    
    people1 = people
    people1.name = '何珊珊'
    people1.age = 18
    people1.sex = 0
    people1.address = '广东省深圳市宝安区西乡芬达科技园对面雅居园11单元1202'
    people1.birthday = '19860526'
    people1.IDcardNo = '410332198605262124'
    print('people:', people)
    print('people1:', people1)
    
    people2 = copy.deepcopy(people)
    people2.name = '李诗彤'
    people2.age = 5
    people2.sex = 0
    people2.address = '广东省深圳市宝安区西乡芬达科技园对面雅居园11单元1202'
    print('people2:', people2)
    
    
    