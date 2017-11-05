from django.shortcuts import render
from django.http import HttpResponse
import re, json

from . import apiList as apiList 

def empty(request):
    return HttpResponse("You need to give me an api name")

def index(request):
#     resStr = """
# request.path: {}
# request.body: {}
# request.content_type: {}
# request.method: {}
# request.META.HTTP_HOST: {}
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
    
    # #-------------------------------------
    # # deal with GET
    
    # preRe= re.compile('^/api/')
    # applicationPath = preRe.sub('', request.path)
    # print(applicationPath)
    
    # if request.method == 'GET':
    #     parameterGET = dict(request.GET)
    #     # http://localhost:8000/api/index?aaa=b;hhh=t
    #     # {'aaa': ['b'], 'hhh': ['t']}
    #     data = ''
    #     try:
    #         data = getattr(apiList, applicationPath)(parameterGET)
    #         if data['status']:
    #             data = json.dumps(data['data'])
    #         else:
    #             data = data['err']
    #     except:
    #         data = '沒有這支 api'

    # rtnRes.write(data)
    return rtnRes
