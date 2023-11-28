import requests
import Application.API.Outlook as Outlook
import Application.Controller.Storage as Storage
import Application.API.News as News
import os


APP_ID = 'e827a227-2bbd-45fc-85ff-5e3de94e4aff'
SCOPES = ['Mail.Send', 'Mail.ReadWrite']


def sendMail(storageComponent):
    access_token = Outlook.generate_access_token(app_id=APP_ID, scopes=SCOPES)

    for email in Storage.keyList(storageComponent):

        components = createDraft(access_token, email, Storage.get(storageComponent, email)[0], Storage.get(storageComponent, email)[1])
        headers = components[0]
        request_body = components[1]

        endpoint = Outlook.GRAPH_API_ENDPOINT + '/me/sendMail'
        response = requests.post(endpoint, headers=headers, json=request_body)

        if response.status_code == 202:
            print('Email sent.\n')
        else:
            print(response.reason)


def createDraft (access_token, email, name, preferences):

    headers = {
        'Authorization': 'Bearer ' + access_token['access_token']
    }

    request_body = {
        'message': {
            # Recipients
            'toRecipients': [
                {  # To add more, just copy-paste this line
                    'emailAddress': {
                        'address': email
                    }
                }  # to this line, over and over again.
            ],
            # Email subject
            'subject': 'Today\'s Newsletter',
            'importance': 'normal',
            'body': {
                'contentType': 'HTML',
                'content': '<b>Dear ' + name + ', here is today\'s newsletter.<b>\n' + grab_content(preferences)
            }
            # Attachments
        }
    }

    return [headers, request_body]


def grab_content(preferences):

    articles = News.getNews(os.getcwd()+'/api_keys.json', preferences)

    html_filler = '''
      <a href="{8}">
      <b>{1}</b>
      </a>
      <br/>
      <a href="{8}">
      <img src="{0}" alt="Image" title="Image" style="display:block" width="200" height="87">
      </a>
      <br/><br/>
      <a href="{9}">
      <b>{3}</b>
      </a>
      <br/>
      <a href="{9}">
      <img src="{2}" alt="Image" title="Image" style="display:block" width="200" height="87">
      </a>
      <br/><br/>
      <a href="{10}">
      <b>{5}</b>
      </a>
      <br/>
      <a href="{10}">
      <img src="{4}" alt="Image" title="Image" style="display:block" width="200" height="87">
      </a>
      <br/><br/>
      <a href="{11}">
      <b>{7}</b>
      </a>
      <br/>
      <a href="{11}">
      <img src="{6}" alt="Image" title="Image" style="display:block" width="200" height="87">
      </a>
      <br/><br/>
    '''

    html_filler = html_filler.format(articles[0]['image'], articles[0]['title'],
                       articles[1]['image'], articles[1]['title'],
                       articles[2]['image'], articles[2]['title'],
                       articles[3]['image'], articles[3]['title'],
                       articles[0]['url'], articles[1]['url'],
                       articles[2]['url'], articles[3]['url'],)

    with open(os.getcwd()+'/templates/email_template.html', 'r') as file:
        first_half = file.read()

    with open(os.getcwd()+'/templates/email_template_2.html', 'r') as file:
        second_half = file.read()

    return first_half + html_filler + second_half