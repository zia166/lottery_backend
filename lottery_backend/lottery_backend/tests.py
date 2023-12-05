import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from rest_framework.exceptions import ValidationError
from rest_framework.test import APIRequestFactory
from lottery_backend.views import LotteryEntryViewSet

class TestCreate(unittest.TestCase):
    @patch('lottery_backend.models.Performance.objects.get')
    @patch('lottery_backend.models.LotteryEntry.objects.create')
    def test_create(self, mock_create, mock_get):
        # Create a mock request object
        factory = APIRequestFactory()
        data = {
            'Tickets': 5,
            'ShowName': 'Example Show',
            # 'ShowDate': '2022-01-01',  # Uncomment this line if ShowDate is required
            # 'ShowTime': '12:34 PM',  # Uncomment this line if ShowTime is required
            'UserName': 'John Doe',
        }
        request = factory.post('/lottery-entry/', data, format='json')
        
        # Mock the Performance.objects.get method
        mock_performance = MagicMock()
        mock_performance.pk = 1  # Replace with the desired performance ID
        mock_get.return_value = mock_performance
        
        # Mock the LotteryEntry.objects.create method
        mock_entry = MagicMock()
        mock_create.return_value = mock_entry
        
        # Create an instance of the class
        obj = LotteryEntryViewSet()
        
        # Assert that the create method raises a ValidationError
        with self.assertRaises(ValidationError) as cm:
            obj.create(request)
        
        # Assert the error message
        self.assertNotEqual(cm.exception.detail.find('ShowTime is required.'), -1)