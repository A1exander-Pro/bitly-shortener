# Обрезка ссылок с помощью сервиса bit.ly 

Проект создан для сокращения длинных ссылок в короткие через сервис [bit.ly](https://app.bitly.com/), а также подсчет 
кликов по переходам уже существующих коротких ссылок.

---

## Установка: 
- Для изоляции проекта рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html)
- Python3 уже должен быть установлен. Использоуйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:   
```python
pip install -r requirements.txt
```
- Далее нужно зарегистрироваться на [bit.ly](https://app.bitly.com/) и сгенерировать  `"Generic Access Token"` .
- Также вам нужно создать ```.env``` файл и прописать ваш `"Generic Access Token"` следующим образом:    
```python
BYTLY_AUTH_TOKEN=************************
```
- Для создания короткой ссылки нужно в консоле(терминале) вставить ссылку, которую нужно сократить (пример ссылки: https://www.google.com)  
в директории, где находится основной файл ```main.py```, например.:   
```python
your_directory your_username$ python3 main.py https://www.google.com
```  
- Для подсчета переходов по ссылке необходимо сделать тоже самое, только вместо длинной ссылки вставить уже существующую короткую ссылку [bit.ly](https://app.bitly.com/), например:   
```python    
 your_directory your_username$ python3 main.py  https://bit.ly/3aRxoV
 ```
---

## Project Goals
Код написан в образовательных целях на онлайн курсе для веб разработчиков [dvmn.org](https://dvmn.org/).

