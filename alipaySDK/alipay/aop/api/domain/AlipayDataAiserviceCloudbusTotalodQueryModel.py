#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataAiserviceCloudbusTotalodQueryModel(object):

    def __init__(self):
        self._app_version = None
        self._city_code = None
        self._end_date = None
        self._origin_geo_hashs = None
        self._partner_id = None
        self._start_date = None
        self._type = None

    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def origin_geo_hashs(self):
        return self._origin_geo_hashs

    @origin_geo_hashs.setter
    def origin_geo_hashs(self, value):
        if isinstance(value, list):
            self._origin_geo_hashs = list()
            for i in value:
                self._origin_geo_hashs.append(i)
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.origin_geo_hashs:
            if isinstance(self.origin_geo_hashs, list):
                for i in range(0, len(self.origin_geo_hashs)):
                    element = self.origin_geo_hashs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.origin_geo_hashs[i] = element.to_alipay_dict()
            if hasattr(self.origin_geo_hashs, 'to_alipay_dict'):
                params['origin_geo_hashs'] = self.origin_geo_hashs.to_alipay_dict()
            else:
                params['origin_geo_hashs'] = self.origin_geo_hashs
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAiserviceCloudbusTotalodQueryModel()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'origin_geo_hashs' in d:
            o.origin_geo_hashs = d['origin_geo_hashs']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'type' in d:
            o.type = d['type']
        return o


