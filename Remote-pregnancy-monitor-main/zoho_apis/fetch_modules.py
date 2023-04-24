import requests
from get_access_token_by_refresh_token import get_access_token

def get_modules():
    url = 'https://www.zohoapis.in/crm/v2/settings/modules'
    access_token = get_access_token()

    headers = {
        'Authorization': 'Zoho-oauthtoken {}'.format(access_token)
    }

    response = requests.get(url=url, headers=headers)

    if response is not None:
        print("HTTP Status Code : " + str(response.status_code))

        print(response.json())


get_modules()