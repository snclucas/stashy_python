import os
import json

import requests
from urllib.parse import urlencode


class Stashy:
    """
    A session stores configuration state and allows you to create service
    clients and resources.
    :type api_key: string
    :param api_key: Stashy.io API key
    """

    def __init__(self, api_key=None):
        self.headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + api_key}

    def get(self, table, filter_by=None, sort_by=None, order_by=None):
        query_params = ""
        if filter_by is not None:
            query_params = '?' + urlencode(filter_by)
        if sort_by is not None:
            query_params = query_params + '&sort=' + sort_by
        if order_by is not None:
            if order_by.lower() == 'asc' or order_by == 1 or order_by.lower() == 'desc' or order_by == -1:
                query_params = query_params + '&order=' + order_by

        url = 'https://stashy.io/api/d/' + table + '/docs' + query_params
        r = requests.get(url, headers=self.headers)
        json_data = r.json()
        if r.status_code == 200:
            return {
                "url": url,
                "count": len(json_data),
                "data": json_data
            }
        else:
            return json_data

    def save(self, table, data=None, explode=None):
        query_params = ""
        if explode is not None:
            query_params = '?' + urlencode({"ss:explode": explode})
        url = 'https://stashy.io/api/d/' + table + '/docs' + query_params
        r = requests.post(url, headers=self.headers, data=json.dumps(data))
        json_data = r.json()
        if r.status_code == 200:
            return {
                "url": url,
                "count": len(json_data),
                "data": json_data
            }
        else:
            return json_data
