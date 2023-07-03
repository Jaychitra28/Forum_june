from django.test import TestCase
from django.urls import reverse, resolve
from forum.models.thread import Thread
from forum.models.category import Category
from forum.models.response import Response
from forum.views import (category, create_response, create_thread, dashboard,
                         thread_detail, thread_list,edit_response,edit_thread)
# from tests.mixin import ModelMixin
from django.contrib.auth.models import User
from forum.models.forms import EditResponseForm


class CategoryTests(TestCase):
    def setUp(self):
        self.board = Category.objects.create(
            title="Django", description="Django board."
        )
        url = reverse("category")
        self.response = self.client.get(url)

    def test_category_view_status_code(self):
        url = reverse("category")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_category_url_resolves_home_view(self):
        view = resolve("/category/")
        self.assertEquals(view.func, category)


class NewThreadTests(TestCase):
    def setUp(self):
        Category.objects.create(name="Django", description="Django board.")
        self.username = "john"
        self.password = "123"
        User.objects.create_user(
            username=self.username,
            email="john@doe.com",
            password=self.password,
        )
        self.client.login(username=self.username, password=self.password)

    def test_new_thread_view_redirect_status_code(self):
        url = reverse("create_thread", kwargs={"category_id": 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_thread_view_not_found_status_code(self):  
        url = reverse("create_thread", kwargs={"category_id": 999})
        self.client.login()
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_thread_url_resolves_new_thread_view(self):
        view = resolve("/category/1/thread/")
        self.assertEquals(view.func, create_thread)

    def test_new_thread_invalid_data(self):
        url = reverse("create_thread", kwargs={"category_id": 1})
        response = self.client.post(url, {})
        self.assertEquals(response.status_code, 200)


class ResponseUpdateViewTestCase(TestCase):
    def setUp(self):
        self.category= Category.objects.create(
            title="Django", description="Django board."
        )
        self.username = "john"
        self.password = "123"
        user = User.objects.create_user(
            username=self.username,
            email="john@doe.com",
            password=self.password,
        )
        self.thread = Thread.objects.create(
            title="Hello world", description ="hellooo",category=self.category
        )
        self.response = Response.objects.create(
            message="Lorem ipsum dolor sit amet",
            thread=self.thread,
            created_by=user,
            updated_by=user,
        )
        self.url = reverse(
            "edit_response",
            kwargs={
                # "category_id": self.category.id,
                "thread_id": self.thread.id,
                "response_id": self.response.id,
            },
        )


class LoginRequiredPostUpdateViewTests(ResponseUpdateViewTestCase):
    def test_redirection(self):

        login_url = reverse("login")
        response = self.client.get(self.url)
        self.assertRedirects(
            response,
            "{login_url}?next={url}".format(login_url=login_url, url=self.url),
        )


class UnauthorizedPostUpdateViewTests(ResponseUpdateViewTestCase):
    def setUp(self):

        super().setUp()
        username = "jane"
        password = "321"
        user = User.objects.create_user(
            username=username, email="jane@doe.com", password=password
        )
        self.client.login(username=username, password=password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.client.get(self.url)
        self.assertEqual(self.response.status_code, 404)


class ResponseUpdateViewTestCase(ResponseUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_class(self):
        view = resolve("/boards/1/topics/1/posts/1/edit")
        self.assertEquals(view.func, edit_response)

    def test_contains_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, EditResponseForm)

   


class SuccessfulResponseUpdateViewTests(ResponseUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.post(
            self.url, {"message": "edited message"}
        )

    def test_redirection(self):
        topic_posts_url = reverse(
            "create_response",
            kwargs={"thread": self.thread.id},
        )
        self.assertRedirects(self.response, topic_posts_url)

    def test_response_changed(self):
        self.response.refresh_from_db()
        self.assertEquals(self.response.message, "edited message")


class InvalidPostUpdateViewTests(ResponseUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.post(self.url, {})

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 302)


class TheradResponseTests(TestCase):
    def setUp(self):
        Category = Category.objects.create(title='Django', description='Django board.')
        user = User.objects.create_user(username='john', email='john@doe.com', password='123')
        thread = Thread.objects.create(subject='Hello, world', category=category, create_by=user)
        Response.objects.create(message='Lorem ipsum dolor sit amet', thread=thread, created_by=user)
        url = reverse('thread_list', kwargs={'category_id': category.id, 'thread_id': thread.id})
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/category/1/thread/1/')
        self.assertEquals(view.func, create_response )