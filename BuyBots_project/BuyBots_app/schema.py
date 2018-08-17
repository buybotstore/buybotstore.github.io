from graphene_django import DjangoObjectType
import graphene
from .models import *

from graphene_django import DjangoObjectType
import graphene


class Bots(DjangoObjectType):
    class Meta:
        model = Bot


class Developers(DjangoObjectType):
    class Meta:
        model = Developer


class Query(graphene.ObjectType):
    bots = graphene.List(Bots)
    developers = graphene.List(Developers)

    def resolve_bots(self, info):
        return Bot.objects.all()

    def resolve_developers(self, info):
        return Developer.objects.all()


schema = graphene.Schema(query=Query)
