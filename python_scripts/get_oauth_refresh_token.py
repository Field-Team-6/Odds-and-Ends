#!/usr/bin/env python3
import argparse
import sys

import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect

'''
This example walks through a basic oauth flow using the existing long-lived token type
Populate your app key and app secret in order to run this locally
'''

APP_KEY = ''
APP_SECRET = ''
idebug = False

## OBTAIN KEY AND SECRET FROM COMMAND LINE ARGUMENTS
parser = argparse.ArgumentParser(description='dropbox_connect_test.py --appkey appkey --appsecret appsecret --reftoken refresh_token')
parser.add_argument('--debug', help='turn on detailed output messages', action='store_true')
parser.add_argument('--appkey', nargs='?', help='App Key provided by Dropbox')
parser.add_argument('--appsecret', nargs='?', help='App Secret provided by Dropbox')

## PARSE COMMAND LINE ARGUMENTS AND VERIFY
args = parser.parse_args()

if not args.appkey:
    print('--appkey is mandatory')
    sys.exit(3)
else:
    APP_KEY = args.appkey
if not args.appsecret:
    print('--appsecret is mandatory')
    sys.exit(4)
else:
    APP_SECRET = args.appsecret
if args.debug:
    idebug = True

if idebug:
    print('APPKEY: ' +  APP_KEY, ' APPSECRET: ' + APP_SECRET)

auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET, token_access_type="offline")

authorize_url = auth_flow.start()
print("1. Go to: " + authorize_url)
print("2. Click \"Allow\" (you might have to log in first).")
print("3. Copy the authorization code.")
auth_code = input("Enter the authorization code here: ").strip()

try:
    oauth_result = auth_flow.finish(auth_code)
    print("REFRESH TOKEN: " + oauth_result.refresh_token)
except Exception as e:
    print('Error: %s' % (e,))
    exit(1)
