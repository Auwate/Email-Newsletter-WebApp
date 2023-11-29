# Email-Newsletter-WebApp

This project utilizes predominantly Python and HTML, creating a simple fullstack project to allow a user to connect to a newsletter.

## APIs

### Microsoft Graph API

The Microsoft Graph API allows this program to connect to your Outlook email and send emails on your behalf. This is why the program opens a Microsoft login page, as you need to authenticate your account.

### Mediastack API

The Mediastack API allows the program to send curated news articles by sending it a language and category requests. This API requires an access key, which you can acquire [here](https://mediastack.com/)

## Python

The Python portion utilizes Flask's render_template module and flask module for creating a responsive web app and sending HTML documents from the server.
