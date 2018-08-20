#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2018年1月3日

@author: Administrator
'''

from flask import Flask
from flask import request
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for

# from flask import sessions

app = Flask(__name__)

@app.route('/')
def home():
#     return '<h1>Home</h1>'
    return render_template('./home.html', name='Hello Lwstar')

@app.route('/redirect')
def redirect():
#     return '<h1>Home</h1>'
    return redirect(url_for('add'))


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


@app.route('/add', methods=['GET', 'POST'])
def add():
#     v = sessions[""]
    
    cook_username = request.cookies.get('username')
    print('cook_username: ', cook_username)
    
    a = None
    b = None
    
    if request.method == 'GET':
        a = request.args.get('a')
        b = request.args.get('b')
        
    #     if not isinstance(a, int):
    #         raise ValueError('a must be an integer!')
    #     if not isinstance(b, int):
    #         raise ValueError('b must be an integer!')
        
    elif request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
    else:
        pass
    
    return str(int(a) + int(b))
    
@app.route('/sub', methods=['GET', 'POST'])
def sub():
    a = None
    b = None
    
    if request.method == 'GET':
        a = request.args.get('a')
        b = request.args.get('b')
                
    elif request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        
    else:
        pass
    
    return str(int(a) - int(b))

@app.route('/dht', methods=['GET'])
def dht():
    c = request.args.get('count')
    t = request.args.get('temp')
    h = request.args.get('hum')
    
    print('采集次数：%s, 温度数据：%s, 湿度：%s' % (c, t, h))
    
    return 'YES'

@app.route('/distance', methods=['GET'])
def distance():
    d = request.args.get('distance')
    
    print('距离：%s cm' % (d))
    
    return 'YES'

if __name__ == '__main__':
    app.logger.debug('debug')
#     app.run(host='10.1.0.54', port=5000)
    app.run(host='0.0.0.0', port=5000)
