import requests


class Request:
    _Data = {
        'end_point' : ENDPOINT,
        'headers' : {'Authorization': APIKEY}
            }

    def Listed_request():
        end_point = Request._Data['end_point']
        headers = Request._Data['headers']
        response = requests.get(url=end_point,headers=headers)
        response = response.json()
        response_item = {
            'is_active': response[0]['IsActive'],
            'warnings' : response[0]['Warnings'],
            'status_summary' : response[0]['StatusSummary'],
            'address' : response[0]['Action']['Address']
        }

        if response_item['status_summary'] == "Not Blacklisted":
            return (False, response_item)
        else:
            return (True, response_item)