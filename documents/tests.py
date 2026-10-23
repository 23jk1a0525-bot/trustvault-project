

from django.test import TestCase
from django.urls import reverse


class TrustVaultSecurityTests(TestCase):

    def test_upload_page_requires_login(self):
        response = self.client.get("/documents/upload/")

        self.assertIn(response.status_code, (301, 302))
        self.assertIn("/accounts/login/", response.url)

    def test_login_page_is_accessible(self):
        response = self.client.get("/accounts/login/")

        self.assertEqual(response.status_code, 200)
        
    def test_anonymous_download_is_rejected(self):
        response = self.client.get(
            "/documents/download/nonexistent.txt/"
        )

        self.assertIn(response.status_code, (301, 302, 403, 404))

    def test_anonymous_delete_is_rejected(self):
        response = self.client.post(
            "/documents/delete/nonexistent.txt/"
        )

        self.assertIn(response.status_code, (301, 302, 403, 404))



# Create your tests here.
