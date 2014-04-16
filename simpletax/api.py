# -*- coding: utf-8 -*-
# vim:tabstop=4:expandtab:sw=4:softtabstop=4

import json
from requests_oauthlib import OAuth2Session
from datetime import date

BASE_API = 'https://secure.gosimpletax.com/api/v2/uk'
INCOME_URL = '%s/incomes/' % BASE_API
EXPENSES_URL = '%s/expenses/' % BASE_API

class ServerError(Exception):
    pass

class NoAccessError(Exception):
    pass

class SimpleTax(OAuth2Session):
    OAUTH_AUTHZ_URL = 'https://secure.gosimpletax.com/o/authorize/'
    OAUTH_TOKEN_URL = 'https://secure.gosimpletax.com/o/token/'

    def __parse_error(self,res):
        if res.status_code >= 500:
            raise ServerError()
        elif res.status_code >= 400:
            raise NoAccessError()

    def __get_today(self):
        return date.today().strftime('%d/%m/%Y')

    def add_income(self,amount,description='',date=None,category=None):
        if date is None:
            date = self.__get_today()

        data = json.dumps({'fields':{'value':amount,'date':date,'reference':description}})
        res = self.post(INCOME_URL,data)
        self.__parse_error(res)
        return res.json()

    def add_expense(self,amount,description='',date=None,category=None):
        if date is None:
            date = self.__get_today()

        data = json.dumps({'fields':{'value':amount,'date':date,'reference':description}})
        res = self.post(EXPENSES_URL,data)
        self.__parse_error(res)
        return res.json()

