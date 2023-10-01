#Getting the problems from DMOJ site as PDF

"""This script takes the problem id and gets the PDF files from 
the dmoj site. If you are using the file to input the problem id
then create file with IDs one below the other..."""

import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

base ="https://dmoj.ca/problem/"

choice = input("How do you want to enter the problems? file / CLI")
choice = choice.lower()
if choice == 'file':
    problem = []
    file_name = input('Provide the file name, ensure it is same folder as the script: ')
    with open(file_name) as f:
        reader = f.readlines()
        for x in reader:
            problem.append(x)    
else:
    how_many = int(sys.stdin.readline())
    problems = []

    for _ in range(how_many):
        problems.append(sys.stdin.readline().strip('\n'))

links = [] #get the links of the problem pages
for probl in problems:
    links.append(urljoin(base, probl))

pdf_links = [] #Collecting the links of the problem pdf
for link in links:    
    data = requests.get(link)
    text = BeautifulSoup(data.text,'html.parser')
    pdf = [z.get('href') for z in text.find_all('a') if z.has_attr('class')][10]
    pdf_links.append(urljoin(base,pdf))
#getting each file

for i in range(how_many):
    response = requests.get(pdf_links[i])
    name = f"{problems[i]}.pdf" 
    file = open(name,'wb')
    file.write(response.content)
    file.close()