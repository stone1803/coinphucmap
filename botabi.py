# tim ra nhung may koh hoat dong bao ve fbchat
# 134 or True
import time
import requests
import pyfiglet
from prettytable import PrettyTable
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colored import fg, bg, attr
from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
from fbchat import Client
from fbchat.models import *

# client = Client("ledanghongphuc@gmail.com", "")
#
# print("Own id: {}".format(client.uid))
#
# client.send(Message(text=131321321), thread_id=100028593181497, thread_type=ThreadType.USER)
#
# client.logout()

dashboard ='https://api.ethermine.org/miner/0x78c56e18906f21c8009fcba662e8f2c0e1ed196c/dashboard'
monitoring ='https://api.ethermine.org/miner/0x78c56e18906f21c8009fcba662e8f2c0e1ed196c/workers/monitor'
currentStats='https://api.ethermine.org/miner/0x78c56e18906f21c8009fcba662e8f2c0e1ed196c/currentStats'
monitor= 'https://api.ethermine.org/miner/0x78c56e18906f21c8009fcba662e8f2c0e1ed196c/workers/monitor'
def showinfo():
    request = requests.get(currentStats)
    data = request.json()
    activeWorkers = data['data']['activeWorkers']
    reportedHashrate = data['data']['reportedHashrate']
    print('So may hien tai dang khai thac',activeWorkers, 'May')
    print('Tong so MHZ dang co duoc',reportedHashrate, 'MHZ')
def showwoker():
    dashboarda = requests.get(dashboard).json()
    data = dashboarda['data']['workers']
    bang = PrettyTable()
    bang.field_names = ['TEN MAY', 'GIO', 'KHAITHAC', 'TB-KHAITHAC']
    for x in data:
        tenmay = Fore.BLUE + x['worker']
        KHAITHAC = x['reportedHashrate']
        tbKhaiThac = x['currentHashrate']
        GIO = x['time']
        bang.add_row([tenmay , GIO, KHAITHAC, tbKhaiThac])
        print(bang)
        bang.clear_rows()


def send():
    request = requests.get(currentStats)
    data = request.json()
    activeWorkers = data['data']['activeWorkers']
    reportedHashrate = data['data']['reportedHashrate']
    gmailpassword = ''
    # mailto = input("NHAP DIA CHI EMAIL MUON GUI \n ")
    tieude = 'BAO CAO SO TRAU DANG HOAT DONG'
    noidung = 'SỐ MÁY ĐANG HOẠT ĐỘNG  ' + str(activeWorkers) +' MÁY ' + 'KHAI THÁC TỔNG ' + str(reportedHashrate)+ ' MHZ'

    # msg1 = input("What is your message? \n ")
    msg = MIMEMultipart()
    msg['From'] = 'jangmi110985@gmail.com'
    msg['To'] = 'ledanghongphuc@gmail.com'
    msg['Subject'] = tieude
    msg.attach(MIMEText(noidung, 'plain'))
    text = msg.as_string()

    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.starttls()
    mailServer.login('jangmi110985@gmail.com', gmailpassword)
    mailServer.sendmail('jangmi110985@gmail.com', 'ledanghongphuc@gmail.com', text)
    print(" \n ĐÃ SENT EMAIL CHO SẾP !")
    mailServer.quit()
def smsfb():
    request = requests.get(currentStats)
    data = request.json()
    activeWorkers = data['data']['activeWorkers']
    reportedHashrate = data['data']['reportedHashrate']/1000000000
    client = Client("ledanghongphuc@gmail.com", "")
    print("Own id: {}".format(client.uid))
    client.send(Message(text=" 👉 Số máy đang hoạt động {} 🆗 và tổng số khai thác {} GHZ ".format(activeWorkers, reportedHashrate)), thread_id=client.uid, thread_type=ThreadType.USER)
    client.logout()

# while True:
#     send()
#     time.sleep(120)
#     send()
#     print(pyfiglet.figlet_format('VNC-COIN'))
#     print('-----------------------')
#     showinfo()
#     print('-----------------------')
#     # xem = input('XEM CHI TIET SO TRAU DANG MINER y/n > : ')
#     # if xem =='y':
#     #     showwoker()
#     # else:
#     #
#     #     quit()
while True:
    smsfb()
    time.sleep(600)

