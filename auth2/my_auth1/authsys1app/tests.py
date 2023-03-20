from django.test import TestCase
from django.contrib.auth.models import User

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'admin1',
            'password': '123'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/authsys1app/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_authenticated)


# class MyTestCase(TestCase):
#     def test_login(self):
#         self.assertFalse(get_user(self.client).is_authenticated)
#         self.client.login(username='admin1', password='123')
#         self.assertTrue(get_user(self.client).is_authenticated)



# def login(self, data):
#     self.username = 'PC301'
#     self.password = 'UdcPYRRt'
#     user = User.objects.create(username=self.username)
#     user.set_password(self.password)
#     user.save()
#
#     c = Client()
#     c.login(username=self.username, password=self.password)
#     return c, user
