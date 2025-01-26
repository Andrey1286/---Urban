import requests
import pprint


class Request1(requests.Request):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def resp_get(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            value = response.json()
            pprint.pprint(value)
        else:
            print(f'Ошибка: {response.status_code}')
        return response.status_code


request_ = Request1('https://api.spacexdata.com/v3')
x = request_.resp_get()
print(x)
