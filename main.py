import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse
import argparse


def shorten_url(main_url, headers):
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    payload = {"long_url": main_url, "domain": "bit.ly", }
    response = requests.post(api_url, headers=headers, json=payload)
    response.raise_for_status()
    short_link = response.json()['link']
    return f'Битлинк: {short_link}'


def count_clicks(bitlink, headers):
    params = {
        'unit': 'week',
        'units': '-1',
        'size': '50',
    }
    click_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    clicks_response = requests.get(click_url, headers=headers, params=params)
    clicks_response.raise_for_status()
    total = clicks_response.json()['total_clicks']
    return f'Переходов по ссылке: {total}'


def handle_link(main_url, bitlink, headers):
    check_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    check_response = requests.get(check_url, headers=headers)
    try:
        if check_response.ok:
            return count_clicks(bitlink, headers)
        else:
            return shorten_url(main_url, headers)
    except requests.exceptions.RequestException as e:
        return e


def create_parser():
    parser = argparse.ArgumentParser(
        description='Преобразовывает длинные ссылки в короткие, а по ссылке bit.ly считает количество переходов'
    )
    parser.add_argument('link', help='ссылка', type=str)
    return parser


if __name__ == "__main__":
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    bitly_auth_token = os.environ.get("BITLY_AUTH_TOKEN")
    headers = {'Authorization': f'Bearer {bitly_auth_token}', 'Content-Type': 'application/json', }
    parser = create_parser()
    args = parser.parse_args()
    main_url = args.link
    main_netloc = urlparse(main_url)[1]
    main_path = urlparse(main_url)[2]
    bitlink = f'{main_netloc}{main_path}'
    print(handle_link(main_url, bitlink, headers))