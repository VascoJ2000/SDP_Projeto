import requests
import time


class Client:
    def __init__(self):
        self.server_url = None

    def get_request(self, route, search_id1, search_id2, token=None):
        url = self.server_url + f"{route}/{search_id1}&{search_id2}"
        if token:
            if search_id1 is None and search_id2 is None:
                url = self.server_url + f"{route}/"
            response = requests.get(url, headers={'Authorization': f'Bearer {token}'})
        else:
            response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Error: ' + str(response.json()['error']))

    def post_request(self, route, data, token=None):
        url = self.server_url + route
        if token:
            response = requests.post(url, headers={'Authorization': f'Bearer {token}'}, json=data)
        else:
            response = requests.post(url, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Error: ' + str(response.json()['error']))

    def update_request(self, route, data, token=None):
        url = self.server_url + route
        if token:
            response = requests.put(url, headers={'Authorization': f'Bearer {token}'}, json=data)
        else:
            response = requests.put(url, json=data)

        if response.status_code == 200:
            return response.status_code
        else:
            raise Exception('Error: ' + str(response.json()['error']))

    def delete_request(self, route, search_id, token=None):
        url = self.server_url + f"{route}/{search_id}"
        if token:
            response = requests.delete(url, headers={'Authorization': f'Bearer {token}'})
        else:
            response = requests.delete(url)

        if response.status_code == 200:
            return response.status_code
        else:
            raise Exception('Error: ' + str(response.json()['error']))

    def connect(self, host, port, max_attempts=12):
        for i in range(max_attempts):
            response = requests.get(f'http://{host}:{port}')
            data = response.json()
            if response.status_code == 200:
                self.server_url = 'http:' + data['server_ip'] + ':' + data['server_port']
                print(f'Cliente connected to load balancer no port {port}')
            elif response.status_code == 425:
                time.sleep(2)
            else:
                raise Exception('Error: ' + str(response.json()['error']))
        raise Exception('Cliente cannot find a available server')
