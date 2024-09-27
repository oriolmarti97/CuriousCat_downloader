import json
import requests
import time
from pathlib import Path

# Set to the username 
PROFILE = ''
URL = f'https://curiouscat.live/api/v2.1/profile?username={PROFILE}&max_timestamp={{}}'
FILENAME = f'{PROFILE}.json'
DELAY = 1


def get_oldest_saved_timestamp(info):
    if len(info['posts']) == 0:
        return int(time.time())
    timestamps = (int(x['post']['timestamp']) for x in info['posts'])
    return min(timestamps)


def read_file(filename):
    if not Path(filename).exists():
        return {
            'posts': []
        }

    with open(filename) as f:
        return json.load(f)


def get_responses(timestamp):
    url = URL.format(timestamp)
    res = requests.get(url)
    res_dict = json.loads(res.content)

    posts = res_dict['posts']
    res_dict.pop('posts', None)

    return posts, res_dict, len(posts)==0


def main():
    info = read_file(FILENAME)
    finish = False
    timestamp = get_oldest_saved_timestamp(info) - 1

    results = info['posts']

    while not finish:
        posts, res_dict, finish = get_responses(timestamp)
        not_posts = [post for post in posts if post['type']!='post']
        if len(not_posts) > 0:
            print(not_posts)
            posts = [post for post in posts if post not in not_posts]
        results.extend(posts)

        if not finish:
            timestamp = int(posts[-1]['post']['timestamp']) - 1
        info.update(res_dict)
        time.sleep(DELAY)

    info['posts'] = results

    with open(FILENAME, 'w') as f:
        json.dump(info, f, indent=4)


main()
