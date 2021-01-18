import requests

class Bot:
    def __init__(self, token):
        self.token = token

    def getUpdates(self):
        url = 'https://api.telegram.org/' + self.token + '/getUpdates'
        response = requests.request('GET', url)
        return response.text
    
    def sendMessage(self, chat_id, text):
        url = 'https://api.telegram.org/' + self.token + '/sendMessage'
        params = (('chat_id', chat_id),('text', text))
        response = requests.request('GET', url, params = params)
        return response.text

    def sendDocument(self, chat_id, file_path):
        url = 'https://api.telegram.org/' + self.token + '/sendDocument?chat_id=' + chat_id
        files = {'document': open(file_path, 'rb')}
        response = requests.request('POST', url, files = files)
        return response.text
