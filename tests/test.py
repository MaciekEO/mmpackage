import unittest

from mmpackage.weather import get_location
from mmpackage.weather import weather

class TestWeather(unittest.TestCase):
    def test_location(self):
        result = get_location()
        self.assertEqual(result, 53.1277491, 23.0159807)
    
    def test_weather(self):
        result = weather()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
