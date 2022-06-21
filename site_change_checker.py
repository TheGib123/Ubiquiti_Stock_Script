import requests
from bs4 import BeautifulSoup
import csv


Devices = []
class Device:
    def __init__(self, name, link, in_stock):
        self.name = name
        self.link = link
        self.in_stock = in_stock

def update_stock(device):
    page = requests.get(device.link)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="titleInStockBadge")
    print()
    print(results)
    print()
    if (results != None):
        print('in stock')
        device.in_stock = True
    else:
        print('not in stock')
        device.in_stock = False

# pick a device that is in stock and one that is out of stock
udm = Device('udm pro', 'https://store.ui.com/collections/unifi-network-unifi-os-consoles/products/udm-pro', 'test')
ap = Device('ap-6-lite', 'https://store.ui.com/collections/unifi-network-wireless/products/unifi-ap-6-lite', 'test')

Devices.append(udm)
Devices.append(ap)

for device in Devices:
    print('##########################')
    print(device.name)
    print(device.link)
    print(device.in_stock)

    update_stock(device)

    print(device.name)
    print(device.link)
    print(device.in_stock)
    print('##########################')