import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title = []
company_name = []
location_name = []
job_skill = []
links = []
r =[]
result=requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

src = result.content

soup = BeautifulSoup(src,"lxml")
job_titles = soup.find_all("h2", {"class":"css-m604qf"})
company_names = soup.find_all("a", {"class":"css-17s97q8"})
location_names = soup.find_all("span",{"class":"css-5wys0k"})
job_skills=soup.find_all("div", {"class":"css-y4udm8"})

for i in range(len(job_titles)):
	job_title.append(job_titles[i].text)
	links.append(job_titles[i].find("a").attrs['href'])
	company_name.append(company_names[i].text)
	location_name.append(location_names[i].text)
	job_skill.append(job_skills[i].text)

for link in links:
	result=requests.get(link)
	src = result.content
	soup = BeautifulSoup(src,"lxml")
	resps = soup.find("div",attrs={'class':'css-1uobp1k'})
	resps_text=""
	for li in enumerate(resps):
		print(type(li))
		resps_text += li.get_text + "| "
	r.append(resps_text)

file_list = [job_title, company_name, location_name, job_skill, links, r]
exported = zip_longest(*file_list)

with open(r"C:\Users\amustafa\Desktop\py\WebScrapping/res.csv","w") as file:
	wr=csv.writer(file)
	wr.writerow(["Job Title", "Company Name", "Location", "Job Skills","Link", "Responsibilities"])
	wr.writerows(exported)


