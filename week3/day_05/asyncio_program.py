import asyncio
import requests
from pro_timer import timer
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

url = "https://httpbin.org/uuid"

async def fetch_uuid(session, url):
    with session.get(url) as response:
        json_data = await response.json()
        print(response.json()['uuid'])

async def func():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_uuid(session, url) for _ in range(100)]
        await asyncio.gether(* tasks)
        


@timer(1,1):
async def run():
    asyncio.run(func())