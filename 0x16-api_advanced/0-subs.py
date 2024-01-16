#!/usr/bin/python3
"""
0-subs
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers or 0 if the subreddit is invalid.
    """
    # Reddit API endpoint for subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'my_bot/0.1'}

    # Make the API request without following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response and extract the number of subscribers
        data = response.json().get('data', {})
        subscribers = data.get('subscribers', 0)
        return subscribers
    elif response.status_code == 404:
        # Subreddit not found, return 0
        return 0
    else:
        # Handle other errors, return 0
        print(f"Error: {response.status_code}")
        return 0

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        print("{:d}".format(number_of_subscribers(subreddit_name)))
