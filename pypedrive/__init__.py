#-*- coding: utf-8 -*-
import requests

PIPEDRIVE_API_URL = "https://api.pipedrive.com/v1/"


class PipedriveError(Exception):
    def __init__(self, response):
        self.response = response

    def __str__(self):
        return self.response.get('error', 'No error provided')


class IncorrectLoginError(PipedriveError):
    pass


class Pypedrive(object):
    def _request(self, endpoint, data, method="GET"):
        url = "{}{}/".format(PIPEDRIVE_API_URL, endpoint)
        params = {'api_token': self.api_token}

        try:
            the_request = self._request_method[method]
        except KeyError:
            raise PipedriveError('Unknown verb')

        if data.get('id') is not None:
            ids = ','.join(map(data.get['id'])) if type(data.get('id')) is list else int(data.get('id'))
            url = '{}{}/'.format(url, ids)

        response = the_request(url, params=params, data=data)

        return response.json()

    def __init__(self, token):
        self.api_token = token
        self._request_method = {
            'POST': requests.post,
            'GET': requests.get,
            'PUT': requests.put,
            'DELETE': requests.delete,
        }

    def __getattr__(self, name):
        def wrapper(data):
            if 'method' in data:
                method = data['method']
                del data['method']
            else:
                method = "GET"
            response = self._request(name, data, method)
            if 'error' in response:
                raise PipedriveError(response)
            return response
        return wrapper
