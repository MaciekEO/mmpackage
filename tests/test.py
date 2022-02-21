import unittest

from mmpackage.weather import get_location
from mmpackage.weather import weather

class TestWeather(unittest.TestCase):
    def test_location(self):
        result1, result2 = get_location("Bialystok")
        self.assertEqual(result1, 53.1277491)
        self.assertEqual(result2, 23.0159807)

        result1, result2 = get_location("Warsaw")
        self.assertEqual(result1, 52.2297)
        self.assertEqual(result2, 21.0122)

        result1, result2 = get_location("Berlin")
        self.assertEqual(result1, 52.5235)
        self.assertEqual(result2, 13.4115)

        result1, result2 = get_location("Paris")
        self.assertEqual(result1, 48.8567)
        self.assertEqual(result2, 2.3510)

        result1, result2 = get_location("London")
        self.assertEqual(result1, 51.5002)
        self.assertEqual(result2, -0.1262)

        result1, result2 = get_location("Moscow")
        self.assertEqual(result1, 55.7558)
        self.assertEqual(result2, 37.6176)
    
    def test_weather(self):
        result = weather(0, ["Białystok"])
        self.assertTrue(result>-50)
        self.assertTrue(result<50)


if __name__ == '__main__':
    unittest.main()
