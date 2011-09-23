from django.utils import unittest
from models import Blog,BlogEntry
from django.test.client import Client
from datetime import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class BlogTestCase(unittest.TestCase):

    def setUp(self):
        self.blog = Blog(title = "test",tag_line = "new blog",entries_per_page=10,recents = 5, recent_comments = 5)
        self.blog.save()

    def test_single_existence(self):
        """Test that the blog is created only once """
        blog = Blog(title = "test",tag_line = "new blog",entries_per_page=10,recents = 5, recent_comments = 5)
        #should raise Exception when another blog is created
        self.assertRaises(Exception,blog.save())


class TestViews(unittest.TestCase):
    """Test pages  of the blog"""
    def setUp(self):
        self.c = Client()

    def test_first_page(self):
        response = self.c.get( reverse("blogango_index"))
        #it should return 200 for all users
        self.assertEqual(response.status_code,200)
        
    def test_admin_page(self):
        response = self.c.get(reverse("blogango_admin_dashboard"))
        self.assertEqual(response.status_code , 200)

    def test_add_entry(self):
        user  = User.objects.create_user(username = 'gonecrazy',email='gonecrazy@gmail.com',password = 'gonecrazy')
        user.is_staff = True
        user.save()
        response = self.c.login(username='gonecrazy',password='gonecrazy')
        response = self.c.post( reverse("blogango_admin_entry_new"),{'title':'test post','text':'this is the test post','publish_date_0':'2011-09-22','publish_date_1':'17:17:55','text_markup_type':"html",'created_by':1,'publish':'Save and Publish'})
        #check for successful posting of entry
        self.assertEqual(response.status_code,302)
        blog = BlogEntry.default.all()
        self.assertEqual(1,blog.count())
        


        def test_entry_existence(self):
            response = self.c.get('/blog/2011/09/test-post/')
            self.assertEqual(response.status_code,200)
    
    
            


        

        

        

        
        
        
    

