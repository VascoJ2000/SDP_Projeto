import requests


class DataLayerClient:
    def __init__(self):
        try:
            response = self.connect('127.0.0.1', 7000)
        except Exception as e:
            print('Error: ' + str(e))
        else:
            self.server_url = 'http:' + response['server_ip'] + ':' + response['server_port']

    def get_request(self, route, search_id):
        url = self.server_url + f"{route}/{search_id}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Error: ' + str(response.json()['error']))

    def post_request(self, route, data):
        url = self.server_url + route
        response = requests.post(url, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Error: ' + str(response.json()['error']))

    def update_request(self, route, data):
        url = self.server_url + route
        response = requests.put(url, json=data)

        if response.status_code == 200:
            return response.status_code
        else:
            raise Exception('Error: ' + str(response.json()['error']))

    def delete_request(self, route, search_id):
        url = self.server_url + f"{route}/{search_id}"
        response = requests.delete(url)

        if response.status_code == 200:
            return response.status_code
        else:
            raise Exception('Error: ' + str(response.json()['error']))

    def connect(self, host, port):
        response = requests.post('http://' + host + ':' + str(port))

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.json()['error'])

