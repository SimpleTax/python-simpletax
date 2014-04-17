# Python wrapper for SimpleTax API

SimpleTax (http://gosimpletax.com) is the free, web-based tax software that helps you easily find the most savings and ensures you file an accurate tax return, no matter how complicated your affairs are.

This Python library allows you to integrate your application with SimpleTax via it's REST API. It relies on OAuth2 for authorising access to a user's account.

# Installation

The fast way to install the library is:
```
pip install -e https://github.com/Leftfield/python-simpletax.git#egg=simpletax
```

# Usage

This library acts an OAuth2 consumer, leveraging the requests-oauthlib library. To request a client ID and secret please contact the SimpleTax team, at hello@gosimpletax.com.

Sample code to make API calls:

```
from api import SimpleTax

# the client_id and secret obtained from the SimpleTax team
client_id = ''
client_secret = ''

# the redirect_uri should be the URI to which users are redirected after authorising access to their account from your app
redirect_uri = 'https://localhost/'

simpletax = SimpleTax(client_id,redirect_uri=redirect_uri)
authorization_url,state = simpletax.authorization_url(SimpleTax.OAUTH_AUTHZ_URL)

print 'Please authorize me in the browser: ',authorization_url
redirect_url = raw_input('Copy the redirect URL here: ')

token = simpletax.fetch_token(SimpleTax.OAUTH_TOKEN_URL,client_secret=client_secret,authorization_response=redirect_url)
print 'Ready to roll...'

simpletax.add_income(2500,description='Customer invoice')
simpletax.add_expense(200,description='Photoshop license')

print 'Check the result on your SimpleTax account'
```

