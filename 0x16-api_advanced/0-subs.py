#!/usr/bin/python3
"""Checks the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers in a subreddit """

    headers = {'User-Agent': 'my_user_agent/0.1 by your_username'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0

