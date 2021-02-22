from http import HTTPStatus
from basepage_aircall import TestData
import null
import requests
from requests.auth import HTTPBasicAuth
import re


'''Assertion to check firstname,last name,company name, information etc is not null/empty 
if the attribute is present in json list'''


def test_json_contacts():
    for contacts_data in TestData.list1:
        assert str(contacts_data['direct_link']) == TestData.base_url + str(contacts_data['id'])
        assert len(contacts_data) != 0
        assert len(contacts_data) is not null
        assert len(str(contacts_data['id'])) != 0
        assert len(str(contacts_data['first_name'])) != 0
        assert str(contacts_data['first_name']) is not null
        assert len(str(contacts_data['company_name'])) != 0
        assert str(contacts_data['company_name']) is not null
        assert len(str(contacts_data['information'])) != 0
        assert str(contacts_data['information']) is not null
        assert str(contacts_data['last_name']) is not null
        assert len(str(contacts_data['last_name'])) != 0
        assert bool(str(contacts_data['is_shared'])) is True


'''Assertion to check conditional mandatory field for firstname,lastname and company name '''


def test_json_names_condition():
    for contacts_data in TestData.list1:
        assert 'first_name' in contacts_data
        assert 'last_name' in contacts_data
        assert 'company_name' in contacts_data
        c_data = [contacts_data['first_name'], contacts_data['last_name'], contacts_data['company_name']]
        assert c_data.count("") <= 2


'''To check  phone numbers in list.label and value is present and not empty '''


def test_phone_number_value():
    for contacts_data in TestData.list1:
        assert len(contacts_data['phone_numbers']) != 0
    for phone_data in TestData.list1:
        phone_detail = phone_data['phone_numbers']
        all_phone = []
        for phone_key in phone_detail:
            assert len(str(phone_key['label'])) != 0
            assert len(str(phone_key['value'])) != 0
            all_phone.append(phone_key['value'])
        assert TestData.ph_no in str(all_phone)


'''To check  response code 200 for phone number parameters with alphanumeric,null,special character etc'''


def test_get_status():
    for url in TestData.url_list:
        response = requests.get(url, auth=HTTPBasicAuth(TestData.api_id, TestData.api_token))
        assert response.status_code == HTTPStatus.OK


'''To test all email in response json and it is matching email format regex'''


def test_email():
    for contacts_data in TestData.list1:
        assert len(contacts_data['emails']) != 0
    email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    all_email = []
    for contacts_data in TestData.list1:
        email_details = contacts_data['emails']
        for email_key in email_details:
            all_email.append(email_key['value'])
    print(f'the email is :' + str(all_email))
    for email in all_email:
        print(email)
        try:
            assert re.match(email_pattern, email) is not None
            print("valid email")
        except AssertionError:
            print("Invalid email format")

