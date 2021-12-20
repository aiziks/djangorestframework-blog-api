from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase , APIClient
from blog.models import Post , Category
from django.contrib.auth.models import User



class PostTests(APITestCase):

    def test_view_posts(self):

        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        # self.assertEqual(response.status_code , status.HTTP_200_OK)


    def test_create_post(self):
        
        self.test_category = Category.objects.create(name="working")
        self.test_user_1 = User.objects.create_superuser(username="aiziks", password="aiziks111")
        self.test_user_1 = User.objects.create_user(username="isaac", password="adedayo")

        
        data = {"title" : "new" , "author":1, "excerpt": "new" , "content":"new" , "slug" : "hello" }
        url = reverse('blog_api:listcreate')
        response = self.client.post(url , data , format='json')
        # self.assertEqual(response.status_code , status.HTTP_201_CREATED)


    # only specific user can update their own post
    def test_post_update(self):

        client = APIClient() # for simulating login in user

        self.test_category = Category.objects.create(name="working")
        self.test_user_1 = User.objects.create_user(username="isaac", password="adedayo")
        self.test_user_2 = User.objects.create_user(username="dayo", password="ilovedayo")

        test_post = Post.objects.create(category_id = 1 , title = "welcome love" ,  excerpt="post cont" , content="post content" , slug="post-title", author_id=1, status="published")
        client.login(username=self.test_user_1.username , password="adedayo")

        url = reverse( ('blog_api:detailcreate') , kwargs = {'pk' : 1 } )
        response = client.put(url,{
        
                    "title": "Tech is sweet",
                    "excerpt": "I love to be world best developer",
                    "content": "I love to be world best developerI love to be world best developerI love to be world best developer",
                    "slug": "welcome-to-slug",
                    "published": "2020-11-05T09:50:46Z",
                    "date": "2020-11-05T09:51:22.969796Z",
                    "status": "published",
                    "category": 1,
                    "author": 1
                } , format='json')

        print(response.data)
        self.assertEqual(response.status_code , status.HTTP_200_OK)
        





