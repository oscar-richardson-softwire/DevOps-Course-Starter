import os
import requests

def make_request(http_method, url, query = {}):
    """
    Makes a request to the Trello REST API.

    Args:
        http_method: The HTTP method to use for the request, e.g., 'GET' or 'POST'.
        url: The URL to make the request to.
        query: A dictionary of query parameters to use for the request, excluding the API key and token.

    Returns:
        response: The response from the request.
    """

    api_key = os.getenv('TRELLO_API_KEY')
    api_token = os.getenv('TRELLO_API_TOKEN')

    query['key'] = api_key
    query['token'] = api_token

    headers = {}
    if (http_method == 'POST' or http_method == 'PUT'):
        headers['Accept'] = 'application/json'

    response = requests.request(
        http_method,
        url,
        params=query,
        headers=headers
    )

    return response
