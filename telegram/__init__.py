import requests
import json

class Response:
    def __init__(self, success, response):
        self.success = success
        self.response = response

    def __repr__(self):
        if self.success:
            return '<Response [Success]>'
        else:
            return '<Response [Failure]>'

class Bot:
    def __init__(self, token):
        self.token = token
        self.id = token.split(':')[0].replace('bot', '')

    def __repr__(self):
        return f'<Bot [{self.id}]>'

    def getUpdates(self):
        url = 'https://api.telegram.org/' + self.token + '/getUpdates'
        request = requests.get(url)
        if request.status_code == 200:
            response = json.loads(request.text)['result']
            return Response(True, response)
        else:
            response = f'Error {request.status_code}.'
        return Response(False, response)

    def sendMessage(self, chat_id, text):
        url = 'https://api.telegram.org/' + self.token + '/sendMessage'
        params = {'chat_id': chat_id, 'text': text}
        request = requests.get(url, params = params)
        if request.status_code == 200:
            response = json.loads(request.text)['result']
            return Response(True, response)
        else:
            response = f'Error {request.status_code}.'
            return Response(False, response)

    def sendDocument(self, chat_id, file_path):
        url = 'https://api.telegram.org/' + self.token + '/sendDocument'
        params = {'chat_id': chat_id}
        files = {'document': open(file_path, 'rb')}
        request = requests.post(url, params = params, files = files)
        if request.status_code == 200:
            response = json.loads(request.text)['result']
            return Response(True, response)
        else:
            response = f'Error {request.status_code}.'
            return Response(False, response)
