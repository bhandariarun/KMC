import requests
from timer import timer
from concurrent.futures import ThreadPoolExecutor

url = "https://httpbin.org/uuid"

def fetch_uuid(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])
    
@timer(1,5)
def main():
    with ThreadPoolExecutor(max_workers=100) as executor:
        with requests.Session() as session:
            executor.map(fetch_uuid, [session]*100, [url]*100)
            executor.shutdown(wait=True)