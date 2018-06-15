from django.test import TestCase
from django.urls import resolve, reverse

from .forms import NewArticleForm
from .models import Article
from .views import article_overview, home, new_article

# Create your tests here.


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func, home)


class ArticleOverviewTests(TestCase):
    """Tests the article_overview page.
    """

    def test_http_return_code_article_view(self):
        """Test checks for the right http
        return code 200."""
        url = reverse('article_overview')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article_url_resolves_article_view(self):
        """Tests verifies if the /articles/ url
        resolves the article_overview"""
        view = resolve('/articles/')
        self.assertEqual(view.func, article_overview)


class AddArticleTests(TestCase):
    """Tests the site for the creation
    of new articles."""

    def test_http_return_code_article_creation(self):
        url = reverse('new_article')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article_creation_url_resolvation(self):
        view = resolve('/article/new/')
        self.assertEqual(view.func, new_article)

    def test_csrf(self):
        url = reverse('new_article')
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_article_valid_post_data(self):
        url = reverse('new_article')
        data = {
            'name': 'Testing article',
            'amount': 12345,
            'article_number': 1337
        }
        response = self.client.post(url, data)
        self.assertTrue(Article.objects.exists())

    def test_new_article_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_article')
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(form.errors)

    def test_new_article_invalid_post_data_empty_fields(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_article')
        data = {
            'name': '',
            'amount': '',
            'article_number': ''
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Article.objects.exists())

    def test_site_contains_form(self):
        url = reverse('new_article')
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewArticleForm)


class ViewArticleInDetail(TestCase):
    """Opens the detailed view for an article.
    """

    def setUp(self):
        Article.objects.create(
            name='Article for Testing purposes', amount=123, article_number=1)

    def test_existing_detailed_article(self):
        url = reverse('article_view', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_not_existing_detailed_article(self):
        url = reverse('article_view', kwargs={'pk': 100})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
