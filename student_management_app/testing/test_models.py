from django.test import TestCase
from student_management_app.models import Students, Subjects

class TestModels(TestCase):
    def setUp(self):
        self.project1 = project.objet.create(
            name='projet1',
            student_management_app=100000
        )

        def test_project_is_assigned_slug_on_creation(self):
            self.assertEquals(self.project1.slug, 'project-1')