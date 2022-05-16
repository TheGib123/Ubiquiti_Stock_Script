import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import smtplib
import time

fromEmail = 'yourEmail@gmail.com'
password = 'applicaionPassword'
toEmail = 'destinationEmail'
check_minutes = 10                  # Pause minutes for the script



Devices = []
class Device:
    def __init__(self, name, link, in_stock):
        self.name = name
        self.link = link
        self.in_stock = in_stock

# reads devices.csv and places each row in Devices list
def read_file():
    with open('devices.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for row in reader:
            device_name = row[0]
            device_link = row[1]
            device_in_stock = False
            d = Device(device_name, device_link, device_in_stock)
            Devices.append(d)

# sends email to email specified above
def send_email(device):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromEmail, password)
    message = f"""\
    Subject: in stock : {device.name} 

    device:
    {device.name}

    link:
    {device.link}

    This message is sent from Python."""
    s.sendmail(fromEmail, toEmail, message)
    s.quit()

# sends a test email to make sure it is working correctly
def send_test_email():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromEmail, password)
    message = """\
    Subject: ubiquiti stock tool

    Test email for ubiquiti stock tool.
    If you are seeing this the email part of the script
    is working correctly.

    This message is sent from Python."""
    s.sendmail(fromEmail, toEmail, message)
    s.quit()

# logs information when ever the device is in stock
def log_info(device):
    time = datetime.now()
    time = time.strftime("%m/%d/%Y %I:%M:%S %p")
    f = open("email_log.txt", "a")
    f.write(str(device.name) + " in stock\n")
    f.write(str(device.link) + '\n')
    f.write(str(time) + '\n')
    f.write("\n")
    f.close()

# outputs the date and time
def console_out_begin():
    time = datetime.now()
    time = time.strftime("%m/%d/%Y %I:%M:%S %p")
    f = open("console_out.txt", "a")
    f.write(str(time) + '\n\n')
    f.close()

# outputs the device information 
def console_out(device):
    f = open("console_out.txt", "a")
    f.write(str(device.name) + ' in stock : ' + str(device.in_stock) + '\n')
    f.write('\n')
    f.close()

# outputs the break line for read ability
def console_out_end():
    f = open("console_out.txt", "a")
    f.write('#####################################\n')
    f.write('\n')
    f.close()

# checks if the stock has changed for a device and updates its value
def update_stock(device):
    page = requests.get(device.link)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="titleInStockBadge")
    if ('In-Stock' in str(results)):
        device.in_stock = True
    else:
        device.in_stock = False

# main loop
def main_loop():
    while True:
        console_out_begin()

        for i in Devices:
            current_stock = i.in_stock
            update_stock(i)
            new_stock = i.in_stock
            if (current_stock == False and new_stock == True):
                send_email(i)
                log_info(i)
            console_out(i)

        console_out_end()
        time.sleep(check_minutes * 60)

print('Ubiquiti script now running')
read_file()
send_test_email()
main_loop()



