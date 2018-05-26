#-*- coding: utf-8 -*-
'''
YWBLogin    
3.x
'''
__version__='0.1'

import string
import json
import sys
from common.basic_http import MyRequest
from conf import server_config as device
from conf import api_url as api
import time
import datetime
import random


#2.7
#reload(sys) 
#sys.setdefaultencoding('utf8')


class YWBLogin(object):

    #------------YWB login Api-------------------------------------------
    def ywb_api_login(self,phone,data):
        
        userdata=data
        userdata['phone']=phone
        ywbuser_login_url = api.API_YWB_URL['ywblogin']
       
        print(userdata,'\n',ywbuser_login_url)

        # 发送post请求
        my_request = MyRequest(ywbuser_login_url,userdata)
        response=my_request.request_post()

        res=response.json()
            
        print("response: ",res)
        
        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)   

       #返回值不报错时
        if err_flag==True:
            print('YWB login successed')          
            flag_status=1
            token=res["datas"]['loginSuccess']["token"]
            userId=res["datas"]['loginSuccess']["accountId"]
        
            print('token=',token)
            print('userId=',userId)

            return flag_status,token,userId
                      
        elif '密码错误' in ret:            
            print('YWB login error password',ret)
            flag_status = 2
            return flag_status
        
        else:
            print('Failed:YWB login failed')
            flag_status = 0
            return flag_status    

    #------------YWB salesmanquery  Api-------------------------------------------
    def ywb_salesmanQuery_api(self,phone,userid,token,data):
        
        userdata=data
        userdata['salesmanId']=userid
        ywbuser_login_url = api.API_YWB_URL['salesmanQuery'].replace('PHONE',phone).replace('id',userid).replace('TOKEN',token)

       
        print(userdata,'\n',ywbuser_login_url)

        # 发送post请求
        my_request = MyRequest(ywbuser_login_url,userdata)
        response=my_request.request_post()

        res=response.json()
            
        print("response: ",res)
        
        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)   

       #返回值不报错时
        if '操作成功' in res['info']:
            print('YWB salesmanQuery successed')          
            flag_status=1

            return flag_status,
        else:
            print('Failed:YWB salesmanQuery failed')
            flag_status = 0
            return flag_status       


    #------------YWB  cropquery Api-------------------------------------------
    def ywb_cropsQuery(self,phone,userid,token):
        
        userdata=[]
        ywbuser_url = api.API_YWB_URL['cropsQuery'].replace('PHONE',phone).replace('id',userid).replace('TOKEN',token)

        
        print(userdata,'\n',ywbuser_url)

        # 发送post请求
        my_request = MyRequest(ywbuser_url,userdata)
        response=my_request.request_post()

        res=response.json()
            
        print("response: ",res)
        
        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)   

       #返回值不报错时
        if '操作成功' in res['info']:
            print('YWB salesmanQuery successed')          
            flag_status=1

            return flag_status,
        else:
            print('Failed:YWB salesmanQuery failed')
            flag_status = 0
            return flag_status       


    #------------YWB  query farnland Api-------------------------------------------
    def ywb_query_farmland(self,phone,userid,token,data,accountId):
        
        userdata=[]
        userdata=data
        userdata['accountId']=accountId
        ywbuser_url = api.API_YWB_URL['queryFarmland'].replace('PHONE',phone).replace('id',userid).replace('TOKEN',token).replace('ACC',accountId)

        
        print(userdata,'\n',ywbuser_url)

        # 发送post请求
        my_request = MyRequest(ywbuser_url,userdata)
        response=my_request.request_post()

        res=response.json()
            
        print("response: ",res)
        
        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)   

       #返回值不报错时
        if '操作成功' in res['info']:
            print('YWB queryfarmland successed')          
            flag_status=1

            return flag_status,
        else:
            print('Failed:YWB ueryfarmland failed')
            flag_status = 0
            return flag_status       




    #------------YWB  addorder Api-------------------------------------------
    def ywb_add_Order(self,phone,userid,token,data):
        
        userdata=data
        ywbuser_login_url = api.API_YWB_URL['addOrder'].replace('PHONE',phone).replace('id',userid).replace('TOKEN',token)

        print('-----add order-----')
        headers={}
        headers['Content-Type']="multipart/form-data;"
        headers['User-Agent']="okhttp/3.4.2"
        
        print(userdata,'\n',ywbuser_login_url)

        # 发送post请求
        my_request = MyRequest(ywbuser_login_url,userdata,headers)
        #my_request = MyRequest(ywbuser_login_url,userdata)
        response=my_request.request_post()

        res=response.json()
            
        print("response: ",res)
        
        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)   

       #返回值不报错时
        if '操作成功' in res['info']:
            print('YWB salesmanQuery successed')          
            flag_status=1

            return flag_status,
        else:
            print('Failed:YWB salesmanQuery failed')
            flag_status = 0
            return flag_status       



if __name__ == "__main__" :

    my_obj = YWBLogin()

    data2= {
            'phone':'19900001001',
            "passWord":"123qwe",
    }
    datalist=my_obj.ywb_api_login(phone,userdata)
    print(datalist)
    
