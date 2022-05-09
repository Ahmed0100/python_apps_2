from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests

result = requests.get("https://www.flipkart.com/computers/laptops/a~buybackguaranteeonlaptops/pr?sid=6bo,b5g&otracker=categorytree")

content=result.content

names=[]
ratings=[]
prices=[]
soup = BeautifulSoup(content,"lxml")

for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
	name=a.find('div',attrs={'class':'_4rR01T'})
	rating=a.find('div',attrs={'class':'gUuXy-'})
	price=a.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
	print(price.text)
	names.append(name.text)
	ratings.append(rating.text)
	prices.append(price.text)

df = pd.DataFrame({'Product Name':names,'Price':prices,'Rating':ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')
