import requests
from bs4 import BeautifulSoup

headers = {
    # "Accept": "*/*",
    # "Accept-Encoding": "gzip, deflate",
    # "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    # "Content-Length": "1520",
    # "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    # "Cookie": cookie2,
    # "Cookie": "gznotes-visited=true; Hm_lvt_f05f30f702742b6da7e05b7a691087cc=1711187817,1711195109; Hm_lpvt_f05f30f702742b6da7e05b7a691087cc=1711195220; JSESSIONID=ahlrRm8kMjbby7gz9oJHHC0izGVNe7QXVqbBDUJzSqYfzVSW--rN!-1475155454",
    # "HHCSRFToken": "55888166-4cdb-4518-9412-526c8928cd45",
    # "Host": "zxszhsz.tj.edu.cn",
    # "Origin": "http://zxszhsz.tj.edu.cn",
    # "Proxy-Connection": "keep-alive",
    # "Referer": "http://zxszhsz.tj.edu.cn/zhszpjcz/web/jbqk/xsXqDack.htm?stuFlag=1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    # "X-Requested-With": "XMLHttpRequest"
}

login_url = "http://zxszhsz.tj.edu.cn/zhszpjcz/uc/j_hh_character_check"

# print(get_cookie)

username = ""
password = ""

login_data = {
    'j_username': username,
    'j_password': password
}

login_url1 = "http://www.tj.edu.cn/uc/j_hh_security_check"

session = requests.Session()

response_login = session.post(
    login_url1, data=login_data, allow_redirects=True)

cookie1 = session.cookies.get_dict()["JSESSIONID"]
# cookie1 = response_login.cookies.get_dict()

cookie1_dick = {
    "Cookie": cookie1
}

r_login = requests.post(
    login_url, headers=headers, cookies=cookie1_dick, allow_redirects=False)
# print(r_login.status_code)
# print(r_login.url)

cookie2 = r_login.cookies.get_dict()["JSESSIONID"]

r = requests.get(
    url="http://zxszhsz.tj.edu.cn/zhszpjcz/uc/character.htm", headers=headers, cookies={"Cookie": cookie2})
print(r.status_code)
print(r.url)
# print(r_login.url)

# cookie_str = "gznotes-visited=true;JSESSIONID=ahlrRm8kMjbby7gz9oJHHC0izGVNe7QXVqbBDUJzSqYfzVSW--rN!-1475155454"
# cookie_str = "gznotes-visited=true; Hm_lvt_f05f30f702742b6da7e05b7a691087cc=1711187817,1711195109; Hm_lpvt_f05f30f702742b6da7e05b7a691087cc=1711195220; JSESSIONID=ahlrRm8kMjbby7gz9oJHHC0izGVNe7QXVqbBDUJzSqYfzVSW--rN!-1475155454"
# cookie = {}

# for line in cookie_str.split(';'):
#     key, value = line.split('=', 1)
#     cookie[key] = value

url1 = "http://zxszhsz.tj.edu.cn/zhszpjcz/web/common/head.do"
url2 = "http://zxszhsz.tj.edu.cn/zhszpjcz/web/jbqk/xsXqDack.do"
url3 = "http://zxszhsz.tj.edu.cn/zhszpjcz/web/jbqk/xsXqDack.htm?stuFlag=1"
url4 = "http://zxszhsz.tj.edu.cn/zhszpjcz/web/index/yhIndex.htm"

r = requests.get(url4, headers=headers, allow_redirects=True,
                 cookies={"Cookie": cookie2, "_walkthrough-introduction": "0"})
cookie3 = r.cookies.get_dict()["JSESSIONID"]
# print(r.headers)
# print(r.url)
# print(r.status_code)
# print(r.headers)

r_index = requests.get(url2,
                       cookies={"Cookie": cookie3}, headers=headers, allow_redirects=False)
# print(r_index.status_code)
# print(r_index.url)
# print(r_index.text)

print("Cookie1", cookie1)
print("Cookie2", cookie2)
# print("Cookie3", cookie3)
