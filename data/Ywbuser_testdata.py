# -*- coding:utf8 -*-

# ------------------------------ case: ywb account----------------------

testdata_YWB_login_userdata_001= {
            'phone':'18301212965',
            "passWord":"123qwe",
    }
# ------------------------------ case: ywbaccount----------------------
testdata_YWB_login_phonenumber_error= {
            'phone':'1990000112@',
            "passWord":"123qw",
    }

# ------------------------------ case: ywb account----------------------
testdata_YWB_salesmanquery_001= {
            'salesmanId':'s1520841050603Sbb9ed6f5-91f5-4989-b14b-3aeafd7031fc',
            "number":"0",
    }

# ------------------------------ case: ywb salesmans_accountId----------------------

testdata_YWB_salesmans_accountId_001= {
            "type":"0",
            'accountId':'809',
     
    }

testdata_YWB_salesmans_accountId_002= {
			"type":"1",
            'accountId':'p1523516849945S26f38a34-3f45-4d68-8138-addd91d0dbb2',     

    }

testdata_YWB_salesmans_accountId_003= {
            "type":"3",
            'accountId':'big1523516703430S8437f197-5bc5-4184-a4ea-4314dc8f6b5e',         
    }


# ------------------------------ case: ywb account----------------------
testdata_YWB_queryfarmland_001= {
            'accountId':'s1520841050603Sbb9ed6f5-91f5-4989-b14b-3aeafd7031fc',
            "fly_user_type":"0",
            'acc':'s1520841050603Sbb9ed6f5-91f5-4989-b14b-3aeafd7031fc'
    }


# ------------------------------ case: ywb account----------------------
testdata_YWB_add_Order_all_001= {
            'data':'{"accountId":"p1523516849945S26f38a34-3f45-4d68-8138-addd91d0dbb2",\
            "address":"北京市市辖区朝阳区朝阳sohu","area":"31.0","b_dosage":"","city":"市辖区",\
            "cityCode":"110100","county":"朝阳区","countyCode":"110105","cropId":"2",\
            "crops_highly":"1.5米及其以下","crops_name":"中稻","customer":"3",\
            "detailsAddress":"融科橄榄城三期融科橄榄城3期","drugType":"0","farmlandArea":"31.0",\
            "farmlands":"F1524911621737","formalType":"1","guideName":"li_test001",\
            "guidePhone":"18301212965","invoice":"2","latitude":"39.9972042753153",\
            "longitude":"116.48347077990067","assembledAddress":"北京市北京市朝阳区朝阳区",\
            "medicineService":"0","assembledAddressLatitude":"39.92147",\
            "assembledAddressLongitude":"116.443108","days":"2",\
            "sprayingTimeStamp":"1526486400","medicineUrl":"","name":"李合伙",\
            "orderNote":"正式","orderType":"1","order_money":"310","phone":"18301212965",\
            "province":"北京市","provinceCode":"110000","salesmanId":"s1520841050603Sbb9ed6f5-91f5-4989-b14b-3aeafd7031fc",\
            "spraying_time":"2018-05-20  至2018-05-21 ","teleAddress":"北京市朝阳区望京街道融科橄榄城三期融科橄榄城3期","transitionsNumber":"0",\
            "type":"1","unit_price":"10.0","userType":"1","weatherId":"0bc40a57-f595-4692-8cac-40a3de9bafae"}',
	}

testdata_YWB_add_Order_headers= {
			"User-Agent":"okhttp/3.4.2",
			"Content-Type":"multipart/form-data;boundary=bb28cb31-7eff-4e4e-8fc9-041f4bd7f732",
			"Accept-Encoding":"gzip",
			"Connection":"Keep-Alive",
	}

#---------------------------------------------
#正式订单
testdata_YWB_formal={"formalType":"1"}
#演示订单
testdata_YWB_formal={"formalType":"2"}
#测试订单
testdata_YWB_formal={"formalType":"3"}
