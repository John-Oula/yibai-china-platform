import unittest
import base64
import hashlib
import  hmac
from webapp import SecretKey


class MyTestCase(unittest.TestCase):
    def create_sign(self):
        h = hmac.new(key, msg=toSign.encode('utf-8'), digestmod=hashlib.sha256).digest()
        print(type(h))
        print(h)

        base64.b64encode(bytes(h.hex(), 'utf-8')).decode()


if __name__ == '__main__':
    unittest.main()
