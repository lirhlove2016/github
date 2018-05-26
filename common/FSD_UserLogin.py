#-*- coding: utf-8 -*-
'''
FSDLogin    
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


class FSDLogin(object):

    #------------FSD login Api-------------------------------------------
    def fsd_api_login(self,phone,flyuser_data):
        
        userdata=flyuser_data
        userdata['phone']=phone
        flyuser_login_url = api.API_URL['fsdlogin']
       
        print(userdata,'\n',flyuser_login_url)

        # 发送post请求
        my_request = MyRequest(flyuser_login_url,userdata)
        reslist=my_request.request_token_fsd()

        res=reslist[0]
        token=reslist[1]
        userId=reslist[2]
        
        #print('token=',token)
        #print('userId=',userId)

        res=res.json()
        print("response: ",res)
        

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        #print(ret)   

       #返回值不报错时
        if err_flag==True:
            print('FSD login successed')          
            flag_fsd_login_status=1
            return flag_fsd_login_status,token,userId
                      
        elif '密码不正确' in ret:            
            print('FSD login error password',ret)
            flag_fsd_login_status = 2
            return flag_fsd_login_status
        elif '账户已冻结' in ret:
            print('Freeze fly account can not login',ret)
            flag_fsd_login_status = 3
            return flag_fsd_login_status
        else:
            print('Failed:FSD login failed')
            flag_fsd_login_status = 0
            return flag_fsd_login_status    

        
    #------------System Management login ------------------------------------------
    def system_management_login(self,sys_data):
        userdata=sys_data
        request_url = api.API_URL['syslogin']
        
        print(userdata,'\n',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)

        reslist=my_request.request_token_sys()
        res=reslist[0]
        farmtoken=reslist[1]
        
        print('farmtoken=',farmtoken)
        
        res=res.json()
        print("response ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_management(res)     
        print(ret)
        
        #返回值不报错时
        if err_flag==True:  

            #登录成功，返回登录状态flag,token
            print('passed:System login successed')
            flag_sys_login_status=1
            return flag_sys_login_status,farmtoken
        else:
            print('Failed:System login failed')
            flag_sys_login_status = 0
            return flag_sys_login_status    


    #------------System Management Freeze flyuser ------------------------------------------
    def sysment_management_freeze_flyuser(self,userid,token):
        #只传入userid

        userdata={}
        userdata["id"]=userid
        userdata["state"]=3
        headers={}
        headers['FARMFRIEND_TOKEN']=token
        
        request_url = api.API_URL['freezeflyaccount']

        print(userdata,'\n',request_url,headers)
        # 发送post请求
        my_request = MyRequest(request_url,userdata,headers)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)
        #转换成Str
        jsonres=json.dumps(res)

        # 解析response返回信息

        if 'SUCCESS' in jsonres:
            print('Passed: freeze fly account successed')
            flag_freez_ret = 1
            return flag_freez_ret
        else:
            print('Failed:freeze fly account failed')
            flag_freez_ret = 0
            return flag_freez_ret


    #------------System Management not Freeze flyuser ------------------------------------------
    def sysment_management_nofreeze_flyuser(self,userid,token):
        #只传入userid

        userdata={}
        userdata["id"]=userid
        userdata["state"]=2

        heads={}
        heads['FARMFRIEND_TOKEN']=token
        
        request_url = api.API_URL['freezeflyaccount']
        print(userdata,'\n',request_url)
        # 发送post请求
        my_request = MyRequest(request_url,userdata,heads)
        res = my_request.request_token_post(token)
        
        res=res.json()
        print("response: ",res)

        jsonres=json.dumps(res)
        # 解析response返回信息
        if 'SUCCESS' in jsonres:
            print('Passed: no freeze fly account successed')
            flag_freez_ret = 1
            return flag_freez_ret
        else:
            print('Failed:no freeze fly account failed')
            flag_freez_ret = 0
            return flag_freez_ret
   

    #------------FSD Register api ------------------------------------------
    def fsd_api_register(self,phone):
        userdata={}
        request_url = api.API_URL['fsdregister']
        
        print('Test data and api url |',userdata,'| ',request_url)
        
        userdata['phone']=phone
        # 发送post请求
        my_request = MyRequest(request_url,userdata)

        reslist=my_request.request_token_fsd()

        res=reslist[0]
        token=reslist[1]
        userId=reslist[2]
        
        print('token=',token)
        print('userId=',userId)

        res=res.json()
        print("response: ",res)
        
        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        #print(ret)

        #返回值不报错时
        if err_flag==True:

            print('FSD register successed')          
            flag_status=1
            return flag_status,token,userId
                      
        else:
            print('FSD register failed')
            flag_fsd_login_status = 0
            return flag_fsd_login_status                

    
    #------------FSD set password  ------------------------------------------
    def flyuser_set_password(self,accesstoken,ids,phone,password):
        userdata={}
        userdata['userId']=ids
        userdata['password']=password
        userdata['phone']=phone
        userdata['token']=accesstoken
        
        request_url = api.API_URL['fsdusersetpassword']
       
        print(userdata,'\n',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)
        

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        if res['info']=='操作成功':
            print('Passed: flyuser set password successed')
            flag_fsd_setpassword = 1
            return flag_fsd_setpassword
        else:
            print('Failed:flyuser set password failed')
            flag_fsd_setpassword = 0
            return flag_fsd_setpassword


    #------------random phone number ------------------------------------------
    def ramdom_phone_number(self):

        # 配置FSD信息
        num_start = ['142','143','141','144','140']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits,8))
        res = start+end
        return res


    #------------FSD add tools ------------------------------------------
    def add_fsd_tools(self,data,ids,token):
        userdata=data
        userdata['id']=ids
        userdata['TOKEN']=token
        
        request_url = api.API_URL['addtools'].replace("id",ids).replace("TOKEN",token)
        
        print(userdata,'\n',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #jsonres=json.dumps(res)
        if res['info']=='操作成功':

            print('Passed: flyuser add tools successed. ')
            flag_fsd_add_tools = 1
            return flag_fsd_add_tools
        else:
            print('Failed: flyuser add tools failed')
            flag_fsd_add_tools = 0
            return flag_fsd_add_tools


    #------------FSD check account api  ------------------------------------------
    def fsd_check_account(self,check_userdata):

        userdata=check_userdata
        request_url = api.API_URL['fsdcheckaccount']
        
        print(userdata,'\n',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)
        
        
        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        #将字典转换成字符
        ret=json.dumps(ret)
        if 'user not exist' in ret:
            print(' flyuser account not exist')
            flag_fsd = 1 
        
        else:
            print('flyuser account  exist')
            flag_fsd = 0
 
        return flag_fsd

    #------------FSD create flyuser team api ------------------------------------------
    def fsd_create_flyuser_team(self,ids,token,flyuserteamdata):

        userdata=flyuserteamdata       
        print(userdata)
        ids=str(ids)
        request_url = api.API_URL['createflyuserteam'].replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        if res['info']=='操作成功':
            print('Passed: FSD create flyuser team successed. ')
            flag_fsd = 1

        elif "已经创建团队的老板不能再创建团队" in res['info']:
            flag_fsd=2
            print('Failed: 已经创建团队的老板不能再创建团队. ')
        else:
            print('Failed: FSD create flyuser team  failed')
            flag_fsd = 0

        return flag_fsd

        
     #------------FSD add operate car api ------------------------------------------
    def fsd_add_operate_car(self,ids,token,data):
        userdata=data
        userdata['memberId']=ids
  
        ids=str(ids)
      
        request_url = api.API_URL['addoperatecar'].replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        if ret==1:
            print('Passed: add operate car successed. ')
            flag_fsd = 1
        else:
            print('Failed: add operate car  failed')
            flag_fsd = 0

        return flag_fsd


    #------------FSD add plane api ------------------------------------------
    def fsd_add_plane(self,phone,ids,token,data):
        userdata=data
        userdata['memberId']=ids
        userdata['phone']=phone
          
        ids=str(ids)
        phone=str(phone)
        print(phone)
      
        request_url = api.API_URL['addplane'].replace("PHONE",phone).replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        if res['info']=='操作成功':
            print('Passed: add plane successed. ')
            flag_fsd = 1
        else:
            print('Failed: add plane  failed')
            flag_fsd = 0

        return flag_fsd


    
     #------------FSD get plane id------------------------------------------
    def fsd_get_plane_id(self,ids,token,phone):
        userdata={}
        userdata['memberId']=ids
        userdata['from']='3'
        userdata['reserveId']=''
          
        ids=str(ids)
        phone=str(phone)
      
        request_url = api.API_URL['getplaneid'].replace("PHONE",phone).replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        if '操作成功' in res['info']:
            print('Passed: fsd get plane id successed. ')
            planeid=res['datas']["toolList"][0]['toolId']
            print('Get the planeid %s'%planeid)
            flag_fsd = 1
            return flag_fsd,planeid
        else:
            print('Failed: fsd get plane id  failed')
            flag_fsd = 0
            return flag_fsd


    
     #------------FSD update  Xy------------------------------------------
    def fsd_update_Xy(self,ids,token,phone):
        userdata={}
        x="116.483189"
        y="39.997527"
          
        ids=str(ids)
        phone=str(phone)
      
        request_url = api.API_URL['updatexy'].replace("XVALUE",x).replace("YVALUE",y).replace("PHONE",phone).replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        if '操作成功' in res['info']:
            print('Passed: update xy successed. ')
            flag_fsd = 1
            return flag_fsd
        else:
            print('Failed: update xy failed')
            flag_fsd = 0
            return flag_fsd

     #------------FSD get car id------------------------------------------
    def fsd_get_car_id(self,ids,token,phone):
        userdata={}
          
        ids=str(ids)
        phone=str(phone)
      
        request_url = api.API_URL['getcarid'].replace("PHONE",phone).replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        if  res['errno']==0:
            print('Passed: fsd get car id successed. ')
            carid=res['data']['list'][0]['id']
            print('Get the car id %s'%carid)
            flag_fsd = 1
            return flag_fsd,carid
        else:
            print('Failed: fsd get car id  failed')
            flag_fsd = 0
            return flag_fsd

     #------------FSD get reserve calendar------------------------------------------
    def fsd_get_reserve_calendar(self,ids,token,phone,carid):
        userdata={}
        userdata['carId']=carid
        print(type(carid))
              
        ids=str(ids)
        phone=str(phone)
      
        request_url = api.API_URL['getreservecalendar'].replace("PHONE",phone).replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        if  res['errno']==0:
            print('Passed: get reserve calendar successed. ')
            times=res['data'][0]['time']
            print('Get the times %s'%times)
            flag_fsd = 1
            return flag_fsd,times
        else:
            print('Failed: get reserve calendar  failed')
            flag_fsd = 0
            return flag_fsd

        
     #------------FSD get reserve calendar------------------------------------------
    def query_crop_price(self,ids,token,phone,data,time):

        userdata=data
        userdata['times']="["+str(time)+"]"
        print(userdata)
                 
        ids=str(ids)
        phone=str(phone)

      
        request_url = api.API_URL['querycropprice'].replace("PHONE",phone).replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        if  res['errno']==0:
            print('Passed: query crop price successed. ')
            
            maxPrice=res['data'][0]['maxPrice']
            scmaxPrice= res['data'][0]['scMaxPrice']          
            minPrice=res['data'][0]['minPrice']  
            exceed=res['data'][0]['exceedScale']
            print('Get the maxPrice %s'%maxPrice)
            print('Get the scmaxPrice %s'%scmaxPrice)
            print('Get the minPrice %s'%minPrice)
            print('Get the exceed %s'%exceed)

            adviceprice=res['data'][0]['advicePrice']
            inputprice= res['data'][0]['inputPrice']          
            cropname=res['data'][0]['cropName']
            cropid=res['data'][0]['cropId']
            print('Get the adviceprice %s'%adviceprice)
            print('Get the inputprice %s'%inputprice)
            print('Get the minPrice %s'%cropname)
            print('Get the exceed %s'%cropid)

            data=res['data']
            returndata={}
            returndata['maxPrice']=maxPrice
            returndata['scmaxPrice']=scmaxPrice
            returndata['minPrice']=minPrice
            returndata['exceed']=exceed
            returndata['adviceprice']=adviceprice
            returndata['inputprice']=inputprice
            returndata['cropname']=cropname
            returndata['cropid']=cropid            
            
            flag_fsd = 1
            return flag_fsd,returndata
        else:
            print('Failed: query crop price  failed')
            flag_fsd = 0
            return flag_fsd



     #------------FSD add reserve order------------------------------------------
    def fsd_add_reserve_order(self,ids,token,phone,carid,planeid,price,time,data):
 
        userdata=data

        #regionPrices[0]['inputPrice']=price
        '''      
        userdata['regionPrices']=regionPrices
        userdata['times']=time        

        '''
        userdata['carId']=carid
        userdata['planes']="["+planeid+"]"
        userdata['times']="["+str(time)+"]"
        userdata['regionPrices'][0]['inputPrice']=price
        userdata['regionPrices']=str(userdata['regionPrices'])
        print(userdata['regionPrices'])

             
        ids=str(ids)
        phone=str(phone)
      
        request_url = api.API_URL['addreserveorder'].replace("PHONE",phone).replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        if  res['errno']==0:
            print('Passed:add reserve order successed. ')
            orderid=res['data']
            print('Get the orderid %s'%orderid)
            flag_fsd = 1
            return flag_fsd,orderid
        else:
            print('Failed: add reserve order  failed')
            flag_fsd = 0
            return flag_fsd


  #------------FSD fly auth  ------------------------------------------
    def fsd_fly_auth(self,ids,token,phone,data):
        userdata=data
        userdata['phone']=phone        
   
        ids=str(ids)
        phone=str(phone)
      
        request_url = api.API_URL['flyauth'].replace("id",ids).replace("TOKEN",token)
        
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_FSD(res)     
        print(ret)

        if '操作成功' in res['info']:
            print('Passed: FSD auth successed. ')
            flag_fsd = 1
            return flag_fsd
        else:
            print('Failed: FSD auth failed')
            flag_fsd = 0
            return flag_fsd




     #------------sys query fly user auth ------------------------------------------
    def query_fly_auth(self,phone,userdata):

        userdata['phone']=phone
        request_url = api.API_URL['queryflyuser']
                
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_errorinfo_from_management(res)     
        print(ret)

        if err_flag==True:

            print('Passed:query flyuser successed.')          
            flag_status=1
            ids=res['data']['data'][0]['id']
            print('get the flyauth id ',ids)
            return flag_status,ids
                      
        else:
            print('Failed:query flyuser failed')
            flag_status = 0
            return flag_status
        

     #------------ sys fly user auth 实名认证------------------------------------------
    def sys_fly_user_auth(self,ids,userdata,headers):

        userdata['id']=str(ids)
        request_url = api.API_URL['sysflyuserauth']
               
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata,headers)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)

        if 'info' in res:
            if "SUCCESS" in res['info']:
                print('Passed:sys flyuser auth successed.')          
                flag_status=1
                return flag_status
            elif "此飞手已审核" in res['info']:
                print('Failed :sys flyuser auth failed.')          
                flag_status=2
                return flag_status
        else:
            print('Failed:sys flyuser auth failed.')
            flag_status = 0
            return flag_status  

     #------------ sys fly  auth 飞手认证------------------------------------------
    def sys_fly_auth(self,flyUserId,userdata,headers):

        userdata['flyUserId']=str(flyUserId)
        request_url = api.API_URL['sysflyauth']
               
        print('Test data and api url |',userdata,'| ',request_url)

        # 发送post请求
        my_request = MyRequest(request_url,userdata,headers)
        res = my_request.request_post()
        
        res=res.json()
        print("response: ",res)

        #解析response返回信息
        err_flag,ret=my_request.decode_res_info(res)     
        #print(ret)

        if err_flag==True:
            if "SUCCESS" in res:
                print('Passed:sys fly auth successed.')          
                flag_status=1
                return flag_status
           
            print('Passed:sys fly auth successed.')          
            flag_status=1
            return flag_status

        elif  "此飞手已审核" in res['info']:
                print('Failed :sys fly auth failed.')          
                flag_status=2
                return flag_status              
        else:
            print('Failed:sys fly auth failed')
            flag_status = 0
            return flag_status
        
    



        

    #此函数不用了
    #------------ login take token-------------------------------------------
    #解析返回值
    def take_token_from_Login(self,res,item_name):
        #print(res)
        jsDumps_res=json.dumps(res)

        res=jsDumps_res
        itemlist = []
        itemlist = res.split(',')
        strname=item_name
        
        #print(strname)        
        templist = []
        
        item=''
        for i in range(0,len(itemlist)):
            if strname in itemlist[i]:
                templist=itemlist[i].split(':')
                item_temp = templist[1]
            
                item = item_temp.strip('\"}')
                item = item_temp.strip(' ')
                #print(type(item))
                #print(item)
                break
        print('Get the %s '%item_name,item)

        return item               
  


if __name__ == "__main__" :

    my_obj = FSDLogin()
    '''
    data2= {
            'phone':'19900001001',
            "password":"123qwe",
    }
    my_obj.fsd_api_login(data2)
 
    data3 = {
        "userName":"lirunhua",
        "passWord":"12345",
    }
    #my_obj.system_management_login(data3)
    data4 = {
        "id":'2803',
        "state":'3',
    }
    my_obj.sysment_management_freeze_flyuser(data4)
    '''

    item="\"FARMFRIEND_TOKEN\":"
    res={'errno': 0, 'data': {'FARMFRIEND_TOKEN': 'eyJ1aWQiOiI3NSIsInRva2VuIjoiYTNjNTJhYzEtYjVkMS00Yjc3LTk5MTQtMDZhZjNkYzM2N2ZlIn0=', 'FARMFRIEND_LT': '1524507681800'}}
    

