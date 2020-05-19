# -*- coding: utf-8 -*-
import time
import random
import hmac
import hashlib
import base64
import json
from hashlib import sha256
import requests

your_secretid = "JIRMZ6O3Qm5KDwCHsgYnlxatGeXq7dfFcjEk"
your_secretkey = "wZn5NeGCqxg4r8XaDum2EMzRhIvWHtcU"

num = random.randint(0,999999999)
stamp = int(time.time())

uri = "/v1/meetings"

headerString = "X-TC-Key=%s&X-TC-Nonce=%s&X-TC-Timestamp=%s" % (your_secretid,num,str(stamp))

req_body = {
   "userid" : "666",
   "instanceid" : 1,
   "subject" : "tester's meeting",
   "type" : 0,
   "hosts" : [{"userid":"666"}],
   "start_time" : str(stamp + 3000),
   "end_time" : str(stamp + 6000),
   "settings" : {
    "mute_enable_join":True,
    "allow_unmute_self":False,
    "mute_all": False,
    "host_video":True,
    "participant_video": False,
    "enable_record": False,
    "play_ivr_on_leave": False,
    "play_ivr_on_join": False,
    "live_url": False
   }
}
req_body = json.dumps(req_body)
stringToSign = "%s\n%s\n%s\n%s" % ('POST',headerString,uri,req_body)
print (stringToSign)


your_secretkey = your_secretkey.encode('utf-8')
stringToSign = stringToSign.encode('utf-8')


signature = hmac.new(your_secretkey,stringToSign,digestmod=hashlib.sha256).digest()
print("我是签名：\n",signature)

signature =signature.hex()
signature =base64.b64encode(signature.encode("utf-8"))


headers = {'Content-Type': 'application/json','X-TC-Key':your_secretid,'X-TC-Timestamp':str(stamp),'X-TC-Nonce':str(num),'AppId':'200000164','X-TC-Signature':signature,'X-TC-Registered':'0'}
datas = req_body
r = requests.post("https://api.meeting.qq.com/v1/meetings", data=datas, headers=headers)
print('创建会议成功：\n',r.text)
print('创建会议成功：\n',r.json())