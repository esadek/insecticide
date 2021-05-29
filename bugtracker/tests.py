from datetime import date
from django.test import TestCase
from . import models


class ProjectTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.project = models.Project(
            name = 'test name',
            description = 'test description'
        )

    def test_str(self):
        self.assertEqual(str(self.project), self.project.name)


class BugTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.bug = models.Bug(
            name = 'test name',
            description = 'test description',
        )

    def test_str(self):
        self.assertEqual(str(self.bug), self.bug.name)
