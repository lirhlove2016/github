# -*- coding:utf8 -*-

# ------------------------------ admin login url     ---------------------
API_URL = {
	"fsdlogin":"/flyHandApp/api/user/loginPassword",
    "fsdregister":"/flyHandApp/api/user/loginTest",
    "fsdusersetpassword":"/flyHandApp/api/user/loginAdd",
    "fsdcheckaccount":"/flyHandApp/api/user/checkAccountRegisted",
    "fsdsms":"/flyHandApp/api/user/getSmsCheckCode?phone=test",
    "addtools":"/flyHandApp/api/user/addTool/v1?userId=id&token=TOKEN",
    "syslogin":"/management/sys/login",
    "freezeflyaccount":"/management/user/updateFlyUserAccountState",
    "createflyuserteam":"/flyHandApp/api/team/createFlyUserTeam?userId=id&token=TOKEN",
    "addoperatecar":"/flyHandApp/api/reserve/addOperateCar?userId=id&token=TOKEN",
    "addplane":"/flyHandApp/api/user/addTool/v1?access_phone=PHONE&userId=id&token=TOKEN",
    "getplaneid":"/flyHandApp/api/user/oneToolList?access_phone=PHONE&userId=id&token=TOKEN",
    "updatexy":"/flyHandApp/api/user/updateXY?x=XVALUE&y=YVALUE&access_phone=PHONE&userId=id&token=TOKEN",
    "flyuserauth":"/flyHandApp/api/user/authInfoUpload/V1?userId=id&token=TOKEN",
    "getsmscheckcode":"/flyHandApp/api/user/getSmsCheckCode",
    "getcarid":"/flyHandApp/api/reserve/getOperateCarList?access_phone=PHONE&userId=id&token=TOKEN",
    "getclendar":"/flyHandApp/api/reserve/getReserveCalendar",
    "getreservecalendar":"/flyHandApp/api/reserve/getReserveCalendar?access_phone=PHONE&userId=id&token=TOKEN",
    "querycropprice":"/flyHandApp/api/reserve/queryCropPricing?access_phone=PHONE&userId=id&token=TOKEN",
    "sysflyauth":"/management/user/putFlyAuth",
    "addreserveorder":"/flyHandApp/api/reserve/addReserve?access_phone=PHONE&userId=id&token=TOKEN",
    "queryflyuser":"/management/user/queryFlyUserTeamList2",
    "sysflyuserauth":"/management/user/updateFlyUserAuthState", 
    "flyauth":"/flyHandApp/api/user/authInfoUpload/V1?userId=id&token=TOKEN",

    }

API_YWB_URL={
	"ywblogin":"/businessTreasure/api/user/loginP",
	"salesmanQuery":"/businessTreasure/api/user/salesmanQuery?access_phone=PHONE&userId=id&token=TOKEN",
	"cropsQuery":"/businessTreasure/api/tool/cropsAllQuery?access_phone=PHONE&userId=id&token=TOKEN",
	"queryFarmland":"/businessTreasure/api/farmland/queryFarmlandByUser?acc=ACC&access_phone=PHONE&userId=id&token=TOKEN",
	"getstartdate":"/weather/getWeatherInfo/getSubOrderWeatherInfo?access_phone=PHONE&userId=id&token=TOKEN",
	"addOrder":"/businessTreasure/api/order/addOrderQuery?access_phone=PHONE&userId=id&token=TOKEN",
	"orderDetaile":"/businessTreasure/api/order/orderDetailedQuery?access_phone=PHONE&userId=id&token=TOKEN",
	"getordercancel":"/businessTreasure/api/order/getOrderCancelReason?access_phone=PHONE&userId=id&token=TOKEN",
	"ywbcancelOrder":"/businessTreasure/api/order/cancelOrder?access_phone=PHONE&userId=id&token=TOKEN",
	"searchflowcount":"/flowcounter_web/flowcount/v3/search_order_number?access_phone=PHONE&userId=id&token=TOKEN",
	"wogetflytrack":"/flowcounter_web/flowcount/v1/getflytrack?access_phone=PHONE&userId=id&token=TOKEN",
	"ywbexit":"/businessTreasure/api/user/exit?access_phone=PHONE&userId=id&token=TOKEN",
	"setunregister":"/msgcenter/push/set_unregisterid?access_phone=PHONE&userId=id&token=TOKEN",

}





