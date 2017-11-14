import graphene

class playDataSchema(graphene.ObjectType):
    ID = graphene.Int()
    NAME = graphene.String()
    LV = graphene.Int()
    SKILL = graphene.String()