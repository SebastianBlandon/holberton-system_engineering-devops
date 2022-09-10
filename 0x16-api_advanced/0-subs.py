#!/usr/bin/python3
"""
    How many subs?
    function that queries the Reddit API and returns the number of subscribers
"""
import requests

url = 'https://www.reddit.com/'


def number_of_subscribers(subreddit):
    """
        If not a valid subreddit, return 0.
    """
    path = 'r/{}/about/.json'.format(subreddit)

    response = requests.get("{}{}".format(url, path), allow_redirects=False)

    if response.status_code != 200:
        response.close()
        return 0

    data = response.json()
    response.close()

    subs = data.get('data').get('subscribers')

    return subs
