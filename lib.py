import requests


def get_redirect_url(url, cookies=None):

    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

    response = requests.get(url, headers=headers, cookies=cookies)

    print('Response URL', response.url)


if __name__ == '__main__':
    index_url = "http://zxszhsz.tj.edu.cn/zhszpjcz/web/index/yhIndexSSO.htm"
    get_redirect_url(index_url)
