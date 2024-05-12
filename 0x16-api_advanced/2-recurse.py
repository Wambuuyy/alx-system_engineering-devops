#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
CreAuthor: Prudence Wambui
"""
from json import loads
from requests import get


def recurse(subreddit, hot_list=[]):
    """recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function should return None.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 \
                        (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
    }
    response = get(url, headers=headers, allow_redirects=False)
    reddits = response.json()

    try:
        children = reddits.get('data').get('children')
        for title in children:
            hot_list.append(title.get('data').get('title'))
        return hot_list
    except Exception:
        print(None)
        return 0
