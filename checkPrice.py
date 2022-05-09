import requests
from bs4 import BeautifulSoup
import smtplib

def send_email():
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('ahmedmustafa0100@gmail.com','VoidBringer')
	subject = 'Price Fall Down'
	body = "Check Amazon"
	msg = f"Subject: {subject}\n\n{body}"
	server.sendmail('ahmedmustafa0100@gmail.com','ahmedmustafa0100@gmail.com', msg)


url= "https://www.amazon.in/dp/B08RSWTH32/ref=gwdb_bmc_0_M02s?pf_rd_s=merchandised-search-6&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=0WFX7P4JJ3GDYSXNJM09&pf_rd_p=282996c8-e914-46f6-8cf4-838309dae510"

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html5lib')
title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_dealprice").get_text()
# print(price[2:9])
# conv_price = float(price[2:9])
# if(conv_price < 1900):
send_email()
print(price)