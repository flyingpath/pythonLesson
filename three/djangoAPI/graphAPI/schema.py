import graphene
from collections import namedtuple 

from .schemaClass.playDataSchema import playDataSchema 
#---- 新增以下 ----------------------
from .mutations.writePlayData import writePlayData as writePlayDataMutation
#-----------------------------------

from api.api.playData import playData
from api.api.writePlayData import writePlayData

class Query(graphene.ObjectType):
    reverse = graphene.String(word=graphene.String(default_value='t'))

    def resolve_reverse(self, info, word):
        print(self)
        return 'hello'

    playData = graphene.List(playDataSchema, name = graphene.String())
    # playData = graphene.NonNull(playDataSchema, name = graphene.String())

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

#---- 新增以下 ----------------------

class Mutation(graphene.ObjectType):
    writePlayData = writePlayDataMutation.Field()
    def resolve_writePlayData(self, info):
        return writePlayDataMutation
        
#------------------------------------
schema = graphene.Schema(query=Query, mutation=Mutation)