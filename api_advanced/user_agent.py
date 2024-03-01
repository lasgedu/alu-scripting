#!/usr/bin/python3
import requests
import platform
import sys

def generate_reddit_user_agent():
    app_name = "lasgedu"
    version = "1.0"
    contact_info = "lasgedu"
    python_version = platform.python_version()
    system_info = platform.system()
    user_agent = f"{lasgedu}/{version} (by /u/{lasgedu}) Python/{python_version} ({system_info}; {sys.platform})"
    return user_agent

def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': generate_reddit_user_agent()}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data['data']['subscribers']
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0

if __name__ == '__main__':
    subreddit_name = input("stag12: ")
    subscribers_count = number_of_subscribers(subreddit_name)

    if subscribers_count != 0:
        print(f"The number of subscribers in /r/{subreddit_name}: {subscribers_count}")
    else:
        print(f"Invalid subreddit or an error occurred.")

