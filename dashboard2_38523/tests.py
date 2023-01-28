from rest_framework.test import APIClient, APITestCase
from .testdata import valid_user, valid_login, wrong_password, missing_password_data
from rest_framework.views import status
        

class UserRegistrationTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_valid_registration(self):
        response = self.client.post('/rest-auth/registration/', valid_user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(list(response.data.keys())[0], "key")
    
    def test_invalid_registration(self):
        response = self.client.post('/rest-auth/registration/', missing_password_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password'][0], "This field is required.")
    
    def test_valid_login(self):
        self.client.post('/rest-auth/registration/', valid_user, format='json')
        response = self.client.post('/rest-auth/login/', valid_login, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data.keys())[0], "key")
    
    def test_invalid_login(self):
        self.client.post('/rest-auth/registration/', valid_user, format='json')
        response = self.client.post('/rest-auth/login/', wrong_password, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['non_field_errors'][0], "Unable to log in with provided credentials.")
