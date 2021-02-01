from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
import csv

from urllib.parse import urlencode
import xlrd

URL_LOGIN = "https://af-a.jp/login"
URL_GET_WEBSITE = "https://af-a.jp/media?mime=csv.all"
URL_REPORT = "https://af-a.jp/conversions?{}"

username = "username"
password = "password"


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        self.get_data_order()
        # self.test_command()

    def test_command(self):
        import requests

        example_url = 'http://www.excel-easy.com/examples/excel-files/fibonacci-sequence.xlsx'

        r = requests.get(example_url)  # make an HTTP request

        workbook = xlrd.open_workbook(file_contents=r.content)  # open workbook

        sheet = workbook.sheet_by_index(0)  # get first sheet

        data = []
        for row in range(0, sheet.nrows):
            l = []
            for column in range(0, sheet.ncols):
                val = sheet.cell(row, column).value
                # l.append(val)

                data.append(val)

        print(data)

    def get_data_order(self):
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

        # 3 - get data website
        csv_file = session.get(URL_GET_WEBSITE)
        decoded_content = csv_file.content.decode('unicode_escape')
        content = csv.reader(decoded_content.splitlines(), delimiter=',')
        websites = list(content)

        result = []
        for row in websites[1:]:
            result.append({
                "id": row[0],
                "name": row[1],
                "url": row[3],
            })

        # 4 - get data order
        params = {
            'approval_status': 'all',
            'period': '2020/12/20-2020/12/20',
            'search_date': 'cv_date',
            'search_column': 'query_string',
            'ad_category': 'all',
            'display_columns': 'all',
            'period_from[date]': '2020-12-20+00:00:00.000000',
            'period_from[timezone_type]': '3',
            'period_from[timezone]': 'Asia/Tokyo',
            'period_to[date]': '2020-12-20+23:59:59.999999',
            'period_to[timezone_type]': '3',
            'period_to[timezone]': 'Asia/Tokyo',
            'mime': 'xlsx.all'
        }

        url = URL_REPORT.format(urlencode(params))
        print(url)
        print()

        r = session.get(url)
        workbook = xlrd.open_workbook(file_contents=r.content)  # open workbook
        # pip install xlrd==1.2.0

        sheet = workbook.sheet_by_index(0)  # get first sheet

        data = []
        for row in range(1, sheet.nrows):
            l = []
            for column in range(0, sheet.ncols):
                val = sheet.cell(row, column).value
                l.append(val)

            print("=====" * 30)
            print(l)
            print("=====" * 30)

            data.append(l)

        print(len(data))
        # 4 - return
        return "ok -- 123"
