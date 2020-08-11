#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotSnCreateModel(object):

    def __init__(self):
        self._content = None
        self._create_count = None
        self._hardware_product_id = None
        self._item_id = None
        self._supplier_id = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def create_count(self):
        return self._create_count

    @create_count.setter
    def create_count(self, value):
        self._create_count = value
    @property
    def hardware_product_id(self):
        return self._hardware_product_id

    @hardware_product_id.setter
    def hardware_product_id(self, value):
        self._hardware_product_id = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.create_count:
            if hasattr(self.create_count, 'to_alipay_dict'):
                params['create_count'] = self.create_count.to_alipay_dict()
            else:
                params['create_count'] = self.create_count
        if self.hardware_product_id:
            if hasattr(self.hardware_product_id, 'to_alipay_dict'):
                params['hardware_product_id'] = self.hardware_product_id.to_alipay_dict()
            else:
                params['hardware_product_id'] = self.hardware_product_id
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotSnCreateModel()
        if 'content' in d:
            o.content = d['content']
        if 'create_count' in d:
            o.create_count = d['create_count']
        if 'hardware_product_id' in d:
            o.hardware_product_id = d['hardware_product_id']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        return o


