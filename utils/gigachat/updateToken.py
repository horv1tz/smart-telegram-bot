from requests import post

from config import SBER_TOKEN, SBER_AUTH_DATA

def update_sber_key():
    responce = post(
        url="https://ngw.devices.sberbank.ru:9443/api/v2/oauth",
    )