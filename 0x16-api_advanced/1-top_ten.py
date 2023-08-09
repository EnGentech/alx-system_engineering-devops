#!/usr/bin/python3
"""Query an API and get the top 10 post"""

import requests


def top_ten(subreddit):
    """Get the firt top 10 post from
    an API"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': '1-top_ten/1.0'}
    con = requests.get(url, headers=header)
    if con.status_code == 200:
        data = con.json()
        subs = data['data']['children']
        
        for post in post[:10]:
            title_content = post['data']['title']
            print(title_content)
    else:
        return 0
