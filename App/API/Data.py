import FileManager
import requests


def get_api_key(filename):
    FileManager.read_from_file(filename)


def get_api_data(apikey):
    url = "http://api.airvisual.com/v2/nearest_city?key=" + apikey
    data = requests.get(url).json()
    FileManager.save_to_file(data, 'air_quality.json')