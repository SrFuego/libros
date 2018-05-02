# apps/books/schemas.py
# Python imports
import graphene

# Django imports

# Third party apps imports
from graphene_django import DjangoObjectType

# Local imports
from .models import Book


# Create your schemas here.
class BookSchema(DjangoObjectType):
    class Meta:
        model = Book


class BookQuery(graphene.AbstractType):
    books = graphene.List(BookSchema)
    
    @graphene.resolve_only_args
    def resolve_books(self):
        return Book.objects.all()
