import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, file_path: str, file):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params_to_get_url = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params_to_get_url)
        url_to_upload = response.json()
        result = requests.put(url_to_upload['href'], data=open(file, 'rb'))
        pprint(result)


if __name__ == '__main__':
    path_to_file = 'Загрузки/OMG.txt'
    file = 'OMG.txt'
    token = ''
    uploader = YaUploader(token)
    uploader.upload(path_to_file, file)
