import setuptools

with open('README.md', 'r', encoding = 'utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'TelePython',
    version = '1.1.0',
    author = 'Vitor Leonardo Pauloski',
    author_email = 'vitorleonardo.pauloski@gmail.com',
    description = 'TelePython is a Python package for sending and receiving messages and documents by a Telegram Bot, based on Telegram Bot API.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/vitorpauloski/TelePython',
    packages = ['telegram'],
    licence = 'MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Communications :: Chat',
    ],
    python_requires = '>=3.8',
    install_requires = ['requests>=2.25.1'],
)
