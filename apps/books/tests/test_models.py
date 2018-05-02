# apps/books/tests/test_models.py
# Python imports


# Django imports
from django.test import TestCase


# Thirod party apps imports
from model_mommy import mommy


# Local imports
from ..models import Collection, Course, Editorial, Kind, Pdf


# Create your model tests here.
class CollectionTestCase(TestCase):
    def setUp(self):
        self.collection = mommy.make(Collection)

    def test_method_str_return_name(self):
        self.assertTrue(self.collection.name in self.collection.__str__())

    def tearDown(self):
        self.collection.delete()


class CourseTestCase(TestCase):
    def setUp(self):
        self.course = mommy.make(Course)

    def test_method_str_return_name(self):
        self.assertTrue(self.course.name in self.course.__str__())

    def tearDown(self):
        self.course.delete()


class EditorialTestCase(TestCase):
    def setUp(self):
        self.editorial = mommy.make(Editorial)

    def test_method_str_return_name(self):
        self.assertTrue(self.editorial.name in self.editorial.__str__())

    def tearDown(self):
        self.editorial.delete()


class KindTestCase(TestCase):
    def setUp(self):
        self.kind = mommy.make(Kind)

    def test_method_str_return_name(self):
        self.assertTrue(self.kind.name in self.kind.__str__())

    def tearDown(self):
        self.kind.delete()


class PdfTestCase(TestCase):
    def setUp(self):
        self.pdf = mommy.make(Pdf)

    def test_method_str_return_name(self):
        self.assertTrue(self.pdf.name in self.pdf.__str__())

    def tearDown(self):
        self.pdf.delete()
