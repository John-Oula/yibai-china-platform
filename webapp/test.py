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
id='16687243626258567007'
def inquire():
    num = random.randint(0, 999999999)
    stamp = int(time.time())

    uri = "/v1/meetings/%s" % (id)

    headerString = "X-TC-Key=%s&X-TC-Nonce=%s&X-TC-Timestamp=%s" % (SecretId, num, str(stamp))

    req_body = {
        "userid": 'olduser',
        "instanceid": 1,
        "subject": 'modify',
        "type": 0,
        "hosts": [{"userid": 'olduser'}],

        "start_time": str(stamp+3000),
        "end_time": str(stamp+6000),
        "settings": {
            "mute_enable_join": True,
            "allow_unmute_self": False,
            "mute_all": False,
            "host_video": True,
            "participant_video": False,
            "enable_record": False,
            "play_ivr_on_leave": False,
            "play_ivr_on_join": False,
            "live_url": False
        }
    }
    req_body = json.dumps(req_body)

    stringToSign = "%s\n%s\n%s\n%s" % ('PUT', headerString, uri, req_body)
    print(stringToSign)

    your_secretkey = SecretKey.encode('utf-8')
    stringToSign = stringToSign.encode('utf-8')

    signature = hmac.new(your_secretkey, stringToSign, digestmod=hashlib.sha256).hexdigest()
    print(signature)

    signature = base64.b64encode(signature.encode("utf-8"))
    datas = req_body

    headers = {'Content-Type': 'application/json', 'X-TC-Key': SecretId, 'X-TC-Timestamp': str(stamp),
               'X-TC-Nonce': str(num), 'AppId': '200000164', 'X-TC-Signature': signature, 'X-TC-Registered': '0'}
    r = requests.put("https://api.meeting.qq.com/v1/meetings/%s" % (id),data=datas,headers=headers)
    print(r.text)
    return r.json()

inquire()