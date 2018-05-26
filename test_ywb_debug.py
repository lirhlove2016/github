#-*- coding: utf-8 -*-
'''
testcase_for_YWB  
3.x
'''

import string
import json
import sys
import time
import datetime

from conf import server_config as device
from  data import Ywbuser_testdata as ywbuser
from  data import System_Management_testdata as sysuser

from modules.YWB_UserLogin import YWBLogin as YWBLogin


#data
my_obj = YWBLogin()

headers=device.DICT__HTTP_HEADERS_002

phone="18301212965"
ywbuserdata=ywbuser.testdata_YWB_login_userdata_001
salesmandata=ywbuser.testdata_YWB_salesmanquery_001

addorderdata=ywbuser.testdata_YWB_add_Order_all_001
queryfarmlanddata=ywbuser.testdata_YWB_queryfarmland_001



#case1--YWB用户登录
#--------------------------------------------------------  
def test_ywb_login(phone,userdata):
    datalist=[]
    #返回值
    datalist=my_obj.ywb_api_login(phone,userdata)
    #print(datalist)
    
    if datalist[0]!=1:
        print('fail')
        return None
    else:
        return datalist

#case2--YWB订单-选择客户
#--------------------------------------------------------  
def test_ywb_salemanquery(phone,userid,token,data):
    datalist=[]
    #返回值
    datalist=my_obj.ywb_salesmanQuery_api(phone,userid,token,data)
    #print(datalist)
    
    if datalist[0]!=1:
        print('fail')
        return None
    else:

        return datalist



#case3--YWB-cropquery
#--------------------------------------------------------  
def test_crop_query(phone,userid,token):
    datalist=[]
    #返回值
    datalist=my_obj.ywb_cropsQuery(phone,userid,token)
    #print(datalist)
    
    if datalist[0]!=1:
        print('fail')
        return None
    else:
        return datalist

#case4--YWB-queryfarmland
#--------------------------------------------------------  
def test_query_farmland(phone,userid,token,data,accountId):
    datalist=[]
    #返回值
    datalist=my_obj.ywb_query_farmland(phone,userid,token,data,accountId)
    #print(datalist)
    
    if datalist[0]!=1:
        print('fail')
        return None
    else:
        return datalist

#case3--YWB订单-下订单
#--------------------------------------------------------  
def test_add_order(phone,userid,token,data):
    datalist=[]
    #返回值
    datalist=my_obj.ywb_add_Order(phone,userid,token,data)
    #print(datalist)
    
    if datalist[0]!=1:
        print('fail')
        return None
    else:
        return datalist



#执行调试
#---------------------------------------------------


#step1:ywb_login
re=test_ywb_login(phone,ywbuserdata)


#step2：ywb select salesman
userid=re[2]
token=re[1]
#test_ywb_salemanquery(phone,userid,token,salesmandata)


#step3:crop query
#test_crop_query(phone,userid,token)


#step4:farmland
#accountId='809'
#accountId='p1523516849945S26f38a34-3f45-4d68-8138-addd91d0dbb2'
accountId='big1523516703430S8437f197-5bc5-4184-a4ea-4314dc8f6b5e'
#test_query_farmland(phone,userid,token,queryfarmlanddata,accountId)


print('---------START Add Order TEST-------------')
#STEP3:ywb add order
test_add_order(phone,userid,token,addorderdata)


