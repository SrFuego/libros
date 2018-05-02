# Python imports


# Django imports


# Third party apps imports
import graphene
from graphene_django.debug import DjangoDebug


# Local imports
from ..books.schemas import BookQuery


# Create your schemas here.
class Query(BookQuery, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query)
