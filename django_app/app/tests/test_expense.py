from django.contrib.auth import get_user_model
from django.urls import reverse
import random
from datetime import datetime, timedelta
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Expense, Category


class ExpenseCRUDTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='TestUser',
            email='test@user.com',
            password='testuserpassword'
        )
        self.client.force_authenticate(user=self.user)

        self.category = Category.objects.create(name='Test Category', user=self.user)

        self.expense = Expense.objects.create(
            title='Test Expense',
            amount=100,
            data=datetime.now().date(),
            user=self.user,
            category=self.category
        )

    def test_create_expense(self):
        print(self.client)

        url = reverse('expense-list')

        start_date = datetime.now().date()
        random_date = start_date + timedelta(days=random.randint(0, 10))

        data = {
            'title': 'Test Title',
            'amount': random.randint(1, 1000),
            'data': random_date,
            'category': self.category.id,
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Expense.objects.count(), 2)
        self.assertEqual(Expense.objects.filter(title='Test Title').exists(), True)
        self.assertEqual(Expense.objects.get(title='Test Title').user, self.user)

    def test_retrieve_expense(self):
        url = reverse('expense-detail', args=[self.expense.pk])

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Expense.objects.get().title, 'Test Expense')
        self.assertEqual(Expense.objects.get().user, self.user)

    def test_update_expense(self):
        url = reverse('expense-detail', args=[self.expense.pk])

        data = {
            'title': 'Updated Title',
            'amount': 1234
        }

        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Expense.objects.get().title, 'Updated Title')
        self.assertEqual(Expense.objects.get().amount, 1234)

    def test_delete_expense(self):
        url = reverse('expense-detail', args=[self.expense.pk])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Expense.objects.count(), 0)

