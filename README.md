# NSFW detection telegram bot
## how it works
1. someone sends a photo
2. the bot analyzes it with a model
3. if it flagged as NSFW, it gets deleted and resent with spoiler
## requirements
- [python 3.8.10](https://www.python.org/downloads/release/python-3810/)
## installation
0. create a venv using `python -m venv ./.venv/`
1. install nsfw-detector (fixed ver.)
    - clone the detector repo: `git clone https://github.com/GantMan/nsfw_model`
    - edit nsfw_model/requirements.txt:
        - replace `tensorflow>=2.2.0;sys_platform != 'darwin'` with `tensorflow==2.2.0;sys_platform != 'darwin'`
    - install the package: `python -m pip install git+file:///absolute/path/to/folder`
2. install aiogram and python-dotenv: `python -m pip install aiogram python-dotenv`
3. get your telegram bot token at [@BotFather](https://t.me/BotFather)
4. create `.env` file with contents: `TOKEN=[your token]`
## usage
you can run it with `python main.py`
## contact
contact me by mail: [q16@q16.dev](mailto:q16@q16.dev)  
or by telegram: [@blurflower](https://t.me/blurflower)