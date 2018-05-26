# -*- coding:utf8 -*-

# ------------------------------ case: fsd account----------------------

testdata_FSD_login_userdata_001= {
            'phone':'19900001001',
            "password":"123qwe",
    }
# ------------------------------ case: fsd account----------------------
testdata_FSD_login_phonenumber_error= {
            'phone':'1990000112@',
            "password":"123qw",
    }
# ------------------------------ case: fsd account----------------------
testdata_FSD_login_password_error= {
            'phone':'19900001001',
            "password":"123qw",
    }
# ------------------------------ case: fsd account----------------------
testdata_FSD_login_only_phone= {
            'phone':'19900001001',
    }
 # ------------------------------ case: fsd account----------------------   
testdata_FSD_login_only_password= {
            "password":"123qw",
    }
# ------------------------------ case: fsd account----------------------
testdata_FSD_login_only_password= {
            "password":"123qw",
    }
# ------------------------------ case: fsd account----------------------
testdata_FSD_login_null= {
    }

 #------------------------------ case: fsd freez account----------------------
testdata_FSD_login_userdata_002= {
            'phone':'14430036005',
            "password":"123qwe",
    }
# ------------------------------ case: fsd  set passworda---------------------

testdata_FSD_setpassword_phone='19900001001'
testdata_FSD_setpasswords_password='123qwe'
# ------------------------------ case: fsd  check---------------------

testdata_FSD_check_data_001={
            'account':'19933331001',
            'acc_type':'0',
            'appid':'1',}



# ------------------------------ case: fsd  add tools---------------------
testdata_FSD_login_userdata_003={
            'phone':'14110428596',
            "password":"t123456",   
}



testdata_flyuser_add_tools_002={"factory":"",
        "flowMeterId":"",
        "internalSerialNumber":"",
        "memberId":"2228",
        "model":"",
        "note":"",
        "planeSn":"",
        "toolFile":"http://farmlandbucketstest.oss-cn-beijing.aliyuncs.com/B9F72FD1753A47C3B3C13EE7F239C186",
        "toolModel":"大疆 MG-1",
        "userName":"测试",
        "workAssistId":"18",
}

# ------------------------------ case: fsd  add operate car---------------------
testdata_FSD_add_operate_car_001= {
            'carName':'jing1223428',
            #"memberId":"2817",
    }

testdata_FSD_add_operate_car_userdata_001={
            'phone':'14433334003',
            "password":"123qwe",   
} 


# ------------------------------ case: fsd  add plane-------------------
testdata_flyuser_add_plane_001={
            'phone':'14110428596',
            "password":"123qwe",
            "toolModel":"大疆 MG-1",
            "username":"测试",
            "memberId":"2817",
            "flowMeterId":"",
            "planSn":"MG7135",
            "internalSerialNumber":"1234",
            "workAssistId":"18",
            "note":"test",
            "toolFile":"http://farmlandbucketstest.oss-cn-beijing.aliyuncs.com/B9F72FD1753A47C3B3C13EE7F239C186",  
    
}
# ------------------------------ case: fsd  create flyuser team-------------------
testdata_FSD_flyuser_not_team_001={
            'phone':'14433334003',
            "password":"123qwe",   
}
testdata_FSD_flyuser_not_team_002={
            'phone':'14433334003',
            "password":"123qwe",   
}
testdata_FSD_flyuser_not_team_003={
            'phone':'14430032001',
            "password":"123qwe",   
}


testdata_create_flyuser_team_001={
            "teamName":"flyuser",
            "userType":1,
            "positionCountyId":"北京市辖区东城区",
            "province":"北京市",
            "provinceCode":"110000",
            "cityCode":"110100",
            "city":"市辖区",
            "countyCode":"110101",
            "county":"东城区",
            "detailedAddress":"test",
            "planeTotalNumber":"1",
            "carTotalNumber":"1",
            "maxWork":"2147483647",
            "historyHomeworkArea":"21474836",
            "planePicturesUrl":"planePicturesUrl",
            "liableIdentityUrl1":"http://farmlandbucketstest.oss-cn-beijing.aliyuncs.com/6640255c85884f108bf9aa6d58293a6",
            "planePicturesUrl":"http://farmlandbucketstest.oss-cn-beijing.aliyuncs.com/817c9254593b4233b909d8ad4e4911ac",
            "businessLicense":"23568",
            "businessLicenseUrl":"http://farmlandbucketstest.oss-cn-beijing.aliyuncs.com/892d0aa6a538478c8112b8b84efbd385",
            "businessLicense":"23568",
}           

# ------------------------------ case: fsd   flyuser  auth--------------
#未认证
testdata_FSD_flyuser_auth_001={
            'phone':'14433332001',
            "password":"123qwe",   
}
testdata_FSD_flyuser_auth_002={
            'phone':'14422221006',
            "password":"123qwe",   
}
testdata_FSD_flyuser_auth_002={
            'phone':'14433334002',
            "password":"123qwe",   
}

#---------------------------fly auth----------------------------------------------
testdata_FSD_ahth={
            "phone":"14923607195",
            "liableName":"autotest",
            "liableIdentity":"33070220071027641X",
            "liableIdentityFile":"http://farmlandbucketstest.oss-cn-beijing.aliyuncs.com/e306ad21701a46fc93f4d2f927e39bac",
            "liableIdentityUrl1":"http://farmlandbucketstest.oss-cn-beijing.aliyuncs.com/6640255c85884f108bf9aa6d58293a68",
            "detaileAddress":"test",
            "province":"北京市",
            "provinceCode":"110000",
            "city":"市辖区",
            "cityCode":"110100",
            "county":"东城区",
            "countyCode":"110101",
            "carTotalType":"0",
            "plane":"0",
            "flyAuthType":1,
            "aptitudePics":"http://farmlandbucketstest.oss-cn-beijing.aliyuncs.com/817c9254593b4233b909d8ad4e4911ac",
            "referrerName":"",
            "referrerPhone":"",
}

#-------------------------------------------------------------------------
regions=[{"province":"北京市","provinceCode":110000,"city":"北京市","cityCode":110100}]

#----------------------------------------------------------------------------
testdat_queryCropPrice_data={
			"times":"[1525881600]",
			"regions":'[{"province":"北京市","provinceCode":110000,"city":"北京市","cityCode":110100}]',

}
#----------------------------------------------------------------------------
testdata_addreserveOrder={
			"times":"[1525881600]",
			"carid":899,
			"planes":"[2124]",
			"regions":'[{"province":"北京市","provinceCode":110000,"city":"北京市","cityCode":110100}]',
			"regionPrices":[{"province":"北京市","provinceCode":110000,"city":"市辖区","cityCode":110100,"maxPrice":12.6,"scMaxPrice":0,"minPrice":4,"exceedScale":90,"advicePrice":0,"inputPrice":4.6,"cropName":"中稻","cropId":2}],
			

}