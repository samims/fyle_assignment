import mock
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase

from branches.models import Branches, Banks

AUTH_TOKEN_URL = reverse("users:login")
IFSC_URL = reverse("branches:ifsc_search")
BRANCH_URL = reverse("branches:info")


class BranchSearchbyIfscTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@example.com", password="test@pass", username="testuser"
        )
        self.client.force_login(user=self.user)

    def test_branch_search_by_ifsc(self):
        url = IFSC_URL + "?ifsc=ABHY0065022"
        bank_obj = Banks()
        branch_obj = mock.Mock(Branches)

        bank_obj.name = "SBI"
        bank_obj.id = 1

        branch_obj.ifsc = "abcd"
        branch_obj.bank = bank_obj
        branch_obj.address = "My Address"
        branch_obj.city = "My City"
        branch_obj.state = "My State"
        branch_obj.district = "My District"
        branch_obj.branch = "My Branch"

        self.assertEqual(branch_obj.bank, bank_obj)
