#!/usr/bin/python3
"""
contains a recursive function
that queries the Reddit API and returns a list
containing the titles of all hot articles
for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    recursive function that makes an api call
    to get the top ten hot posts in a given subreddit

    Args:
        subreddit: name of subreddit
    """
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    data = requests.get(URL,
                        headers={'User-agent': 'my-bot'},
                        params={'after': after},
                        allow_redirects=False)

    if data.status_code == 200:
        after = data.json().get('data').get('after')
        post_list = data.json().get('data').get('children')

        for post in post_list:
            hot_list.append(post.get("data").get("title"))

        if after is None:
            # If there is no new page
            if len(hot_list) == 0:
                return None

            return hot_list
        else:
            # If there is another page
            return recurse(subreddit, hot_list, after)
    else:
        return None
