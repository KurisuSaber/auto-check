import requests
import time
info = {
    "统一认证登录用户名":{
        "password":"统一认证登录密码","name":"真实姓名","number":"学号"
    }
}
url1 = "https://app.buaa.edu.cn/uc/wap/login/check"
url2 = "https://app.buaa.edu.cn/buaaxsncov/wap/default/save"
flag = True
for u,p in info.items():
    print(u)
    data1 = {"username":u,"password":p["password"]}
    res1 = requests.post(url=url1,data=data1)
    cookie = res1.cookies
    print(res1.text)
    data2 = {
        "sfzs":"1",
        "brsfzc":"1",
        "bzxyy": "",
        "bzxyy_other": "",
        "tw":"",
        "sfcxzz":"",
        "zdjg":"",
        "zdjg_other":"",
        "sfgl":"",
        "gldd":"",
        "gldd_other":"",
        "glyy":"",
        "glyy_other":"",
        "gl_start":"",
        "gl_end":"",
        "sfmqjc":"",
        "sfzc_14":"1",
        "sfqw_14":"",
        "sfqw_14_remark":"",
        "sfzgfx":"",
        "sfzgfx_remark":"",
        "sfjc_14":"",
        "sfjc_14_remark":"",
        "sfjcqz_14":"",
        "sfjcqz_14_remark":"",
        "sfgtjz_14":"",
        "sfgtjz_14_remark":"",
        "szsqqz":"",
        "sfyqk":"",
        "szdd":"1",
        "area":"北京市 海淀区",
        "city":"北京市",
        "province":"北京市",
        "address":"北京市海淀区花园路街道北京航空航天大学北京航空航天大学学院路校区",
        "geo_api_info":"{\"type\":\"complete\",\"info\":\"SUCCESS\",\"status\":1,\"$DA\":\"jsonp_240934_\",\"position\":{\"Q\":39.98138,\"R\":116.34541000000002,\"lng\":116.34541,\"lat\":39.98138},\"message\":\"Get ipLocation success.Get address success.\",\"location_type\":\"ip\",\"accuracy\":null,\"isConverted\":true,\"addressComponent\":{\"citycode\":\"010\",\"adcode\":\"110108\",\"businessAreas\":[{\"name\":\"五道口\",\"id\":\"110108\",\"location\":{\"Q\":39.99118,\"R\":116.34157800000003,\"lng\":116.341578,\"lat\":39.99118}},{\"name\":\"大钟寺村\",\"id\":\"110108\",\"location\":{\"Q\":39.965569,\"R\":116.339877,\"lng\":116.339877,\"lat\":39.965569}}],\"neighborhoodType\":\"生活服务;生活服务场所;生活服务场所\",\"neighborhood\":\"北京航空航天大学\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"学院路\",\"streetNumber\":\"43号\",\"country\":\"中国\",\"province\":\"北京市\",\"city\":\"\",\"district\":\"海淀区\",\"township\":\"花园路街道\"},\"formattedAddress\":\"北京市海淀区花园路街道北京航空航天大学北京航空航天大学学院路校区\",\"roads\":[],\"crosses\":[],\"pois\":[]}",
        "is_move":"0",
        "move_reason":"",
        "move_remark":"",
        "realname":p["name"],
        "number":p["number"]
    }
    res2 = requests.post(url=url2,data=data2,cookies=cookie)
    print(res2.text)