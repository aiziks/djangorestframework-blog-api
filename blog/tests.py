from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post , Category

# User = get_user_model()

# Create your tests here.
class TestCreatePost(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name="Love")
        test_user_1 = User.objects.create(username="aiziks", password="aiziks111")
        test_post = Post.objects.create(category_id = 1 , title = "welcome love" ,  excerpt="post cont" , content="post content" , slug="post-title", author_id=1, status="published")
    
    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author= f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author , 'aiziks')
        self.assertEqual(title , 'welcome love')
        self.assertEqual(content , 'post content')
        self.assertEqual(str(post) , 'welcome love')
        self.assertEqual(str(cat) , 'Love')