# -*- coding: utf-8 -*-
import time
import random
import hmac
import hashlib
import base64
import json
from hashlib import sha256
import requests

SecretId = "JIRMZ6O3Qm5KDwCHsgYnlxatGeXq7dfFcjEk"
SecretKey = "wZn5NeGCqxg4r8XaDum2EMzRhIvWHtcU"

num = random.randint(0,999999999)
stamp = int(time.time())

uri = "/v1/meetings/12269259670683052373/cancel"

headerString = "X-TC-Key=%s&X-TC-Nonce=%s&X-TC-Timestamp=%s" % (SecretId,num,str(stamp))

req_body = {
    "userid": 'user',
    "instanceid": 1,
    "reason_code": 1,
}
req_body = json.dumps(req_body)
stringToSign = "%s\n%s\n%s\n%s" % ('POST', headerString, uri, req_body)
print(stringToSign)

your_secretkey = SecretKey.encode('utf-8')
stringToSign = stringToSign.encode('utf-8')

signature = hmac.new(your_secretkey, stringToSign, digestmod=hashlib.sha256).hexdigest()
print(signature)

signature = base64.b64encode(signature.encode("utf-8"))

headers = {'Content-Type': 'application/json', 'X-TC-Key': SecretId, 'X-TC-Timestamp': str(stamp),
           'X-TC-Nonce': str(num), 'AppId': '200000164', 'X-TC-Signature': signature, 'X-TC-Registered': '0'}
datas = req_body
r = requests.post("https://api.meeting.qq.com/v1/meetings/12269259670683052373/cancel", data=datas, headers=headers)
print(r.ok)
print(r.json())

