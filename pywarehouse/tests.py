from django.test import TestCase
from django.urls import resolve, reverse

from .views import home, article_overview

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
