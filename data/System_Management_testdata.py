# -*- coding:utf8 -*-

# ------------------------------ case: system management account----------------------
testdata_system_login_userdata_001 = {
        "userName":"lirunhua",
        "passWord":"123456",
}

testdata_system_login_userdata_002 = {
        "userName":"lirunhua",
        "passWord":"12345",
}

# ------------------------------ case: city management account----------------------
testdata_001_city_account_001 = {
        "userName":"lirunhua",
        "passWord":"123456",
}

# ------------------------------ case: add salesman----------------------
testdata_001_add_salesman_001 = {
        "email":"test@farmfriend.cn",
        "department":"10",
        "managerId":"72",
        "address":"江苏省徐州市鼓楼区黄楼街道华联社区",
}

# ------------------------------ case: system query fly user----------------------
testdata_001_system_query_flyuser_001 = {
        "phone":"14200010006",
}


# ------------------------------ case: system freez flyuser----------------------
testdata_system_freeze_flyuser = {
        "id":"2785",
        "state":"3",
}

# ------------------------------ case: system freez flyuser state----------------------
testdata_system_freez_flyuser_auth = {
        "flyAuthState":"3",
}

#---------------------------------sys query auth----------------------------------------
testdata_sys_query_auth_001={
        "phone":"14923607195",
        "liableName":"",
        "teamName":"",
        "address":"",
        "roleId":"-1",
        "label":"-1",
        "authState":"-1",
        "isBlacklist":"2",
        "state":"-1",
        "flyAuthState":"",
        "page":"1",
        "rows":"30",
        "sort":"",
        "order":"",
}
#---------------------------sys user auth---------------------------------------------
testdata_fly_user_auth_001={
        "id":"2651",
        "authState":"3",
        "check":"true",
        "noPassReason":"",
}
#------------------------sys fly auth---------------------------------------------
testdata_fly_auth_001={
        "flyUserId":"2651",
        "flyAuthState":3,
        "noPassReason":"",
}
