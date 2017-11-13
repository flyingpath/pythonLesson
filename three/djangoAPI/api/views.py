from django.shortcuts import render
from django.http import HttpResponse
import re, json

from . import apiList as apiList 

def indexGET(request):
#     resStr = """
# request.path: {}
# request.body: {}
# request.content_type: {}
# request.method: {}
# request.META['HTTP_HOST']: {}
# """.format(
#     request.path, 
#     request.body, 
#     request.content_type, 
#     request.method, 
#     request.META['HTTP_HOST']
#     )
    
    rtnRes = HttpResponse()

    # #------------------------------------
    # # force status
    # rtnRes.__init__(status= 405)
    
    # #-------------------------------------
    # # write header
    # rtnRes.__setitem__('memo', 'Go home kid')
    
    #-------------------------------------
    # deal with GET
    if request.method == 'GET':
        # 刪掉網址中的 /api/
        preRe= re.compile('^/api/')
        apiName = preRe.sub('', request.path)
#playData
        parameterGET = dict(request.GET)
        # http://localhost:8000/api/index?aaa=b;hhh=t
        # {'aaa': ['b'], 'hhh': ['t']}
        for eachP in parameterGET:
            if len(parameterGET[eachP])==1:
                parameterGET[eachP] = parameterGET[eachP][0]

        data = ''
        try:
            data = getattr(apiList, apiName)(parameterGET)
            if data['status']:
                data = json.dumps(data['data'])
            else:
                data = data['err']
        except:
            data = '沒有這支 api'
        # http://localhost:8000/api/playData?name=Charmander
    else:
        data='你只能用GET'
    rtnRes.write(data)
    return rtnRes

def indexPOST(request):
    rtnRes = HttpResponse()
    # #-------------------------------------
    # # deal with POST NEED TO DISABLE CSRF
    if request.method == 'POST':
        if request.content_type == 'application/json':
            parameterPOST =  json.loads( str(request.body, encoding='utf8') )
            try:
                apiName = parameterPOST['api']
                data = getattr(apiList, apiName)(parameterPOST)
            except:
                data = "api 為必要欄位"
    else:
        data = "如用 GET 請加上 api 名稱"

    rtnRes.write(data)
    return rtnRes

# {
# 	"api": "playData",
# 	"name": "Charmander"
# }