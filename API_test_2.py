import requests
import json

# 得到result_linus.json
endpoints = 'https://api.github.com/graphql'
ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit' \
        '/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
token = 'token 18064256b17a4f4f05dc558ffb6d33c8676b3751'
h = {'User-Agent': ua, 'Authorization': token}


def get_response(url, json_data=None):
    try:
        r = requests.post(url=url, json=json_data, headers=h)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except Exception as e:
        print(e)
        return None


def get_query():
    with open('query.gql', 'r', encoding='utf-8') as fr:
        return fr.read()


if __name__ == "__main__":

    j = {}
    with open('result_linus.json', 'r', encoding='utf-8') as f:
        j = json.load(f)

    followers = j['data']['user']['followers']
    totalCount = followers['totalCount']
    cursor = followers['edges'][0]['cursor']
    print(totalCount)
    print(cursor)

    while totalCount:
        totalCount -= 1
        print(totalCount)

    # query = get_query()
    # j = {"query": query, "variables": {}, "operationName": None}
    # response = get_response(endpoints, json_data=j)
    # r_content = response.content
    # result = json.loads(r_content)
    # with open('result.json', 'w', encoding='utf-8') as f:
    #     f.write(json.dumps(result, indent=4))


