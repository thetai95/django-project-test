from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
import csv

URL_LOGIN = "https://af-a.jp/login"
URL_GET_WEBSITE = "https://af-a.jp/media?mime=csv.all"

username = "ohtsubo@tubox.co.jp"
password = "sE9cMJtPax"


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        session = requests.session()

        # find token
        r = session.get(URL_LOGIN)
        soup = BeautifulSoup(r.text, "lxml")
        token = soup.find("input", {'name': '_token'})
        if token:
            token = token.get('value')
        # else: thi sao

        # check login
        payload = {
            "_token": token,
            "email": username,
            "password": password
        }
        # print(payload)

        p = session.post(URL_LOGIN, data=payload)
        soup = BeautifulSoup(p.text, "lxml")
        logout = soup.find("form", {
            'action': '/logout',
            'method': 'post'
        })

        # print(bool(logout))

        # return true/false

        # get data
        file_csv = session.get(URL_GET_WEBSITE)

        # print(file_csv.text)

        decoded_content = file_csv.content.decode('unicode_escape')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)

        for row in my_list[1:]:
            obj = {
                "id": row[0],
                "name": row[1],
                "type": row[2],
                "url": row[3],
                "status": row[4],
            }
            print(obj)
            print("=====" * 30)

        # print("=====" * 40)
        # print(my_list)
        # print("=====" * 40)
