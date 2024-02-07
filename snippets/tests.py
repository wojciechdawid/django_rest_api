from django.test import TestCase
from snippets.models import Snippet


class TestSnippet(TestCase):

    def test_save_highlighted(self):
        s = Snippet.objects.create(code="x += 3")
        self.assertEqual(s.highlighted, "")


class TestSnippetView(TestCase):

    def test_list(self):
        user = "XXX"
        Snippet.objects.create(code="x=1", owner=user)
        response = self.client.get("/api/v1/snippets/", content_type="application/json")

        self.assertEqual(response.json(), ["xxx"])

