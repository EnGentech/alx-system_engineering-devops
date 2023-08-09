#!/usr/bin/python3
"""
Query an API from reddit and a list of all titles of all
hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """A function defined to query reddit API
    for the above state parameters"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(url, headers={"User-Agent": "2-recurse/1.0"},
        params={"after": after}
    )

    if req.status_code == 200:
        for con in req.json().get("data").get("children"):
            data = con.get("data")
            title = data.get("title")
            hot_list.append(title)
        after = req.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None