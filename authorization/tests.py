from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http.response import JsonResponse
from .services.db_services import *

# Create your tests here


class TestUserLogin(TestCase):
    def setUp(self) -> None:
        self.username = 'TestUserUsername'
        self.password = 'TestUserPassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_user_can_login(self):
        response = self.client.post(reverse_lazy('login'), data={
            'username': self.username,
            'password': self.password,
            'next': reverse_lazy('home'),
        })
        self.assertEquals(response.__class__, JsonResponse,
                          msg='Response after login user is not type JsonResponse')
        self.assertDictEqual(response.json(), {'status': 'success', 'next': reverse_lazy('home')},
                             msg=f'Response after login user is not correct, it was {response.json()}')

    def test_wrong_user_cant_login(self):
        response = self.client.post(reverse_lazy('login'), data={
            'username': self.username,
            'password': 'wrong_password',
            'next': reverse_lazy('home'),
        })
        self.assertEquals(response.__class__, JsonResponse,
                          msg='Response after login wrong user is not type JsonResponse')
        self.assertEquals(response.json()['status'], 'fail',
                          msg=f'Response after login wrong user is not correct, it was {response.json()}')


class TestUserRegister(TestCase):
    def setUp(self) -> None:
        self.username = 'TestUserUsername'
        self.password = 'TestUserPassword'

    def test_user_can_register(self):
        response = self.client.post(reverse_lazy('signup'), data={
            'username': self.username,
            'password': self.password,
            'next': reverse_lazy('home'),
        })
        self.assertEquals(response.__class__, JsonResponse,
                          msg='Response after registering user is not type JsonResponse')
        self.assertDictEqual(response.json(), {'status': 'success', 'next': reverse_lazy('home')},
                             msg=f'Response after registering user is not correct, it is {response.json()}')
        user = get_user_by_params(username=self.username)
        self.assertNotEquals(user, None,
                             msg='After registering user, user was not created')

    def test_not_unique_user_cant_register(self):
        user = User.objects.create_user(username=self.username, password=self.password)
        response = self.client.post(reverse_lazy('signup'), data={
            'username': self.username,
            'password': self.password,
            'next': reverse_lazy('home'),
        })
        self.assertEquals(response.__class__, JsonResponse,
                          msg='Response after registering wrong user is not type JsonResponse')
        self.assertEquals(response.json()['status'], 'fail')

    def test_user_cant_register_without_data(self):
        response = self.client.post(reverse_lazy('signup'), data={
            'username': self.username,
        })
        self.assertEquals(response.__class__, JsonResponse,
                          msg='Response after registering wrong user is not type JsonResponse')
        self.assertEquals(response.json()['status'], 'fail')
