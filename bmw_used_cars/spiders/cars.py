from pathlib import Path
import json

import requests
import scrapy
from scrapy.http import Response


class CarsSpider(scrapy.Spider):
    name = "cars"
    allowed_domains = ["usedcars.bmw.co.uk"]
    start_urls = ["https://usedcars.bmw.co.uk/vehicle/api/list/?payment_type=cash&size=23&source=home"]
    method = "get"

    custom_headers = headers = {
          'accept': 'application/json, text/plain, */*',
          'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
          'cache-control': 'no-cache',
          'pragma': 'no-cache',
          'priority': 'u=1, i',
          'referer': 'https://usedcars.bmw.co.uk/result/?payment_type=cash&size=23&source=home',
          'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
          'sec-ch-ua-mobile': '?1',
          'sec-ch-ua-platform': '"Android"',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Mobile Safari/537.36',
          'x-csrftoken': 'Vo6mBqVBjSyonJkQ5OZxFjSuRMBUsya7',
          'Cookie': 'csrftoken=Vo6mBqVBjSyonJkQ5OZxFjSuRMBUsya7; django_language=en-gb; C5tM5s_origin=%7B%22sentAnomalies%22%3A%5B%5D%2C%22from%22%3A%22usedcars_bmw_co_uk%22%2C%22sid%22%3A%2219043063305591490565464684817296264291%22%7D; cc_consentCookie=%7B%22bmw_unitedkingdom_family%22%3A%7B%22cmm%22%3A%7B%22advertising%22%3A0%7D%2C%22cdc%22%3A1%2C%22tp%22%3A1661330829156%2C%22lmt%22%3A1772866333185%7D%7D'
    }

    def start_requests(self):
        """ Send a request to the website """
        yield scrapy.Request(
            url=self.start_urls[0],
            headers=self.custom_headers,
            method="get",
            callback=self.parse
        )

    def parse(self, response: Response, **kwargs):

        data = json.loads(response.text)
        for i in data["results"]:
            yield {"data": i["derivative"]}
