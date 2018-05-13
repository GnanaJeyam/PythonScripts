from bs4 import BeautifulSoup
import requests
import urllib

class GetScore():
	# Creating a requests to cricbuzz
	page = requests.get("http://www.cricbuzz.com/")

	page_data = BeautifulSoup(page.content,'html.parser')

	team_score = page_data.find_all('div',class_="cb-ovr-flo")
	score = '	'
	for name in team_score[0:5]:
		if( name != None):
			score = score + name.text
	
