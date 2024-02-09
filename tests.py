from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post  # models modulini .models ga o'zgartiring

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='Yangi post',  # author_ ni author ga o'zgartiring
            body='Post matni',
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title='Post mavzusi')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(self.post.title, 'Yangi post')  # f-string dan olib tashlang
        self.assertEqual(self.post.author.username, 'testuser')  # f-string dan olib tashlang
        self.assertEqual(self.post.body, 'Post matni')  # f-string dan olib tashlang

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post matni')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')  # chiziqni olib tashlang
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Yangi post')
        self.assertTemplateUsed(response, 'post_detail.html')




