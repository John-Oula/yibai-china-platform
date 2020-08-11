# -*- coding: utf-8 -*-
'''
Created on 2017-12-20

@author: liuqun
'''
import base64
import json
from base64 import b64decode

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from alipaySDK.alipay.aop.api.constant.CommonConstants import PYTHON_VERSION_3
from alipaySDK.alipay.aop.api.util.StringUtils import *


# import rsa

def get_sign_content(all_params):
    sign_content = ""
    for (k, v) in sorted(all_params.items()):
        value = v
        if not isinstance(value, str):
            value = json.dumps(value, ensure_ascii=False)
        sign_content += ("&" + k + "=" + value)
    sign_content = sign_content[1:]
    return sign_content


def fill_private_key_marker(private_key):
    return add_start_end(private_key, "-----BEGIN RSA PRIVATE KEY-----\n", "\n-----END RSA PRIVATE KEY-----")


def fill_public_key_marker(public_key):
    return add_start_end(public_key, "-----BEGIN PUBLIC KEY-----\n", "\n-----END PUBLIC KEY-----")


def sign_data(private_key_loc, data):
    '''
    param: private_key_loc Path to your private key
    param: package Data to be signed
    return: base64 encoded signature
    '''

    key = private_key_loc
    rsakey = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA256.new()
    # It's being assumed the data is base64 encoded, so it's decoded before updating the digest
    digest.update(data)
    sign = signer.sign(digest)
    return sign

def verify_sign(public_key_loc, signature, data):
    '''
    Verifies with a public key from whom the data came that it was indeed
    signed by their private key
    param: public_key_loc Path to public key
    param: signature String signature to be verified
    return: Boolean. True if the signature is valid; False otherwise.
    '''

    pub_key = public_key_loc
    rsakey = RSA.importKey(pub_key)
    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA256.new()
    # Assumes the data is base64 encoded to begin with
    digest.update(b64decode(data))
    if signer.verify(digest, b64decode(signature)):
        return True

def sign_with_rsa(private_key, sign_content, charset):
    if PYTHON_VERSION_3:
        sign_content = sign_content.encode(charset)
    private_key = fill_private_key_marker(private_key)
#    signature = rsa.sign(sign_content, rsa.PrivateKey.load_pkcs1(private_key, format='PEM'), 'SHA-1')
    sign = sign_data(private_key,sign_content)
#    sign = base64.b64encode(signature)
    if PYTHON_VERSION_3:
        sign = str(sign, encoding=charset)
    return sign


def sign_with_rsa2(private_key, sign_content, charset):
    if PYTHON_VERSION_3:
        sign_content = sign_content.encode(charset)
    private_key = fill_private_key_marker(private_key)
#    signature = rsa.sign(sign_content, rsa.PrivateKey.load_pkcs1(private_key, format='PEM'), 'SHA-256')
    signature = sign_data(private_key, sign_content)
    sign = base64.b64encode(signature)
    if PYTHON_VERSION_3:
        sign = str(sign, encoding=charset)
    return sign


def verify_with_rsa(public_key, message, sign):
    public_key = fill_public_key_marker(public_key)
    sign = base64.b64decode(sign)
 #   return bool(rsa.verify(message, sign, rsa.PublicKey.load_pkcs1_openssl_pem(public_key)))
    return verify_sign(public_key,sign,message)

