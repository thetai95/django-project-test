from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup

URL_LOGIN = "https://partner.link-a.net/login.php"
URL_GET_WEBSITE = "https://partner.link-a.net/linkapages/partner_media_list.php?page_num={}"
URL_EDIT_WEBSITE = "https://partner.link-a.net/linkapages/media_edit_input.php?id={}"

username = "username"
password = "password"


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        session = requests.session()

        # CHECK LOGIN
        payload = {
            "login": username,
            "password": password
        }

        r = session.post(URL_LOGIN, data=payload)

        soup = BeautifulSoup(r.text, "lxml")
        logout = soup.find("a", {'href': 'logout.php'})

        if not logout:
            return "Login failed!"

        # GET LIST SITE_ID
        print(URL_GET_WEBSITE.format(1))

        r = session.get(URL_GET_WEBSITE.format(1))
        soup = BeautifulSoup(r.text, "lxml")
        list_tbody = soup.find_all("tbody")

        print(list_tbody)

        # site_ids = []
        # for tbody in list_tbody:
        #     site_ids.append(tbody.find("td").getText())

        # # GET ALL INFO WEBSITE
        # result = []
        # for site_id in site_ids:
        #     r = session.get(URL_EDIT_WEBSITE.format(site_id))
        #     soup = BeautifulSoup(r.text, "lxml")
        #
        #     site_name = soup.find("input", {'name': 'title'})
        #     site_url = soup.find("input", {'name': 'url'})
        #
        #     result.append({
        #         "id": site_id,
        #         "name": site_name.get("value") if site_name else "",
        #         "url": site_url.get("value") if site_url else "",
        #     })
        #     # break
        #
        # for site in result:
        #     print(f'{site.get("id")} - {site.get("name")} - {site.get("url")}')
        #     print()
        #
        # print("len_result = ", len(result))
