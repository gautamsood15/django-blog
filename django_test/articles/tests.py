from django.test import TestCase
from articles.models import Article,get_upload_file_name
from django.utils import timezone
from time import time

# Create your tests here.

class ArticleTest(TestCase):
    def create_article(self,title="title article",body="this si the body of the article"):
        return Article.objects.create(title=title,body=body,pub_date=timezone.now(),likes=0)
   
   
    def test_article_creation(self):
        a=self.create_article()
        self.assertTrue(isinstance(a,Article))
        self.assertEqual(a.__unicode__(),a.title)
    
    def test_get_upload_file_name(self):
        filename='Cheese.txt'
        path = "uploaded_files/%s_%s" % (str(time()).replace('.','_'),filename)
        created_path = get_upload_file_name(self,filename)
        
        self.assertEqual(path,created_path)