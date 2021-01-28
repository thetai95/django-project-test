from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup

URL_LOGIN = "https://af-a.jp/login"

username = "username"
password = "password"


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        # 1 - validate: coi nhu tat ca input dung

        # 2 - check login
        session = requests.session()

        # find token
        r = session.get(URL_LOGIN)
        soup = BeautifulSoup(r.text, "lxml")
        token = soup.find("input", {'name': '_token'})
        if not token:
            return "Get token failure."

        payload = {
            "_token": token.get('value'),
            "email": username,
            "password": password
        }
        print(payload)

        p = session.post(URL_LOGIN, data=payload)
        soup = BeautifulSoup(p.text, "lxml")
        logout = soup.find("form", {
            'action': '/logout',
            'method': 'post'
        })

        if not bool(logout):
            return "Login failure."

        # login true => get data
        # 3 - get data



        return "ok"


        # 4 - return
