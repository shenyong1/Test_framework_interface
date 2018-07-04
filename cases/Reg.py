# -*- coding:utf-8 -*-

import unittest,ddt,requests
from BeautifulReport import BeautifulReport as bf
from urllib import parse
from conf.setting import BASE_URL


@ddt.ddt
class Reg(unittest.TestCase):

    # base_url = 'http://118.24.3.40/'

    @ddt.file_data(r'E:\shenyong\作业练习\day14-测试框架\day14-1\UTP\case_data\reg.yml') #读文件，获取数据
    def test_request(self,**kwargs):
        detail = kwargs.get('detail','没有用例描述')
        self._testMethodDoc = detail #动态设置用例描述

        url = kwargs.get('url')
        url = parse.urljoin(BASE_URL,url)
        print(url)

        method = kwargs.get('method','get')#若没值，默认取get
        print(method)
        data = kwargs.get('data',{})
        print(data)
        header = kwargs.get('header',{})
        cookie = kwargs.get('cookie',{})
        check = kwargs.get('check')

        method = method.lower()
        try:
            if method == 'get':
                res = requests.get(url,params=data,headers=header,cookies=cookie).text

            else:
                res = requests.post(url,data=data,headers=header,cookies=cookie).text
        except Exception as e:
            print('接口请求出错')
            res = e
            print(res)

        for c in check:
            self.assertIn(c,res,msg='预计结果不符，预期结果'+c+'实际结果'+res)

