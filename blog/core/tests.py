from django.test import TestCase
from . import models
# Create your tests here.
class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get("/")

    def test_get(self):
        """ Get must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """  Must use home.html template"""
        self.assertTemplateUsed(self.response,"home.html")

    def test_html(self):
        """ Html must contain same number of posts (no pagination) """

        for i in range(1,10):
            models.Post.objects.create(title="post teste",content="conteudo teste")
            response = self.client.get("/")
            posts_number =  len(models.Post.objects.all())
            self.assertContains(response,"<article", posts_number)



class MarkdownTest(TestCase):
# O teste deveria pegar um texto completo em markdown e validar(?)
    def test_h1(self):
        """ Must convert markdown heading to html"""
        models.Post.objects.create(title="Markdown",content="# h1-tag")
        self.response = self.client.get("/")
        self.assertContains(self.response,"<h1>h1-tag</h1>")

    def test_lists(self):
        """ Must convert markdown heading to html"""
        models.Post.objects.create(title="Markdown",content="- item - item")
        self.response = self.client.get("/")
        self.assertContains(self.response,"<ul>")
        self.assertContains(self.response,"<li>item")
