#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Detail import Detail


class AttachmentExplain(object):

    def __init__(self):
        self._allow_more_uploads = None
        self._description = None
        self._details = None
        self._title = None

    @property
    def allow_more_uploads(self):
        return self._allow_more_uploads

    @allow_more_uploads.setter
    def allow_more_uploads(self, value):
        self._allow_more_uploads = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        if isinstance(value, list):
            self._details = list()
            for i in value:
                if isinstance(i, Detail):
                    self._details.append(i)
                else:
                    self._details.append(Detail.from_alipay_dict(i))
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.allow_more_uploads:
            if hasattr(self.allow_more_uploads, 'to_alipay_dict'):
                params['allow_more_uploads'] = self.allow_more_uploads.to_alipay_dict()
            else:
                params['allow_more_uploads'] = self.allow_more_uploads
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.details:
            if isinstance(self.details, list):
                for i in range(0, len(self.details)):
                    element = self.details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.details[i] = element.to_alipay_dict()
            if hasattr(self.details, 'to_alipay_dict'):
                params['details'] = self.details.to_alipay_dict()
            else:
                params['details'] = self.details
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AttachmentExplain()
        if 'allow_more_uploads' in d:
            o.allow_more_uploads = d['allow_more_uploads']
        if 'description' in d:
            o.description = d['description']
        if 'details' in d:
            o.details = d['details']
        if 'title' in d:
            o.title = d['title']
        return o


