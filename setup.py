import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="telegram-vitorpauloski",
    version="0.0.1",
    author="Vitor Leonardo Pauloski",
    author_email="vitorleonardo.pauloski@gmail.com",
    description="Um pacote para facilitar o envio de texto e documentos pelo Telegram",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vitorpauloski/telegram",
    packages=setuptools.find_packages(),
    licence='MIT',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Communications :: Chat",
    ],
    python_requires='>=3.6',
    install_requires=['requests'],
)
