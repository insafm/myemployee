from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class TestCreateUpdateEmployee(TestCase):
    def test_call_view_deny_anonymous(self):
        response = self.client.get('/employee/add/', follow=True)
        self.assertRedirects(response, '/accounts/login/?next=/employee/add/')
        response = self.client.post('/employee/add/', follow=True)
        self.assertRedirects(response, '/accounts/login/?next=/employee/add/')

    def test_call_view_load(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username=self.user.username, password='12345')  # defined in fixture or with factory in setUp()
        response = self.client.get('/employee/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard_form_wrapper.html')

    def test_call_view_fail_blank(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        response = self.client.post('/employee/add/', {}) # blank data dictionary
        self.assertEqual(response.status_code, 200)
    
    # TODO: Some text cases needs to be added.