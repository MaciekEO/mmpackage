import unittest

from mmpackage.weather import get_location
from mmpackage.weather import weather

class TestWeather(unittest.TestCase):
    def test_location(self):
        result1, result2 = get_location()
        self.assertEqual(result1, 53.1277491)
        self.assertEqual(result2, 23.0159807)

    
    def test_weather(self):
        result = weather()
        self.assertTrue(result>-50)
        self.assertTrue(result<50)


if __name__ == '__main__':
    unittest.main()
