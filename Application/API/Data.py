import os
import requests
import base64
import Application.API.Outlook as Outlook
import Application.Controller.Storage as Storage


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
                'content': '<b>Dear ' + name + ',<b>\n' + preferences
            }
            # Attachments
        }
    }

    return [headers, request_body]