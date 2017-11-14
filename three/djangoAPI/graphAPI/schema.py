import graphene
#--------- 新增以下
from collections import namedtuple 
from .schemaClass.playDataSchema import playDataSchema 
from api.api.playData import playData
#---------

class Query(graphene.ObjectType):
    reverse = graphene.String(word=graphene.String(default_value='t'))

    def resolve_reverse(self, info, word):
        print(self)
        return 'hello'

#--------- 新增以下 ------------------------
    playData = graphene.List(playDataSchema, name = graphene.String())

    def resolve_playData(self, info, name):
        data = playData( {'name': name} )['data']
        if len(data) > 0:
            # --- 轉成 namedtuple ---
            outDataNT = namedtuple('myData', [ key for key in data[0] ])
            outData = [ outDataNT(**eachData) for eachData in data ]
            # ----------------------
            return outData
        else: 
            return []
#-------------------------------------------


schema = graphene.Schema(query=Query)