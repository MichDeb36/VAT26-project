from lxml import html
import requests

class InfoVat26():

    def getInfoVat26(self):
        url = 'https://www.pit.pl/samochod-a-vat/siedem-dni-na-zlozenie-vat-26-aby-odliczyc-caly-podatek-1001569'
        xpath = '/html/body/main/div[2]/div[2]/article/div/p[11]/text()'
        page = requests.get(url)
        tree = html.fromstring(page.text)
        text = tree.xpath(xpath)
        text = str(text)
        text = text[2:-2]
        return text