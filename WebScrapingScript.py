'''
Name: Rebeka Henry

Date: 11/2/2018

Program name: Webscraping Prompt of the Day

Description: This is a simple script that generates
a writing prompt using web scraping. It utilizes Beautiful
Soup and the url library. It then saves the data to be
accessed as a csv that updates this information. Every time
the script is run on python, it generates a new prompt for the 
user
'''

from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

from datetime import datetime

import csv

class GeneratePrompt():
	def permissions_parse_extract_data(self):

		#request from the site permission to use the url, create a parser
		quote_page = Request ('https://www.plot-generator.org.uk/story-ideas/')
		page = urlopen(quote_page).read()
		soup = BeautifulSoup(page, 'html.parser')

		#extract the data from the page
		name_box =  soup.find('div', attrs= {'class' : 'random_story'} )	
		
		#clean the data from the site
		name = name_box.text.strip()

		#use date time and csv to save and access data
		hold_date_time = str(datetime.now())
		with open ('Prompt.csv', 'a') as csv_file:
			writer = csv.writer(csv_file)
			writer.writerow([hold_date_time, name])	
		

call_class = GeneratePrompt()

call_class.permissions_parse_extract_data()