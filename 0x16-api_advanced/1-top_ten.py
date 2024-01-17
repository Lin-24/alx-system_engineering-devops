#!/usr/bin/python3
"""Query Reddit API to determine subreddit sub count
"""

import requests


def top_ten(subreddit):
    """Request top ten hot posts of subreddit from Reddit API
    """
    user_agent = 'Lin-24'
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        print('None')
    else:
        data = r.json()['data']
        posts = data['children']
        for post in posts:
            print(post['data']['title'])
