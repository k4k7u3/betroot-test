import asyncio
from aiohttp_requests import requests
import json

url = 'https://api.pushshift.io/reddit/comment/search/'
data = {}
line = []


async def req(url):
    global data
    resp = await requests.get(url)
    data = await resp.json()
    print("Close")


async def load_json():
    global data, line
    data1 = {}
    if data == {}:
        await asyncio.sleep(5)
    for i in range(0, len(data['data'])):
        data1[f'{i}'] = data['data'][i]['body']
    line.append(data1)
    try:
        with open('comments.json', 'w+') as json_file:
            json.dump(line, json_file, indent=4)
    finally:
        print("Yeeah baby")


event_loop = asyncio.get_event_loop()
try:
    event_loop.create_task(req(url))
    event_loop.create_task(load_json())
    event_loop.run_forever()
finally:
    event_loop.close()
