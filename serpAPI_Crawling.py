import json

import serpapi
from googlesearch import search
from serpapi import GoogleSearch
from serpapi import BingSearch
from serpapi import BaiduSearch
from serpapi import YahooSearch
from serpapi import DuckDuckGoSearch


def crawl_from_google(question):
    search = GoogleSearch({
        "q": question,
        "location": "United States",
        "api_key": GoogleSearch.SERP_API_KEY
    })
    try:
        result1 = search.get_dict().get('organic_results')[0]["snippet"]
        json_object = json.dumps("organic_results: " + result1, indent=4)
    except:
        print("there is no organic_results")
    try:
        result2 = search.get_dict().get('organic_results')[0]["related_results"][0]["snippet"]
        json_object = json_object.__add__('\n')
        json_object = json_object.__add__(json.dumps("related_results: " + result2, indent=4))
    except:
        print("there is no related_results")
    try:
        result3 = search.get_dict().get("answer_box")["snippet"]
        json_object = json_object.__add__('\n')
        json_object = json_object.__add__(json.dumps("answer_box: " + result3, indent=4))
    except:
        print("there is no answer box")

    with open("googleResults.json", "w") as outfile:
        outfile.write(json_object)

    res = search.get_dict()
    js = json.dumps(res, indent=4)
    with open("google.json", "w") as outfile:
        outfile.write(js)


def crawl_from_Bing(question):
    search = BingSearch({
        "q": question,
        "location": "United States",
        "api_key": GoogleSearch.SERP_API_KEY
    })
    try:
        result1 = search.get_dict().get('organic_results')[0]["snippet"]
        json_object = json.dumps("organic_results: " + result1, indent=4)
    except:
        print("there is no organic_results")
    try:
        result2 = search.get_dict().get('organic_results')[0]["related_results"][0]["snippet"]
        json_object = json_object.__add__('\n')
        json_object = json_object.__add__(json.dumps("related_results: " + result2, indent=4))
    except:
        print("there is no related_results")
    try:
        result3 = search.get_dict().get("answer_box")["snippet"]
        json_object = json_object.__add__('\n')
        json_object = json_object.__add__(json.dumps("answer_box: " + result3, indent=4))
    except:
        print("there is no answer box")

    with open("bingResults.json", "w") as outfile:
        outfile.write(json_object)

    res = search.get_dict()
    js = json.dumps(res, indent=4)
    with open("Bing.json", "w") as outfile:
        outfile.write(js)


def crawl_from_Baidu(question):
    search = BaiduSearch({
        "q": question,
        "location": "United States",
        "api_key": GoogleSearch.SERP_API_KEY
    })
    try:
        result1 = search.get_dict().get('organic_results')[0]["snippet"]
        json_object = json.dumps("organic_results: " + result1, indent=4)
    except:
        print("there is no organic_results")
    try:
        result2 = search.get_dict().get('organic_results')[0]["related_results"][0]["snippet"]
        json_object = json_object.__add__('\n')
        json_object = json_object.__add__(json.dumps("related_results: " + result2, indent=4))
    except:
        print("there is no related_results")
    try:
        result3 = search.get_dict().get("answer_box")["snippet"]
        json_object = json_object.__add__('\n')
        json_object = json_object.__add__(json.dumps("answer_box: " + result3, indent=4))
    except:
        print("there is no answer box")
    try:
        with open("baiduResults.json", "w") as outfile:
            outfile.write(json_object)
    except:
        print("couldn't open the file in the Baidu function")

    res = search.get_dict()
    js = json.dumps(res, indent=4)
    with open("Baidu.json", "w") as outfile:
        outfile.write(js)


def crawl_from_DuckDuckGo(question):
    search = DuckDuckGoSearch({
        "q": question,
        "location": "United States",
        "api_key": GoogleSearch.SERP_API_KEY
    })
    try:
        result1 = search.get_dict().get('organic_results')[0]["snippet"]
        json_object = json.dumps("organic_results: " + result1, indent=4)
    except:
        print("there is no organic_results")
    try:
        result2 = search.get_dict().get('organic_results')[0]["related_results"][0]["snippet"]
        json_object = json_object.__add__('\n')
        json_object = json_object.__add__(json.dumps("related_results: " + result2, indent=4))
    except:
        print("there is no related_results")
    try:
        result3 = search.get_dict().get("answer_box")["snippet"]
        json_object = json_object.__add__('\n')
        json_object = json_object.__add__(json.dumps("answer_box: " + result3, indent=4))
    except:
        print("there is no answer box")
    with open("duckDuckGoResults.json", "w") as outfile:
        outfile.write(json_object)
    res = search.get_dict()
    js = json.dumps(res, indent=4)
    with open("duckDuckGo.json", "w") as outfile:
        outfile.write(js)

def crawl_from_Yahoo(question):
    search = YahooSearch({
        "q": question,
        "location": "United States",
        "api_key": GoogleSearch.SERP_API_KEY
    })
    try:
        result1 = search.get_dict().get('organic_results')[0]["snippet"]
        json_object = json.dumps("organic_results: " + result1, indent=4)
    except:
        print("there is no organic_results")
    try:
        result2 = search.get_dict().get('organic_results')[0]["related_results"][0]["snippet"]
        json_object = json_object.__add__('\n')
        json_object = json_object.__add__(json.dumps("related_results: " + result2, indent=4))
    except:
        print("there is no related_results")
    try:
        result3 = search.get_dict().get("answer_box")["snippet"]
        json_object = json_object.__add__('\n')
        json_object = json_object.__add__(json.dumps("answer_box: " + result3, indent=4))
    except:
        print("there is no answer box")
    with open("yahooResults.json", "w") as outfile:
        outfile.write(json_object)
    res = search.get_dict()
    js = json.dumps(res, indent=4)
    with open("yahoo.json", "w") as outfile:
        outfile.write(js)


if __name__ == '__main__':
    GoogleSearch.SERP_API_KEY = "19a952be597284ddf1ec5c5a3fa3425c9390e2ff2f3b1e4c23316a3a6d92df67"

    crawl_from_google("what is oco.org?")
    crawl_from_Bing("what is oco.org?")
    crawl_from_Baidu("what is oco.org")
    crawl_from_DuckDuckGo("what is oco.org?")
