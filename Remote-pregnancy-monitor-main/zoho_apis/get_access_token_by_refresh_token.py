def get_access_token():
    import requests
    from get_refresh_token import get_refresh_token, request_parameters
    import os.path


    Accounts_URL = 'https://accounts.zoho.in'
    if (os.path.exists("temp_file.txt") == False):
      refresh_token = get_refresh_token()
    else:
      f = open("temp_file.txt", "r")
      refresh_token = f.readline()
      f.close()
    client_id = request_parameters['client_id']
    client_secret = request_parameters['client_secret']
    url = '{}/oauth/v2/token?refresh_token={}&client_id={}&client_secret={}&grant_type=refresh_token'.format(Accounts_URL,refresh_token,client_id,client_secret)
    # print(url)
    res = requests.post(url)
    json_data = res.json()
    access_token = json_data["access_token"]

    return access_token


    
