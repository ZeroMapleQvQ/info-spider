import requests
import sys
import io
from urllib.parse import urljoin
from lib import *
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

login_url = "http://www.tj.edu.cn/uc/j_hh_security_check"
# index_url = "http://www.tj.edu.cn/uc/infocenter/"
index_url = "http://zxszhsz.tj.edu.cn/zhszpjcz/web/index/yhIndexSSO.htm"
post_url = "http://zxszhsz.tj.edu.cn/zhszpjcz/uc/j_hh_character_check"

username = "86506187"
password = "YCJZ@2023"

data = {
    'j_username': username,
    'j_password': password
}

# session = requests.Session()

response_login = requests.post(login_url, data=data, allow_redirects=False)
# }, allow_redirects=True)

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

# session.post(login_url, data=data, headers=headers)

# cookies = session.cookies.get_dict()
cookies = response_login.cookies.get_dict()
# print('Cookies', cookies)

response_index = requests.get(index_url, cookies=cookies, headers=headers)

# print(response_index.url)
# print('Response Cookies', response_index.cookies.get_dict())
# print('Response Status', response_index.status_code)
# print('Response URL', response_index.url)
# print("Response History", response_index.history)
# print("Response Headers", response_index.headers)

# cookie = response_index.cookies.get_dict()["JSESSIONID"]
# print(cookie)


# cookie = response_index.headers["Set-Cookie"]
# print(cookie)

# print("Response Text", response_index.text)
# print('Response URL', get_redirect_url(index_url, cookies))

def get_cookie():
    return response_index.cookies.get_dict()["JSESSIONID"]
