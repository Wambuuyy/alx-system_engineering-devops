#!/usr/bin/python3
"""
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number
    of subscribers for a given subreddit.
    Args:
        subreddit (str): The name of the subreddit.
    Returns:
        int: The number of subscribers of the subreddit.
        Returns 0 if the subreddit is invalid or not found.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}

    try:
        response = get(url, headers=headers)
        response.raise_for_status()
        reddits = response.json()
        subscribers = reddits.get('data', {}).get('subscribers', 0)
        return int(subscribers)
    except Exception as e:
        print("Error:", e)
        return 0
