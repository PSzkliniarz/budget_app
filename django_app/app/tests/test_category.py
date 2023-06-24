from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Category


class CategoryCRUDTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='TestUser',
            email='test@user.com',
            password='testuserpassword'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_category(self):
        url = reverse('category-list')
        data = {
            'name': 'New Category',
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, 'New Category')
        self.assertEqual(Category.objects.get().user, self.user)

    def test_update_category(self):
        category = Category.objects.create(name='Test Category', user=self.user)
        url = reverse('category-detail', args=[category.pk])  # URL endpointu szczegółów kategorii
        data = {
            'name': 'Updated Category',
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.get(pk=category.pk).name, 'Updated Category')

    def test_delete_category(self):
        category = Category.objects.create(name='Test Category', user=self.user)
        url = reverse('category-detail', args=[category.pk])  # URL endpointu szczegółów kategorii
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)
