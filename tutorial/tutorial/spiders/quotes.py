import json
import time

import pandas as pd
import scrapy
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64


def recode(t):
    # 将UTF-8字符串转为字节串
    key = "EB444973714E4A40876CE66BE45D5930".encode('utf-8')
    iv = "B5A8904209931867".encode('utf-8')

    # 解码base64
    t = base64.b64decode(t)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext_padded = cipher.decrypt(t)
    plaintext = unpad(plaintext_padded, AES.block_size).decode('utf-8')

    return plaintext


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ['ggzyfw.fujian.gov.cn']
    start_urls = ["https://ggzyfw.fujian.gov.cn/business/list/"]

    def start_requests(self):
        url = 'https://ggzyfw.fujian.gov.cn/FwPortalApi/Trade/TradeInfo'
        df = pd.read_csv('D:\songxuanyi\PycharmProjects\scrapy_demo\\tutorial\\tutorial\spiders\param.csv')
        for index, row in df.iterrows():
            pageNo = row['pageNo']
            pageSize = row['pageSize']
            total = row['total']
            ts = row['ts']
            portal_sign = row['portal_sign']

            payload = {"pageNo": pageNo, "pageSize": pageSize, "total": total, "AREACODE": "", "M_PROJECT_TYPE": "",
                       "KIND": "GCJS",
                       "GGTYPE": "1", "PROTYPE": "", "timeType": "6", "BeginTime": "2023-01-28 00:00:00",
                       "EndTime": "2023-07-28 23:59:59", "createTime": [], "ts": ts}
            headers = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json;charset=UTF-8',
                'Origin': 'https://ggzyfw.fujian.gov.cn',
                'Referer': 'https://ggzyfw.fujian.gov.cn/business/list/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'portal-sign': portal_sign,
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
            }
            yield scrapy.Request(url, headers=headers, method='POST', body=json.dumps(payload), callback=self.parse)

    def parse(self, response):
        res_data = response.json()
        success = res_data['Success']

        if success:
            data = res_data['Data']
            recode_data = recode(data)
            json_data = json.loads(recode_data)
            table = json_data['Table']

            for item in table:
                yield {
                    "KIND": item["KIND"],
                    "TITLE": item["TITLE"],
                    "GGTYPE": item["GGTYPE"],
                    "NAME": item["NAME"],
                    "M_ID": item["M_ID"],
                    "PLATFORM_CODE": item["PLATFORM_CODE"],
                    "PLATFORM_NAME": item["PLATFORM_NAME"],
                    "TM1": item["TM1"],
                    "AREACODE": item["AREACODE"],
                    "AREANAME": item["AREANAME"],
                    "PROTYPE_TEXT": item["PROTYPE_TEXT"],
                    "PROTYPE": item["PROTYPE"],
                    "M_DATA_SOURCE": item["M_DATA_SOURCE"],
                    "M_TM": item["M_TM"],
                    "M_PROJECT_TYPE": item["M_PROJECT_TYPE"],
                    "TM": item["TM"],
                    "IS_NEW": item["IS_NEW"]
                }
