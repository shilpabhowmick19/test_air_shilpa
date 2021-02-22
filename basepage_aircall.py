import requests
from requests.auth import HTTPBasicAuth
import json


class TestData:
    api_id = "de76a30151efb543f1861aefc593cce3"
    api_token = "c17e9cd430811b8da7625070304323ac"
    base_url = "https://api.aircall.io/v1/contacts/"
    ph_no = "33652556756"
    url2 = "https://api.aircall.io/v1/contacts/search?order=asc&order_by=created_at&phone_number=33652556756%"
    url3 = "https://api.aircall.io/v1/contacts/search?order=asc&order_by=created_at&phone_number=%33652556756"
    url4 = "https://api.aircall.io/v1/contacts/search?order=asc&order_by=created_at&phone_number=£33652556756"
    url5 = "https://api.aircall.io/v1/contacts/search?order=asc&order_by=created_at&phone_number=33652556756£"
    url6 = "https://api.aircall.io/v1/contacts/search?order=asc&order_by=created_at&phone_number=£33652556756xyz"
    url7 = "https://api.aircall.io/v1/contacts/search?order=asc&order_by=created_at&phone_number=null"
    url_list = [url2, url3, url4, url5, url6, url7]
    session = requests.session()
    resp = session.get(base_url + "search?order=asc&order_by=created_at&phone_number=33652556756",
                       auth=HTTPBasicAuth(api_id, api_token))
    request_text = resp.text
    data = json.loads(request_text)
    list1 = data['contacts']
    list2 = data['meta']
