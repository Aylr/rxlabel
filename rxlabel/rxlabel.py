# -*- coding: utf-8 -*-
import requests

BASE_URL = 'https://api.fda.gov/drug/label.json'


def _add_api_key_to_url(api_key):
    return BASE_URL + '?api_key=' + api_key


class RxLabel:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.base_url = _add_api_key_to_url(api_key)

    def search_generic_name(self, search_term):
        params = {'api_key': self.api_key, 'search': 'generic_name:' + search_term}

        r = requests.get(self.base_url, params=params)
        if r.status_code == 200:
            return r.json()
        else:
            return None
