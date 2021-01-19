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
```

To learn how to create a Bot and generate an authorization token, read the *BotFather* session from [Telegram Bots documentation](https://core.telegram.org/bots#6-botfather).

## Available methods

- **getUpdates()**\
Use this method to receive incoming updates.

- **sendMessage(`chat_id`, `text`)**\
Use this method to send text messages.

- **sendDocument(`chat_id`, `file_path`)**\
Use this method to send general files. Bots can currently send files of any type of up to 50 MB in size.
