from django.test import TestCase
from .models import Editor,Article,tags

class EditorTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.micah= Editor(first_name = 'Micah', last_name ='Mutugi', email = 'micahkimathi@gmail.com')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.micah,Editor))
        
    # Testing Save Method
    def test_save_method(self):
        self.micah.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

