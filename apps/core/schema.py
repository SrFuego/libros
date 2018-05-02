# Python imports


# Django imports


# Third party apps imports
import graphene


# Local imports
from ..books.schemas import PdfQuery


# Create your schemas here.
class Query(PdfQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
