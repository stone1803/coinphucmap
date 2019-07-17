import requests
import json
import pyfiglet
from prettytable import PrettyTable
while True:
    # noi dung lay url api coin
    gloURL = 'https://api.coinmarketcap.com/v1/global/'
    tickerUrl = 'https://api.coinmarketcap.com/v1/ticker/'
    request = requests.get(gloURL)
    data = request.json()
    tonggiaodich = data["total_market_cap_usd"]
    print(pyfiglet.figlet_format('CoinMarketCap'))
    print('Kiem tra gia coinmarketCap' )
    print('Tong giao dich tren thi truong hien tai la ' + str(tonggiaodich))
    print('Nhap all xe lay tat ca coin gia usd va ban co the nhap tu coin vd bitcoin')
    print('-------------------------------------------')
    nhap = input('Lua chon cua ban')
    if nhap == 'all':
        request = requests.get(tickerUrl)
        data = request.json()
        for x in data:
            bang = PrettyTable()
            bang.field_names =['TENCOIN','GIA USD']
            symbol = x["symbol"]
            price = x["price_usd"]
            bang.add_row([symbol,price])
            print(bang)
    else:
        tickerUrl +='/'+nhap+'/'
        request =requests.get(tickerUrl)
        data = request.json()
        symbol = data[0]["symbol"]
        price = data[0]["price_usd"]
    nhap2 = input('Muon kiem tra lai koh (y/n) :')
    if nhap2 =='y':
        continue
    if nhap2 =='n':
        break