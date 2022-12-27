# Operating system
import json
import os

# regular expression library
import re

# safe queue (named Queue in python2)
from queue import Queue

# Time utility
import time

# SerpApi search
import serpapi
import urllib.request

from serpapi import GoogleSearch, BingSearch, YahooSearch, DuckDuckGoSearch, YandexSearch


def asynchronic_crawl(func):
    # store searches
    global search
    search_queue = Queue()

    # SerpApi search
    if func == 'Google':
        search = GoogleSearch({
            "location": "United States",
            "async": True,
            "api_key": "19a952be597284ddf1ec5c5a3fa3425c9390e2ff2f3b1e4c23316a3a6d92df67"
        })
    elif func == 'Bing':
        search = BingSearch({
            "location": "United States",
            "async": True,
            "api_key": "19a952be597284ddf1ec5c5a3fa3425c9390e2ff2f3b1e4c23316a3a6d92df67"
        })
    elif func == 'Yahoo':
        search = YahooSearch({
            "location": "United States",
            "async": True,
            "api_key": "19a952be597284ddf1ec5c5a3fa3425c9390e2ff2f3b1e4c23316a3a6d92df67"
        })
    elif func == 'DuckDuckGo':
        search = DuckDuckGoSearch({
            "location": "United States",
            "async": True,
            "api_key": "19a952be597284ddf1ec5c5a3fa3425c9390e2ff2f3b1e4c23316a3a6d92df67"
        })
    elif func == 'Yandex':
        search = YandexSearch({
            "location": "United States",
            "async": True,
            "api_key": "19a952be597284ddf1ec5c5a3fa3425c9390e2ff2f3b1e4c23316a3a6d92df67"
        })

    # loop through a list of companies
    with open('domains') as f:
        for company in f:
            t = company
            t = t[:-1]
            if func == 'Yahoo':
                search.params_dict["p"] = "What is the industry of " +t+"?"
            elif func == 'Yandex':
                search.params_dict["text"] = "What is the industry of " +t+"?"
            else:
                search.params_dict["q"] = "What is the industry of " +t+"?"
            result = search.get_dict()
            if "error" in result:
                print("oops error: ", result["error"])
            result = search.get_dict()


            # print("add search to the queue where id: ", result['search_metadata'])
            # add search to the search_queue
            search_queue.put(result)

    # Create regular search
    id_list = []
    while not search_queue.empty():
        result = search_queue.get()
        search_id = result['search_metadata']['id']

        # retrieve search from the archive - blocker
        search_archived = search.get_search_archive(search_id)

        # check status
        if re.search('Cached|Success', search_archived['search_metadata']['status']):
            id_list.append(search_archived['search_metadata']['json_endpoint'])
        else:
            # requeue search_queue
            search_queue.put(result)
            # wait 1s
            time.sleep(1)

        # put all the keys in an hash table and counting them
    object_counter = {}
    for i in id_list:
        get_url = urllib.request.urlopen(i)
        json_file = json.loads(get_url.read())
        keys = json_file.keys()
        for key in keys:
            object_counter[key] = 0
    for i in id_list:
        get_url = urllib.request.urlopen(i)
        json_file = json.loads(get_url.read())
        keys = json_file.keys()
        for key in keys:
            object_counter[key] += 1

        # print(id_list)
    print(object_counter)
    print('all searches completed')


if __name__ == '__main__':
    func = ['Google','Bing','Yahoo','DuckDuckGo', 'Yandex']
    for foo in func:
        asynchronic_crawl(foo)
