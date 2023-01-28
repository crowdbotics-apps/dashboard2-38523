from rest_framework.test import APIClient, APITestCase
from .testdata import valid_app_1, valid_app_2, invalid_app
from dashboard2_38523.testdata import valid_login, valid_user
from rest_framework.views import status
        

class ApplicationTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_app(self):
        self.client.post('/rest-auth/registration/', valid_user, format='json')
        self.client.post('/rest-auth/login/', valid_login, format='json')

        response = self.client.post('/api/v1/apps/', valid_app_1, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'First Applications')
    
    def test_get_apps(self):
        self.client.post('/rest-auth/registration/', valid_user, format='json')
        self.client.post('/rest-auth/login/', valid_login, format='json')

        self.client.post('/api/v1/apps/', valid_app_1, format='json')
        self.client.post('/api/v1/apps/', valid_app_2, format='json')
        
        response = self.client.get('/api/v1/apps/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
