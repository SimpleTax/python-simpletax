# -*- coding: utf-8 -*-
# vim:tabstop=4:expandtab:sw=4:softtabstop=4

from api import SimpleTax

client_id = ''
client_secret = ''
redirect_uri = 'https://localhost/'

simpletax = SimpleTax(client_id,redirect_uri=redirect_uri)
authorization_url,state = simpletax.authorization_url(SimpleTax.OAUTH_AUTHZ_URL)

print 'Please authorize me in the browser: ',authorization_url
redirect_url = raw_input('Copy the redirect URL here: ')

token = simpletax.fetch_token(SimpleTax.OAUTH_TOKEN_URL,client_secret=client_secret,authorization_response=redirect_url)
print 'Ready to roll...'

simpletax.add_income(2500,description='Demo')
simpletax.add_expense(200,description='Demo 2')

