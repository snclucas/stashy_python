import os

import requests


class Stashy:
    """
    A session stores configuration state and allows you to create service
    clients and resources.
    :type api_key: string
    :param api_key: Stashy.io API key
    """

    def __init__(self, api_key=None):
        if api_key is None:
            api_key = os.environ.get('STASHY_AP_KEY')
            if api_key is None:
                raise Exception("STASHY_API_KEY env variable not set")
        self.headers = {'Authorization': ' Bearer ' + api_key}

    def get(self, table, filter_by=None, sort_by=None):
        query_params = "?"
        if filter_by is not None:
            query_params = query_params + 'filter=' + filter_by
        if sort_by is None:
            query_params = '&sort=' + query_params + [('_id', 1)]
        url = 'https://stashy.io/api/d/' + table
        r = requests.get(url, headers=self.headers)
