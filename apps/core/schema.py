# Python imports


# Django imports


# Third party apps imports
import graphene


# Local imports
from ..books.queries import CourseQuery, EditorialQuery, KindQuery, PdfQuery


# Create your schemas here.
class Query(
        CourseQuery, EditorialQuery, KindQuery, PdfQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
