import http.client, urllib.parse
import Application.API.FileManager as FileManager
import json

MEDIASTACK_ENDPOINT = 'api.mediastack.com'

options = {
    '1': 'general',
    '2': 'business',
    '3': 'entertainment',
    '4': 'health',
    '5': 'science',
    '6': 'sports',
    '7': 'technology'
}


def getNews(filelocation, preferences):

    newsType = options.get(preferences)

    api_key = FileManager.read_from_file(file_name=filelocation)['mediastack']
    conn = http.client.HTTPConnection(MEDIASTACK_ENDPOINT)

    params = urllib.parse.urlencode({
        'access_key': api_key,
        'categories': newsType,
        'sort': 'published_desc',
        'languages': 'en',
        'limit': 4
    })
    conn.request('GET', '/v1/news?{}'.format(params))

    res = conn.getresponse()
    data = json.load(res)

    return data['data']


def parse_to_html(data, html_location):
    # First, copy the email_template.html to a new file called email.html
    FileManager.save_to_file(FileManager.read_from_file(''))