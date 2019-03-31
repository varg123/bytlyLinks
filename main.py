import requests
import os
from dotenv import load_dotenv
import argparse


def create_bitlink(token, long_url):
    headers = {
        'Authorization': 'Bearer ' + token
    }
    json = {
        "long_url": long_url
    }
    resp = requests.post(
        "https://api-ssl.bitly.com/v4/bitlinks",
        headers=headers,
        json=json
    )
    resp.raise_for_status()
    return resp.json()['link']


def get_bitlink_clicks(token, url):
    headers = {
        'Authorization': 'Bearer ' + token
    }
    params = {
        "units": -1,
        "unit": "day",
    }
    resp = requests.get(
        "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary".format(url),
        headers=headers,
        params=params
    )
    resp.raise_for_status()
    return resp.json()['total_clicks']


def is_bitlink(token, url):
    headers = {
        'Authorization': 'Bearer ' + token
    }
    resp = requests.get(
        "https://api-ssl.bitly.com/v4/bitlinks/{}".format(url),
        headers=headers
    )
    return resp.ok


def main():
    load_dotenv()
    token = os.getenv("TOKEN")
    parser = argparse.ArgumentParser(
        description="Создать ссылку bit.ly или узнать кол-во кликов уже созданной"
    )
    parser.add_argument(
        '-l',
        '--link',
        required=True,
        help='Полная ссылка на внешний ресурс или bit.ly/ХХХХХХХ'
    )
    url = parser.parse_args().link
    if is_bitlink(token, url):
        print("Сумарное кол-во кликов по ссылке: {}".format(get_bitlink_clicks(token, url)))
    else:
        print("Созданная сокращенная ссылка: {}".format(create_bitlink(token, url)))

if __name__ == "__main__":
    main()
