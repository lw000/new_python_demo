'''
Created on 2018年1月4日

@author: Administrator
'''
import sys
import json
import time
import uuid
import tornado.websocket

from chatroom import ChatRoom
from user import User

sys.path.append('./common')

chatroom = ChatRoom()

class ChatSocketHandler(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self, *args, **kwargs):
        self.user = User()
        self.user.name = self.get_argument('name', '')
        self.user.upsd = self.get_argument('upsd', '')
        self.user.rid = self.get_argument('rid', '')
        self.user.uid = self.get_argument('uid', '')
        self.user.extra = self.get_argument('extra', '')

        if chatroom.register(self):
            msg = dict(cmd=0, uuid=uuid.uuid4().hex, name=self.user.name, upsd=self.user.upsd,
                       rid=self.user.rid, uid=self.user.uid, tm=time.time(),  msg='娆㈣繋鍔犲叆鑱婂ぉ瀹�')
            s = json.dumps(msg, ensure_ascii=False)
            self.write_message(s)
        else:
            self.close(10001, 'pragmas error')

    def on_pong(self, data):
        print('on_pong %s' % data)

    def on_ping(self, data):
        print('on_ping %s' % data)

    def on_close(self):
        #         users.unregister(self)

        chatroom.unregister(self)

        print(self)

    def on_message(self, message):

        data = json.loads(message)
        if data is None:
            return
        
        print(message)
                
        cmd = data['cmd']
        name = data['name']
        rid = data['rid']
        uid = data['uid']
        msg = data['msg']
        tm = data['tm']
        uuid = data['uuid']

        msg = dict(cmd=0, uuid=uuid, name=name,
                   rid=rid, uid=uid, msg=msg, tm=tm)
        s = json.dumps(msg, ensure_ascii=False)

        if cmd == 1:  # 鍏ㄧ珯骞挎挱
            chatroom.broadcastMessage(s)
        elif cmd == 2:  # 鎴块棿娑堟伅
            chatroom.sendMessageToRoom(s, rid)
        elif cmd == 3:  # 鍗曡亰娑堟伅
            chatroom.sendMessageToUid(s, rid, uid)
        else:
            self.write_message('{\'code\':0}')
