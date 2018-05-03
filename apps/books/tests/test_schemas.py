# apps/books/tests/test_schemas.py
# Python imports
import random

# Django imports


# Third party apps imports
from graphene.test import Client
from model_mommy import mommy
from snapshottest import TestCase

# Local imports
from ..models import Pdf
from apps.core.schema import schema


# Create your schemas tests here.
class APITestCase(TestCase):
    def setUp(self):
        self.pdfs = mommy.make(Pdf, _quantity=7)
        self.client = Client(schema)
        self.pdfs_queryset = Pdf.objects.all()

    def test_pdfs_list(self):
        self.assertMatchSnapshot(self.client.execute('''
            query {
                allPdfs {
                    id
                    name
                }
            }
        '''))

    def tests_filter_by_id(self):
        pdf_id_exists = random.choice(list(set(
            self.pdfs_queryset.values_list("id", flat=True))))
        self.assertMatchSnapshot(self.client.execute('''
            query Pdf($id: Int, $name: String) {
                pdf (id: $id, name: $name) {
                    id
                    name
                }
            }
        ''', variable_values={"id": pdf_id_exists}))

    def tests_filter_by_name(self):
        pdf_name_exists = random.choice(list(set(
            self.pdfs_queryset.values_list("name", flat=True))))
        self.assertMatchSnapshot(self.client.execute('''
            query Pdf($id: Int, $name: String) {
                pdf (id: $id, name: $name) {
                    id
                    name
                }
            }
        ''', variable_values={"name": pdf_name_exists}))

    def tearDown(self):
        for pdf in self.pdfs:
            pdf.delete()
