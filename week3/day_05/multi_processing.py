# import requests
# from multiprocessing.pool import Pool
# from pro_timer import timer

# URL = "https://httpbin.org/uuid"

# def fetch_uuid(session, url):
#     with session.get(url) as response:
#         print(response.json()['uuid'])

# @timer(1,1)
# def main():
#     with Pool() as pool:
#         with requests.Session() as session:
#             pool.starmap(fetch_uuid, [(session, URL) for _ in range(100)])


# if __name__ == "__main__":
#     main()




# from multiprocessing import Process
import requests
from multi_proccessiny_timer import timer
from multiprocessing import Pool


# print(multiprocessing.cpu_cunt())
URL = "https://httpbin.org/uuid"


def fetch_uuid(session, url):
   with session.get(url) as response:
      print(response.json()['uuid'])

@timer(1,1)
def main():
    with Pool() as pool:
        with requests.Session() as session:
            pool.starmap(fetch_uuid, [(session,URL) for _ in range(0,100)])

