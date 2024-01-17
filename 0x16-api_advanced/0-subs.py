#!/usr/bin/python3
"""Query Reddit API to determine subreddit sub count
"""

import requests


def number_of_subscribers(subreddit):
    """Request number of subscribers of subreddit
    from Reddit API
    """

    user_agent = 'Lin-24'
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return 0

    data = r.json()['data']
    pages = data['children']
    page_data = pages[0]['data']
    return page_data['subreddit_subscribers']
