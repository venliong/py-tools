#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import os

# 登录【邮箱、手机】接口
URL_LOGIN_EMAIL = 'https://juejin.im/auth/type/email'
URL_LOGIN_PHONENUMBER = 'https://juejin.im/auth/type/phoneNumber'

# 获取自己够买的小册列表接口
URL_ARTICLE_BUY = 'https://xiaoce-cache-api-ms.juejin.im/v1/userBuyList'

# 获取小册文章列表接口
URL_ARTICLE_CATALOG = 'https://xiaoce-cache-api-ms.juejin.im/v1/getListSection'

# 获取小册单章节数据接口
URL_ARTICLE_CONTENT = 'https://xiaoce-cache-api-ms.juejin.im/v1/getSection'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Content-Type': 'application/json'
}

cwpath = os.getcwd()


class JueJin:
    def __init__(self, loginType=1, account=None, pwd=None, uid=None, clientId=None, token=None):
        self.loginType = loginType
        self.account = account
        self.pwd = pwd
        self.uid = uid
        self.clientId = clientId
        self.token = token


# 创建文件夹
def create_folder(folder):
    path = os.path.join(cwpath, folder)
    if not os.path.exists(path):
        os.makedirs(path)
        print('====创建目录', path)
    return path


# 写到文本中
def write2_file(path, title, content, prefix):
    fileName = path + '\\' + title + prefix
    fileName = fileName.replace('"', "").replace("?", "").replace("？", "").strip()
    f = open(fileName, mode='w', encoding='utf-8')
    try:
        f.write(content)
        print("====写入", fileName)
    except Exception:
        print("====fail", fileName)


# 获取小册中具体文本内容
def get_article_content(catalogName, dataList):
    params = {
        'uid': jin.uid,
        'client_id': jin.clientId,
        'src': 'web',
        'token': jin.token
    }
    path = create_folder(catalogName)
    for data in dataList:
        params['sectionId'] = data['_id']
        rep = requests.get(url=URL_ARTICLE_CONTENT, params=params)
        if rep.status_code == 200:
            resp = rep.json()
            data = resp['d']
            title = data['title']
            htmlData = data['html']
            mdData = data['content']
            write2_file(path, title, htmlData, '.html')
            write2_file(path, title, mdData, '.md')


# 获取小册中目录
def get_article_catalog(articleList):
    params = {
        'uid': jin.uid,
        'client_id': jin.clientId,
        'src': 'web',
        'token': jin.token
    }
    for article in articleList:
        params['id'] = article['id']
        rep = requests.get(url=URL_ARTICLE_CATALOG, params=params, headers=headers)
        if rep.status_code == 200:
            resp = rep.json()
            dataList = resp['d']
            catalogName = article['title']
            get_article_content(catalogName, dataList)


# 获取购买的小册数据
def get_buy_article_list():
    params = {
        'uid': jin.uid,
        'client_id': jin.clientId,
        'src': 'web',
        'token': jin.token
    }
    rep = requests.get(url=URL_ARTICLE_BUY, params=params)
    buyList = []
    if 200 == rep.status_code:
        print("====获取到购买列表成功")
        resp = rep.json()
        articleArrayData = resp['d']
        for article in articleArrayData:
            buyDict = {}
            buyDict['title'] = article['title']
            buyDict['id'] = article['_id']
            buyList.append(buyDict)
        get_article_catalog(buyList)
    else:
        print("未正确获取到" + jin.account + "下够买的小册数据.")
        exit()


# 登录
def login():
    print("====login.....")
    login_url = URL_LOGIN_PHONENUMBER
    loginObj = {"password": jin.pwd}
    if jin.loginType == 0:
        login_url = URL_LOGIN_EMAIL
        loginObj['email'] = jin.account
    else:
        loginObj['phoneNumber'] = jin.account
    rep = requests.post(login_url, data=json.dumps(loginObj), headers=headers)
    if rep.status_code == 200:
        print("====login sucess")
        resp = rep.json()
        jin.token = resp['token']
        jin.uid = resp['userId']
        jin.clientId = resp['clientId']
        get_buy_article_list()
    else:
        print("====登录失败.....")
        exit()


if __name__ == '__main__':
    jin = JueJin()
    jin.loginType = input("LoginType 0为邮箱 1为手机:")
    jin.account = input("Account:")
    jin.pwd = input("Password:")
    login()
    print('====下载操作完成')
