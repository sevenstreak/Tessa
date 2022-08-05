import os	
import requests

#load_dotenv()

rk = os.environ['RAWG_KEY']

key = "?key=" + rk
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
