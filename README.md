# TelePython

TelePython is a Python package for sending and receiving messages and documents by a Telegram Bot, based on [Telegram Bot API](https://core.telegram.org/bots/api)

## Installation

TelePython is available on [PyPI](https://pypi.org/project/TelePython/):
```
pip install TelePython
```
TelePython officially supports Python 3.8 or above.

## Basic usage

```python
>>> import telegram
>>> bot = telegram.Bot('YOUR_BOT_TOKEN')
>>> bot.sendMessage('CHAT_ID', 'Your message here!')
<Response [Success]>
```

To learn how to create a Bot and generate an authorization token, read the *BotFather* session from [Telegram Bots documentation](https://core.telegram.org/bots#6-botfather).

## Available methods

- **getUpdates()**\
Use this method to receive incoming updates.

- **sendMessage(`chat_id`, `text`)**\
Use this method to send text messages.

- **sendDocument(`chat_id`, `file_path`)**\
Use this method to send general files. Bots can currently send files of any type of up to 50 MB in size.

## Response object

The Response objects have two parameters:

- **success**\
Indicates whether the request was successful (True or False).

- **response**\
returns the result of the request to the Telegram Bot API

Example:

```python
>>>  import telegram
>>> bot = telegram.Bot('YOUR_BOT_TOKEN')
>>> response = bot.getUpdates()
>>> response.succes
True
>>> response.response
[{'update_id': 675682626, 'message': {'message_id': 56, 'from': {'id': 8644990718, 'is_bot': False, 'first_name': 'Vitor', 'last_name': 'Pauloski', 'username': 'vitorpauloski', 'language_code': 'pt-br'}, 'chat': {'id': 8644990718, 'first_name': 'Vitor', 'last_name': 'Pauloski', 'username': 'vitorpauloski', 'type': 'private'}, 'date': 1611617371, 'text': 'Test Message.'}}]
```
