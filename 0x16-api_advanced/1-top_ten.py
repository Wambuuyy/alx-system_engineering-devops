#!/usr/bin/python3
"""
created 6:58 pm 7th july 2024
@author: Prudence Wambui
"""
from json import loads
from requests import get


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
    'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
    }
    response = get(url, headers=headers, allow_redirects=False)
    reddits = response.json()

    try:
        children = reddits.get('data').get('children')
        for i in range(10):
            print(children[i].get('data').get('title'))
    except Exception:
        print('None')
