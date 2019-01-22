import pytest
import requests
from app import quote
import unittest.mock

@unittest.mock.patch('requests.get')
def test_request_returns_quote(mock_request):
    quote.get_todays_quote()
    mock_request.assert_called_once_with(
        'http://quotes.rest/qod.json')

@unittest.mock.patch('requests.get')
def test_parsing_json_object(mock_request):
    phrase = 'A dime a day keeps the doctor away.'
    mock_request.return_value.status_code = requests.codes.ok
    mock_request.return_value.json.return_value = {'contents': {'quotes': [{'quote': phrase}]}}
    response = quote.get_todays_quote()
    assert response == phrase
