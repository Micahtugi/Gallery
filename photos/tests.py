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

class ArticleTestClass(TestCase):
    def setUp(self):
        # Creating a new editor and saving it
        self.micah= Editor(first_name = 'Micah', last_name ='Mutugi',email ='micahkimathi@gmail.com')
        self.micah.save_editor()
        
        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()
        
        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.micah)
        self.new_article.save()
        self.new_article.tags.add(self.new_tag)
        
    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
