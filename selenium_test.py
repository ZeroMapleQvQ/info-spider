# -*- coding: utf-8 -*-

# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium import common
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.service import Service
import requests
import time
import pyautogui
# import logging
import json
# import sys
import os
# from tqdm import tqdm
from one_sentence import get_sentence
from excel import read_info

# logger = logging.getLogger(__file__)
# logger.setLevel(logging.INFO)

# fh = logging.FileHandler("log.txt", encoding="utf-8", mode="w")
# fh.setLevel(logging.INFO)

# ch = logging.StreamHandler()
# ch.setLevel(logging.INFO)

# logger.addHandler(fh)
# logger.addHandler(ch)

# info_list = read_info("./8.1账号.xlsx")

if os.path.exists("./info"):
    pass
else:
    os.mkdir("./info")


info_dict = {}
file_path = str(input("请输入账号文件所在路径:"))
os.system("cls")
file_path = file_path.strip("'")
file_path = file_path.strip('"')
info_list = read_info(file_path)
error_list = []
info_dir = []

sentence = get_sentence()


def print_one_sentence():
    print(get_sentence().center(120))

# LOGGER.setLevel(logging.INFO)
# ch = logging.FileHandler
# LOGGER.addHandler(ch)

# logging.basicConfig(filename="log.txt", level=logging.WARN,
#                     filemode="w", encoding="utf-8")


# caps = DesiredCapabilities.CHROME

# caps["browserName"] = "chrome"
# caps["goog:loggingPrefs"] = {"performance": "ALL"}


def spider_info(name, username, password):

    def get_text(XPATH):
        return driver.find_element(By.XPATH, XPATH).text

    def get_info():
        xm = get_text('//*[@id="XsJbxxKo"]/tbody/tr[1]/td[2]')
        info_dict["姓名"] = xm
        xb = get_text('//*[@id="XsJbxxKo"]/tbody/tr[2]/td[2]')
        info_dict["性别"] = xb
        csqr = get_text('//*[@id="XsJbxxKo"]/tbody/tr[2]/td[4]')
        info_dict["出生日期"] = csqr
        mz = get_text('//*[@id="XsJbxxKo"]/tbody/tr[3]/td[2]')
        info_dict["民族"] = mz
        sfzh = get_text('//*[@id="XsJbxxKo"]/tbody/tr[4]/td[4]')[1:]
        info_dict["身份证号"] = sfzh
        zz = get_text('//*[@id="XsJbxxKo"]/tbody/tr[6]/td[2]')
        info_dict["住址"] = zz
        return (info_dict)

    options = webdriver.ChromeOptions()

    # prefs = {'profile.default_content_settings.popups': 0,
    #          'download.default_directory': 'D:\\Project\\综评Spider\\img'}
    # options.add_experimental_option('prefs', prefs)
    # options.add_experimental_option('useAutomationExtension', False)
    # options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    # options.add_experimental_option(
    # 'perfLoggingPrefs', {'enableNetwork': False})
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--enable-logging")
    options.add_argument('--disable-extensions')
    # options.add_argument("--disable-logging")
    options.add_argument("--disable-gpu")
    options.add_argument("disable-cache")
    options.add_argument("--log-level=3")
    options.add_argument('--no-sandbox')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    # options.add_argument('--proxy-server={}'.format(BMPProxy.proxy))s

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    login_url1 = "http://www.tj.edu.cn/cxcms"
    login_url2 = "http://zxszhsz.tj.edu.cn/zhszpjcz/web/index/yhIndexSSO.htm"
    info_url = "http://zxszhsz.tj.edu.cn/zhszpjcz/web/jbqk/xsXqDack.htm?stuFlag=1"

    # sys.stdout.write("\033[F")
    # sys.stdout.write("\033[K")
    driver.get(login_url1)
    print(f"{login_url1} has opened")
    time.sleep(3)
    driver.switch_to.frame(0)
    username_elements = driver.find_element(By.NAME, value='j_username')
    password_elements = driver.find_element(By.NAME, value='j_password')
    username_elements.send_keys(username)
    print("username has sent")
    password_elements.send_keys(password)
    print("password has sent")
    login_button = driver.find_element(
        By.XPATH, '//*[@id="cms_login_win"]/div/div[7]/a')
    driver.execute_script("arguments[0].click();", login_button)
    time.sleep(3)
    print(f"{login_url1} has logged in")
    driver.get(login_url2)
    time.sleep(3)
    print(f"{login_url2} has logged in")
    driver.get(info_url)
    time.sleep(3)
    print(f"{info_url} has opened")
    info = get_info()
    print("info has got")
    # print(info)
    # if info == "":
    #     print(f"爬取失败 {name} {username} {password}\n")
    json.dump(info, open(f"./info/{name}.json", mode="w",
                         encoding="utf-8"), ensure_ascii=False, indent=4)
    time.sleep(3)
    driver.quit()


def main():
    # try:
    count = len(info_list)

    # with alive_bar(count, force_tty=True) as a_bar:
    # with tqdm(total=count, leave=False, unit="名",) as bar:
    for i in range(count):
        try:
            name = str(info_list[i]["name"])
            username = str(info_list[i]["username"])
            password = str(info_list[i]["password"])
            # bar.write(f"正在爬取 {name} {username} {password}")
            print(sentence.center(120))
            print(f"正在爬取 {name} {username} {password}")
            # print(get_sentence())
            # print_one_sentence(get_sentence())
            spider_info(name, username, password)
            continue
        except common.exceptions.NoSuchElementException:
            # a_bar
            print(f"爬取失败 {name} {username} {password}")
            print(f"登录失败 {name} {username} {password}")
            time.sleep(1)
            os.system("cls")
            # bar.update(1)
            error_list.append(name)
            continue
        except:
            pass
            # continue
    print(f"爬取失败列表: {error_list}")


if __name__ == "__main__":
    try:
        main()
        # pass
    except:
        pass

    # spider_info("李佳润", "86506187", "YCJZ@2023")

# soup = BeautifulSoup(driver.page_source)
# print(soup.prettify())
# logs = driver.get_log("performance")


# img = driver.find_element(By.ID, value="xsImg")
# action = ActionChains(driver).move_to_element(img)
# action.context_click(img).perform()
# time.sleep(1)
# pyautogui.press("v")
# time.sleep(1)
# pyautogui.press("backspace")
# time.sleep(1)
# pyautogui.write(username+".png")
# time.sleep(1)
# pyautogui.press("enter")
