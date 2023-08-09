#!/usr/bin/python3
"""Define a function to get number
of subscribers from a given API"""

import requests


def number_of_subscribers(subreddit):
    """Get the numbers of subscribers
    from a given API URL"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': '0-subs/1.0'}
    con = requests.get(url, headers=header)
    if con.status_code == 200:
        data = con.json()
        subs = data['data']['subscribers']
        return subs
    else:
        return 0
