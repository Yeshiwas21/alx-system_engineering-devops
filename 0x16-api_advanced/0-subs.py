#!/usr/bin/python3
"""
This script queries the Reddit API and returns the number
of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers or 0 if the subreddit is invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = requests.get(
        f'http://www.reddit.com/r/{subreddit}/about.json',
        headers={'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /b/bicky)'}
    ).json()

    subs = url.get("data", {}).get("subscribers", 0)
    return subs
