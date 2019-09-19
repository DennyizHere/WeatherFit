import json
import os
import sys
import urllib
import json
import requests

def image_collector(subreddits):
    url = "https://www.reddit.com/r/"
    url_end = "/top/.json?t=week&count=20"

    for item in subreddits:
        final_url = url + item + url_end
        r = requests.get(final_url,  headers = {'User-agent': 'your bot 0.1'})
        subreddit = r.json()

        for i in range(len(subreddit['data']['children'])):
            domain = subreddit['data']['children'][i]['data']['domain']
            if domain != "i.redd.it" and domain != "i.imgur.com" and domain != "m.imgur.com":
                continue
            post_url = subreddit['data']['children'][i]['data']['url']

            if "imgur" in post_url:
                if post_url[-4:] != ".jpg":
                    post_url = post_url + ".jpg"

            folder_location = item + "/"
            image_name = os.path.basename(post_url)
            urllib.request.urlretrieve(post_url, folder_location + image_name)
            print ("Downloading " + subreddit['data']['children'][i]['data']['title'] + " in r/" + item)

def initial(subreddit):
    url = "https://www.reddit.com/r/"
    url_end = "/top/.json?t=year&count=100"

    final_url = url + subreddit + url_end
    r = requests.get(final_url, headers={'User-agent': 'your bot 0.1'})
    posts = r.json()

    for i in range(len(posts['data']['children'])):
        domain = posts['data']['children'][i]['data']['domain']
        if domain != "i.redd.it" and domain != "i.imgur.com" and domain != "m.imgur.com":
            continue
        post_url = posts['data']['children'][i]['data']['url']

        if "imgur" in post_url:
            if post_url[-4:] != ".jpg":
                post_url = post_url + ".jpg"

        folder_location = subreddit + "/"
        image_name = os.path.basename(post_url)
        urllib.request.urlretrieve(post_url, folder_location + image_name)
        print("Downloading " + posts['data']['children'][i]['data']['title'] + " in r/" + subreddit)

def dir_check(subreddits):
    for item in subreddits:
        if not os.path.exists(item):
            print ("Creating " + item + " directory")
            os.makedirs(item)
            initial(item)

def main():

    with open(os.path.join(sys.path[0], "subreddit_list.txt"), "r") as f:
        subreddits = f.read().splitlines()

    dir_check(subreddits)

    print (subreddits)
    image_collector(subreddits)

if __name__ == '__main__':
    main()