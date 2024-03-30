import requests


def get_sentence():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }

    url = "https://international.v1.hitokoto.cn/?c=a&c=b&c=c&c=d&c=j"

    r = requests.get(url=url, headers=headers)
    # print('"'+r.json()["hitokoto"]+'"'+" -- "+r.json()["from"])
    # print(r.text)
    sentence = '"'+r.json()["hitokoto"]+'"'+" -- "+r.json()["from"]
    return sentence


if __name__ == '__main__':
    print(get_sentence())
