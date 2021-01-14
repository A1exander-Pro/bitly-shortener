# Bitly url shorterer 

This project is made for short your links into short [bit.ly](https://app.bitly.com/) links, and count clicks from existing [bit.ly](https://app.bitly.com/) link.<br>

---

## How to install: 
- Recommended to use for isolation of your project [virtualenv/venv](https://docs.python.org/3/library/venv.html)
- Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:<br>
```pip install -r requirements.txt```
- Then you need to register at [bit.ly](https://app.bitly.com/) and generate your  `"Generic Access Token"` in your account.
- You need to make our own .env file and put your `"Generic Access Token"` as <br>
```BYTLY_AUTH_TOKEN=************************```
- To short new link you need to write in console(terminal) link you need to short (ex.: https://www.google.com)  
in the directory of your main.py file ex.: <br>
```your_directory your_username$ python3 main.py https://www.google.com``` <br>
- To count link you need to make same procedure but instead of long link you should put [bit.ly](https://app.bitly.com/) link ex.:<br>
 ```your_directory your_username$ python3 main.py  https://bit.ly/3aRxoV```

---

## Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).

Russian language [README](https://github.com/A1exander-Pro/bitly-shorterer/blob/main/README_RU.md)
