#!/usr/bin/python3
"""
created at 5:47 pm on 7th may 2024
@author: Prudence Wambui
"""
from json import loads
from requests import get


def number_of_subscribers(subreddit):
    """recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given
    subreddit.  if number of results are found for the given subreddit,
    the function should return None"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Google Chrome Version 124.0.6367.63 '
    }
    response = get(url, headers=headers)
    reddits = response.json()

    try:
        subscribers = reddits.get('data').get('subscribers')
        return int(subscribers)
    except Exception:
        return 0
