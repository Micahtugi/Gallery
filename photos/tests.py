from django.test import TestCase
from .models import Editor,Article,tags

class EditorTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.micah= Editor(first_name = 'Micah', last_name ='Mutugi', email = 'micahkimathi@gmail.com')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.micah,Editor))

