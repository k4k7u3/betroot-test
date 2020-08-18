import asyncio
from aiohttp_requests import requests
import json

url = 'https://api.pushshift.io/reddit/search/comment/'
data = {}
line = []
thems = ['soccer', 'AskReddit', 'ireland']


async def req(url, i):
    global data, line
    print("start")
    resp = await requests.get(url, params={"sort": 'new', 'subreddit': i})
    print("Close")
    return await resp.json()


def load_json(data):
    comments = {}
    for i in range(0, 3):
        line = []
        for j in data[i]['data']:
            line.append(j['body'])
        comments[thems[i]] = line
    line = []
    line.append(comments)
    try:
        with open('comments.json', 'w+') as json_file:
            json.dump(line, json_file, indent=4)
    finally:
        print("Yeeah baby")


if __name__ == "__main__":
    cor = [req(url, i) for i in thems]
    data = asyncio.get_event_loop().run_until_complete(asyncio.gather(*cor))
    load_json(data)
