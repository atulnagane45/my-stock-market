from fyers_api import accessToken
import yaml
import requests, json

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

app_id =  cfg['app_id']

app_secret = cfg['app_secret']

app_session = accessToken.SessionModel(app_id, app_secret)

response = app_session.auth()

authorization_code = response['data']['authorization_code']

app_session.set_token(authorization_code)

print(app_session.generate_token())

access_token = (app_session.generate_token()).split('?')[1]
print()
print(access_token)
#https://trade.fyers.in/?access_token=gAAAAABg7_w4YT-3EEFuIcL8SO9yXhnpJCqlhc4QC4nxzE0TWzRVh6FQ7Hu6KDwfgvkSHNRJgZ_mlZP89HTMEV41vq2n4l7zqCpKbRXUBqbJCbwLQRO2FJc=&user_id=XA08240&poa_flag=N