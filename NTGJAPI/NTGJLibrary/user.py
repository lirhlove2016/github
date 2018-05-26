#-*- coding: utf-8 -*-
'''
    created by xietingmei 2018-02-22
'''
__version__='0.1'

import string
import urllib2
import urllib
import cookielib
import json
import sys
from basiclib import *
import pysical_devices as device
import api_url as api
import time
import datetime
import random
reload(sys) 
sys.setdefaultencoding('utf8')

class FSDLogin(object):


    #----------------------------------------------------------------------------------------FSD user register
    def fsd_register(self,phone):
        '''
            FSD register。

            参数:
          
            举例:
            | FSD register |
        '''
        # 配置FSD信息

        json_content = '' 
        json_data = ['''phone=''']
        json_data.append(phone)
        json_content += ''.join(json_data)
        
        url_string = api.ADMIN_API['fsdregister']
        
        # 发送request到NTGJAPI
        my_request = NTGJRequest(url_string,json_content)
        res = my_request.request_post()
        print "response",res

        tokenlist = []
        tokenlist = res.split(',')
        strname = "\"token\":"
        templist = []
        accesstoken=''
        for i in range(0,len(tokenlist)):
               if strname in tokenlist[i]:
                    templist=tokenlist[i].split(':')
                    accesstoken1 = templist[1]
                    accesstoken = accesstoken1.strip('\"}')
                    break
        print 'Get the accesstoken',accesstoken

        idlist = []
        idlist = res.split(',')
        strname = "\"userId\":"
        templist = []
        ids=''
        for i in range(0,len(idlist)):
            if strname in idlist[i]:
                templist=idlist[i].split(':')
                ids1 = templist[1]
                ids = ids1.strip('\"}')
                break
        print 'Get the id',ids
         
        if '操作成功' in res:
            print 'Passed:FSD user register successed';
            flag_ret = 1
            return flag_ret,accesstoken,ids
        else:
            print 'Failed:FSD user register failed';
            flag_ret = 0
            return flag_ret


    #---------------------------------------------------------------------------------------- fly user set password
    def flyuser_set_password(self,accesstoken,ids,phone):
        '''
            flyuser set password 。

            参数:
          
            举例:
            |flyuser set password |
        '''
        # 配置信息

        json_content = '' 
        json_data = ['''userId=''']
        json_data.append(ids)
        json_data.append('''&password=''')
        json_data.append('''123qwe''')
        json_data.append('''&token=''')
        json_data.append(accesstoken)
        json_data.append('''&phone=''')
        json_data.append(phone)
        json_content += ''.join(json_data)
        
        url_string = api.ADMIN_API['fsduserpassword']


        # 发送request到NTGJAPI
        my_request = NTGJRequest(url_string,json_content)
        res = my_request.request_post()
        print "response",res

        # 解析response返回信息

        if '操作成功' in res:
            print 'Passed: flyuser set password successed';
            flag_ret = 1
            return flag_ret
        else:
            print 'Failed:flyuser set password failed';
            flag_ret = 0
            return flag_ret

    #----------------------------------------------------------------------------------------ramdom phone number
    def ramdom_phone_number(self):
        '''
            Ramdom phone number。

            参数:
          
            举例:
            | Ramdom phone numbe |
        '''
        # 配置FSD信息
        num_start = ['142','143','141','144','140']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits,8))
        res = start+end
        return res

    #----------------------------------------------------------------------------------------management login Api
    def management_login(self,**confdict):
        '''
            management login  登陆。

            参数:
          
            举例:
            | management login |
        '''
        # 配置信息

        json_content = '' 
        json_data = ['''userName=''']
        json_data.append(confdict['userName'])
        json_data.append('''&passWord=''')
        json_data.append(confdict['passWord'])
        json_content += ''.join(json_data)

        url_string = api.ADMIN_API['syslogin']

        
        # 发送request到NTGJAPI
        my_request = NTGJRequest(url_string,json_content)
        res = my_request.request_post()
        print "response",res

        # 解析response返回信息

        if 'FARMFRIEND_TOKEN' in res:
            print 'Passed:sys login successed';
            flag_ret = 1
            return flag_ret
        else:
            print 'Failed:sys login failed';
            flag_ret = 0
            return flag_ret


    #----------------------------------------------------------------------------------------Freeze fly account
    def freeze_fly_account(self,ids):
        '''
            freeze fly account 。

            参数:
          
            举例:
            |freeze fly account  |
        '''
        # 配置信息

        json_content = '' 
        json_data = ['''id=''']
        json_data.append(ids)
        json_data.append('''&state=3''')
        json_content += ''.join(json_data)
        url_string = api.ADMIN_API['freezeflyaccount']

        
        # 发送request到NTGJAPI
        my_request = NTGJRequest(url_string,json_content)
        res = my_request.request_post()
        print "response",res

        # 解析response返回信息

        if 'SUCCESS' in res:
            print 'Passed: freeze fly account successed';
            flag_ret = 1
            return flag_ret
        else:
            print 'Failed:freeze fly account failed';
            flag_ret = 0
            return flag_ret
    

    #----------------------------------------------------------------------------------------add tools
    def add_tools(self,ids,accesstoken):
        '''
            add tools 。

            参数:
          
            举例:
            |add tools |
        '''
        # 配置信息

        json_content = '' 
        json_data = ['''factory=''']
        json_data.append('''&flowMeterId=&internalSerialNumber=&memberId=''')
        json_data.append(ids)
        json_data.append('''&model=&note=&planeSn=&toolFile=''')
        json_data.append('''http://farmlandbucketstest.oss-cn-beijing.aliyuncs.com/B9F72FD1753A47C3B3C13EE7F239C186''')
        json_data.append('''&toolModel=''')
        json_data.append('''大疆 MG-1''')
        json_data.append('''&userName=测试''')
        json_data.append('''&workAssistId=18''')
        json_content += ''.join(json_data)
        
        url_string = api.ADMIN_API['addtools'].replace("id",ids).replace("TOKEN",accesstoken)


        # 发送request到NTGJAPI
        my_request = NTGJRequest(url_string,json_content)
        res = my_request.request_post()
        print "response",res

        # 解析response返回信息

        if '操作成功' in res:
            print 'Passed: add tools successed';
            flag_ret = 1
            return flag_ret
        else:
            print 'Failed: add tools  failed';
            flag_ret = 0
            return flag_ret


