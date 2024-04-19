import requests
import json
from fake_useragent import UserAgent
from math import floor


def get_url_json(_url):
    response = requests.get(_url, headers={'User-Agent': UserAgent().random})
    if response.status_code == 200:
        return response.json()
    else:
        return get_url_json(_url)


def sort_type_url(_url, sort):
    sort_index = _url.find('sort=') + 5
    sort_to = _url[sort_index:].find('&') + sort_index
    return _url[:sort_index] + sort + _url[sort_to:]


def parse(_url, sort, pars_pages):
    _url = sort_type_url(_url, sort)
    collected_data = dict()
    page = 1
    data = 0
    page_index = _url.find("page=") + 5
    product_id = 1

    while page == 1 or ((data == 100 or data is not None) and page <= pars_pages):
        page_url = _url[:page_index] + str(page) + _url[page_index + 1:]
        response = get_url_json(page_url)
        data = response.get("data").get("products")
        for product in data:
            article = product.get("id")
            prod_name = product.get("name")
            cost = int(product.get("sizes")[0].get("price").get("product")) // 100
            cost_with_wallet = floor(int(cost) * 0.97)
            prod_rating = product.get("reviewRating")
            feedbacks = product.get("feedbacks")
            sizes = [size.get("name") for size in product.get("sizes")]
            colors = [color.get("name") for color in product.get("colors")]

            collected_data[product_id] = {"name": prod_name,
                                          "cost": cost,
                                          "wallet_cost": cost_with_wallet,
                                          "rate": prod_rating,
                                          "feedback": feedbacks,
                                          "colors": colors,
                                          "sizes": sizes,
                                          "article": article}
            product_id += 1
        page += 1

    with open("bot/files/result.json", "w") as file:
        json.dump(collected_data, file)
