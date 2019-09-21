import os
import sys
import urllib
import requests
import time
import multiprocessing

def image_collector(subreddit):
    # url = "https://www.reddit.com/r/"
    # url_end = "/top/.json?t=week&count=20"
    #
    # for item in subreddits:
    #     final_url = url + item + url_end
    #     r = requests.get(final_url,  headers = {'User-agent': 'your bot 0.1'})
    #     subreddit = r.json()
    #
    #     for i in range(len(subreddit['data']['children'])):
    #         domain = subreddit['data']['children'][i]['data']['domain']
    #         if domain != "i.redd.it" and domain != "i.imgur.com" and domain != "m.imgur.com":
    #             continue
    #         post_url = subreddit['data']['children'][i]['data']['url']
    #
    #         if "imgur" in post_url:
    #             if post_url[-4:] != ".jpg":
    #                 post_url = post_url + ".jpg"
    #
    #         folder_location = item + "/"
    #         image_name = os.path.basename(post_url)
    #         image_name = image_tag(subreddit['data']['children'][i]['data'])
    #         urllib.request.urlretrieve(post_url, folder_location + image_name)
    #         print ("Downloading " + subreddit['data']['children'][i]['data']['title'] + " in r/" + item + " as " + image_name)
    url = "https://www.reddit.com/r/"
    url_end = "/top/.json?t=year&count=20"

    final_url = url + subreddit + url_end
    r = requests.get(final_url, headers={'User-agent': 'your bot 0.1'})
    posts = r.json()

    for i in range(len(posts['data']['children'])):
        post = posts['data']['children'][i]['data']
        image_tag(post)
        domain = post['domain']
        if domain != "i.redd.it" and domain != "i.imgur.com" and domain != "m.imgur.com":
            continue
        post_url = post['url']

        if "imgur" in post_url:
            if post_url[-4:] != ".jpg":
                post_url = post_url + ".jpg"

        folder_location = subreddit + "/"
        image_name = image_tag(post)
        urllib.request.urlretrieve(post_url, folder_location + image_name)
        print("Downloading " + post['title'] + " in r/" + subreddit + " as " + image_name)

def initial(subreddit):
    url = "https://www.reddit.com/r/"
    url_end = "/top/.json?t=year&count=100"

    final_url = url + subreddit + url_end
    r = requests.get(final_url, headers={'User-agent': 'your bot 0.1'})
    posts = r.json()

    for i in range(len(posts['data']['children'])):
        post = posts['data']['children'][i]['data']
        image_tag(post)
        domain = post['domain']
        if domain != "i.redd.it" and domain != "i.imgur.com" and domain != "m.imgur.com":
            continue
        post_url = post['url']

        if "imgur" in post_url:
            if post_url[-4:] != ".jpg":
                post_url = post_url + ".jpg"

        folder_location = subreddit + "/"
        image_name = image_tag(post)
        urllib.request.urlretrieve(post_url, folder_location + image_name)
        print("Downloading " + post['title'] + " in r/" + subreddit + " as " + image_name)

def image_tag(post):
    when = time.strftime("%Y%m%d", time.gmtime(post["created_utc"]))
    post_url = post['url']
    base_filename = os.path.basename(post_url)
    filename = "[" + when + "]" + base_filename

    return filename

def dir_check(subreddits):
    jobs = []
    for item in subreddits:
        if not os.path.exists(item):
            print ("Creating " + item + " directory")
            os.makedirs(item)
            p = multiprocessing.Process(target=initial, args=(item,))
            jobs.append(p)
            p.start()
            #initial(item)

def main():
    jobs = []
    with open(os.path.join(sys.path[0], "subreddit_list.txt"), "r") as f:
        subreddits = f.read().splitlines()

    dir_check(subreddits)

    for item in subreddits:
        p = multiprocessing.Process(target=image_collector, args=(item,))
        jobs.append(p)
        p.start()

if __name__ == '__main__':
    main()