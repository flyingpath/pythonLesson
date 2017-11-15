import graphene
from api.api.writePlayData import writePlayData as writePlayDataFunc

class writePlayData(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        lv = graphene.Int()
        skill = graphene.String()
    
    status = graphene.Boolean()
    err = graphene.String()

    def mutate(self, info, name, lv, skill):
        data = writePlayDataFunc( { 
            'name': name,
            'lv': lv, 
            'skill': skill
        } )

        status = data['status']
        err = data['err']
        return writePlayData(status=status, err=err)

# #query{
#   playData(name: "Charmander") {
#     LV
#     SKILL
#   }
# }