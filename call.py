import requests
from dotenv import load_dotenv
import os	


load_dotenv()

key = "?key=" + os.getenv('RAWG_KEY')
api = "https://api.rawg.io/api/games/"

async def desc(game:str):
	url = api + game + key                 
	response = requests.request("GET", url)
	decoded = response.json()
	#print(decoded)
	return decoded['description_raw']


async def metacritic(game:str):
	url = api + game + key                 
	response = requests.request("GET", url)
	decoded = response.json()
	#print(decoded)
	return decoded['metacritic']


async def g(game:str):
	url = api + game + key                 
	response = requests.request("GET", url)
	decoded = response.json()
	#print(decoded)
	return decoded


async def bg(game:str):
	url = api + game + key                 
	response = requests.request("GET", url)
	decoded = response.json()
	#print(decoded)
	return decoded['background_image']
