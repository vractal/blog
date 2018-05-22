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


class AdaoTest(TestCase):
    def setUp(self):
        self.response = self.client.get("/adao")

    def test_get(self):
        """ Get must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """  Must use home.html template"""
        self.assertTemplateUsed(self.response,"home.html")

    def test_html(self):
        """ Html must contain same number of posts (no pagination) """
        tag = models.Tag.objects.get(name="adao")
        models.Post.objects.create(title="post teste",content="conteudo teste")

        for i in range(1,10):
            post = models.Post.objects.create(title="post teste",content="conteudo teste")
            post.tags.add(tag)
            post.save()
            response = self.client.get("/adao")
            posts_number =  len(models.Post.objects.filter(tags=tag))
            self.assertContains(response,"<article", posts_number)



class BlogTest(TestCase):
    def setUp(self):
        self.response = self.client.get("/blog")

    def test_get(self):
        """ Get must return status code 200 """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use blog.html template """
        self.assertTemplateUsed(self.response,"blog.html")

    def test_html(self):
        """ Must contain the same number of posts in page as created """
        tag = models.Tag.objects.get(name="blog")
        models.Post.objects.create(title="post teste",content="conteudo teste")
        for i in range(1,10):
            post = models.Post.objects.create(title="post teste",content="conteudo teste")
            post.tags.add(tag)
            post.save()
            response = self.client.get("/blog")
            posts_number =  len(models.Post.objects.filter(tags=tag))
            self.assertContains(response,"<article", posts_number)


class PostPageTest(TestCase):
    def setUp(self):
        self.post = models.Post.objects.create(title="teste",content="Conteudo mesmo")
        self.post.tags.add(models.Tag.objects.create(name="adao",description="adao"))
        url = "/post/" + str(self.post.slug)
        self.response = self.client.get(url)

    def test_slug_get(self):
        """ Get must return status code 200 """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use blog.html template if doesnt contain adao tag """
        if models.Tag.objects.get(name="adao") in self.post.tags.all():
            self.assertTemplateUsed(self.response,"home.html")
        else:
            self.assertTemplateUsed(self.response,"blog.html")

    def test_content(self):
        """ Must contain the article matching slug """
        pass




class MarkdownTest(TestCase):
# O teste deveria pegar um texto completo em markdown e validar(?)
    def test_h1(self):
        """ Must convert markdown heading to html"""
        tag = models.Tag.objects.create(name="blog",description="blog")
        post = models.Post.objects.create(title="Markdown",content="# h1-tag")
        post.tags.add(models.Tag.objects.get(name="blog"))
        self.response = self.client.get("/blog")
        self.assertContains(self.response,"<h1>h1-tag</h1>")

    def test_lists(self):
        """ Must convert markdown heading to html"""
        try:
            tag = models.Tag.objects.get(name="blog")
        except:
            tag = models.Tag.objects.create(name="blog",description="blog")
        post = models.Post.objects.create(title="Markdown",content="- item - item")
        post.tags.add(models.Tag.objects.get(name="blog"))
        self.response = self.client.get("/blog")
        self.assertContains(self.response,"<ul>")
        self.assertContains(self.response,"<li>item")
