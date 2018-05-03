# apps/books/tests/test_schemas.py
# Python imports
import random


# Django imports


# Third party apps imports
from graphene.test import Client
from model_mommy import mommy
from snapshottest import TestCase


# Local imports
from ..models import Collection, Course, Editorial, Kind, Pdf
from apps.core.schema import schema


# Create your schemas tests here.
class CollectionTestCase(TestCase):
    def setUp(self):
        self.collections = mommy.make(Collection, _quantity=20)
        self.client = Client(schema)

    def test_all_collectionss_list(self):
        self.assertMatchSnapshot(self.client.execute('''
            query Collection {
                allCollections {
                    id
                    name
                    editorial {
                        id
                        name
                    }
                }
            }
        '''))

    def tearDown(self):
        for collection in self.collections:
            collection.delete()


class CourseTestCase(TestCase):
    def setUp(self):
        self.courses = mommy.make(Course, _quantity=20)
        self.client = Client(schema)

    def test_all_courses_list(self):
        self.assertMatchSnapshot(self.client.execute('''
            query Course {
                allCourses {
                    id
                    name
                }
            }
        '''))

    def tearDown(self):
        for course in self.courses:
            course.delete()


class EditorialTestCase(TestCase):
    def setUp(self):
        self.editorials = mommy.make(Editorial, _quantity=20)
        self.client = Client(schema)

    def test_all_editorials_list(self):
        self.assertMatchSnapshot(self.client.execute('''
            query Editorial{
                allEditorials {
                    id
                    name
                }
            }
        '''))

    def tearDown(self):
        for editorial in self.editorials:
            editorial.delete()


class KindTestCase(TestCase):
    def setUp(self):
        self.kinds = mommy.make(Kind, _quantity=20)
        self.client = Client(schema)

    def test_all_kinds_list(self):
        self.assertMatchSnapshot(self.client.execute('''
            query Kind {
                allKinds {
                    id
                    name
                }
            }
        '''))

    def tearDown(self):
        for kind in self.kinds:
            kind.delete()


class PdfTestCase(TestCase):
    def setUp(self):
        self.pdfs = mommy.make(Pdf, _quantity=20)
        self.client = Client(schema)
        self.pdfs_queryset = Pdf.objects.all()
        self.list_variables = [
            {
                "collection": random.choice(list(set(
                    self.pdfs_queryset.values_list("collection", flat=True)))),
            },
            {
                "course": random.choice(
                    list(set(
                        self.pdfs_queryset.values_list("course", flat=True)))),
            },
            {
                "kind": random.choice(
                    list(set(
                        self.pdfs_queryset.values_list("kind", flat=True)))),
            }
        ]
        self.element_variables = [
            {
                "id": random.choice(
                    list(set(self.pdfs_queryset.values_list("id", flat=True)))),
            },
            {
                "name": random.choice(
                    list(set(
                        self.pdfs_queryset.values_list("name", flat=True)))),
            }
        ]

    def test_all_pdfs_list(self):
        self.assertMatchSnapshot(self.client.execute('''
            query Pdf {
                allPdfs {
                    available
                    name
                    url
                }
            }
        '''))

    def test_filter_pdfs_list(self):
        for variable in self.list_variables:
            self.assertMatchSnapshot(self.client.execute('''
                query Pdf($collection: Int, $course: Int, $kind: Int) {
                    allPdfs (
                            collection: $collection, course: $course,
                            kind: $kind) {
                        available
                        name
                        url
                    }
                }
            ''', variable_values=variable))

    def tests_get_by_parameter(self):
        for variable in self.element_variables:
            self.assertMatchSnapshot(self.client.execute('''
                query Pdf($id: Int, $name: String) {
                    pdf (id: $id, name: $name) {
                        available
                        name
                        url
                    }
                }
            ''', variable_values=variable))

    def tearDown(self):
        for pdf in self.pdfs:
            pdf.delete()
