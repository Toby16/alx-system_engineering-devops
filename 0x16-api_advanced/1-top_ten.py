#!/usr/bin/python3
"""
COntains function that queries the Reddit API
and prints the titles of the first 10 hot posts listed
for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    function that makes an api call
    to get the top ten hot posts in a given subreddit

    Args:
        subreddit: name of the subreddit
    """
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    data = data = requests.get(URL,
                               headers={'User-agent': 'my-bot'},
                               allow_redirects=False)

    if data.status_code == 200:
        post_list = data.json().get('data').get('children')
        counter = 0
        for post in post_list:
            if counter == 10:
                break
            print(post.get("data").get("title"))
            counter += 1
    else:
        print("None")