#----------------------------------------------------------------------------------------FSD login Api
    def fsd_api_login(self,phone,**confdict):
        '''
            FSD login  登陆。

            参数:
          
            举例:
            | FSD login |
        '''
        # 配置信息

        json_content = '' 
        json_data = ['''phone=''']
        json_data.append(phone)
        json_data.append('''&password=''')
        json_data.append(confdict['password'])
        json_data.append('''&InviteCode=''')
        json_content += ''.join(json_data)

        url_string = api.ADMIN_API['fsdlogin']

        
        # 发送request到NTGJAPI
        my_request = NTGJRequest(url_string,json_content)
        res = my_request.request_post()
        print "response",res

        tokenlist = []
        tokenlist = res.split(',')
        strname = "\"token\":"
        templist = []
        accesstoken=''
        for i in range(0,len(tokenlist)):
               if strname in tokenlist[i]:
                    templist=tokenlist[i].split(':')
                    accesstoken1 = templist[1]
                    accesstoken = accesstoken1.strip('\"}')
                    break
        print 'Get the accesstoken',accesstoken

        idlist = []
        idlist = res.split(',')
        strname = "\"userId\":"
        templist = []
        ids=''
        for i in range(0,len(idlist)):
            if strname in idlist[i]:
                templist=idlist[i].split(':')
                ids1 = templist[1]
                ids = ids1.strip('\"}')
                break
        print 'Get the id',ids
        # 解析response返回信息

        if 'token' in res:
            print 'Passed:FSD login successed';
            flag_ret = 1
            return flag_ret,accesstoken,ids
        elif '密码不正确' in res:
            print 'Passed:FSD login error password';
            flag_ret = 2
            return flag_ret
        elif '账户已冻结' in res:
            print 'Passed:Freeze fly account can not login';
            flag_ret = 3
            return flag_ret
        else:
            print 'Failed:FSD login failed';
            flag_ret = 0
            return flag_ret

#----------------------------------------------------------------------------------------FSD checkaccount
    def fsd_check_account(self,**confdict):
        '''
            FSD check account  检查账号是否存在。

            参数:
          
            举例:
            | FSD check account |
        '''
        # 配置信息

        json_content = '' 
        json_data = ['''account=''']
        json_data.append(confdict['account'])
        json_data.append('''&acc_type=0&appid=1''')
        json_content += ''.join(json_data)

        url_string = api.ADMIN_API['fsdcheckaccount']

        
        # 发送request到NTGJAPI
        my_request = NTGJRequest(url_string,json_content)
        res = my_request.request_post()
        print "response",res

        # 解析response返回信息

        if 'user not exist' in res:
            print 'Passed:FSD account not exist';
            flag_ret = 1
            return flag_ret
        else:
            print 'Failed:FSD account exist';
            flag_ret = 0
            return flag_ret


if __name__ == "__main__" :
    my_obj = FSDLogin()
