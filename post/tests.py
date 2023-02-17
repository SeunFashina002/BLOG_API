from django.test import TestCase
from django.contrib.auth.models import User

from post.models import Post

# Create your tests here.
class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create a user
        
        test_user1 = User.objects.create_user(username='testuser', password='test1pwd')
        test_user1.save()

        # create a blog post
        post = Post.objects.create(author=test_user1, title='testuser1 blog', body='this is test user1 first post')
        post.save()

    def test_blog(self):
        post_id = Post.objects.get(id=1)
        author = f'{post_id.author}'
        title = f'{post_id.title}'
        body = f'{post_id.body}'

        self.assertEqual(author, 'testuser')
        self.assertEqual(title, 'testuser1 blog')
        self.assertEqual(body, 'this is test user1 first post')
