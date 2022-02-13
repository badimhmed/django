from django.test import TestCase
from student_management_app.models import Students, Subjects

class TestModels(TestCase):
    def setUp(self):
        self.students1 = Students.objet.create(
            name='students1',
            student_management_app=1000
        )

        def test_project_is_assigned_slug_on_creation(self):
            self.assertEquals(self.students1.slug, 'students-1')

   

    def test_Subjects(self):
        Subjects1 = Subjects.objects.create(
           subject_name = "django"
           course_id = 1 #need to give defauult course
           staff_id = 1
           created_at = "13-02-2022"
           updated_at =  "13-02-2022"
        )