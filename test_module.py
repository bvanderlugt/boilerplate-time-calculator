import unittest
from time_calculator import (add_time,
                             _split_twelve_hour,
                             _convert_to_minutes,
                             _convert_to_twelvehour)


class UnitTests(unittest.TestCase):
    maxDiff = None
    def test_same_period(self):
        actual = add_time("3:30 PM", "2:12")
        expected = "5:42 PM"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "3:30 PM", "2:12" to return "5:42 PM"')

    def test_different_period(self):
        actual = add_time("11:55 AM", "3:12")
        expected = "3:07 PM"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:55 AM", "3:12" to return "3:07 PM"')

    def test_next_day(self):
        actual = add_time("9:15 PM", "5:30")
        expected = "2:45 AM (next day)"
        self.assertEqual(actual, expected, 'Expected time to end with "(next day)" when it is the next day.')

    def test_period_change_at_twelve(self):
        actual = add_time("11:40 AM", "0:25")
        expected = "12:05 PM"
        self.assertEqual(actual, expected, 'Expected period to change from AM to PM at 12:00')

    def test_twenty_four(self):
        actual = add_time("2:59 AM", "24:00")
        expected = "2:59 AM (next day)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "2:59 AM", "24:00" to return "2:59 AM"')

    def test_two_days_later(self):
        actual = add_time("11:59 PM", "24:05")
        expected = "12:04 AM (2 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:59 PM", "24:05" to return "12:04 AM (2 days later)"')

    def test_high_duration(self):
        actual = add_time("8:16 PM", "466:02")
        expected = "6:18 AM (20 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "8:16 PM", "466:02" to return "6:18 AM (20 days later)"')

    def test_no_change(self):
        actual = add_time("5:01 AM", "0:00")
        expected = "5:01 AM"
        self.assertEqual(actual, expected, 'Expected adding 0:00 to return initial time.')

    def test_same_period_with_day(self):
        actual = add_time("3:30 PM", "2:12", "Monday")
        expected = "5:42 PM, Monday"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "3:30 PM", "2:12", "Monday" to return "5:42 PM, Monday"')

    def test_twenty_four_with_day(self):
        actual = add_time("2:59 AM", "24:00", "saturDay")
        expected = "2:59 AM, Sunday (next day)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "2:59 AM", "24:00", "saturDay" to return "2:59 AM, Sunday (next day)"')

    def test_two_days_later_with_day(self):
        actual = add_time("11:59 PM", "24:05", "Wednesday")
        expected = "12:04 AM, Friday (2 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:59 PM", "24:05", "Wednesday" to return "12:04 AM, Friday (2 days later)"')

    def test_high_duration_with_day(self):
        actual = add_time("8:16 PM", "466:02", "tuesday")
        expected = "6:18 AM, Monday (20 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "8:16 PM", "466:02", "tuesday" to return "6:18 AM, Monday (20 days later)"')

    def test_util_split_twelve_hour(self):
        actual = _split_twelve_hour("12:01 PM")
        expected = ("12", "01", "PM")
        self.assertEqual(actual, expected, 'Expected calling \
                         "_split_twelve_hour" with "12:01 PM" to equal' +
                         '("12", "01", "PM")')

    def test_util_split_twelve_hour_no_phase(self):
        actual = _split_twelve_hour("12:01")
        expected = ("12", "01", None)
        self.assertEqual(actual, expected, 'Expected calling \
                         "_split_twelve_hour" with "12:01" to equal \
                         ("12", "01", None)')

    def test_util_convert_to_minutes(self):
        actual = _convert_to_minutes("1:41 PM")
        expected = 821
        self.assertEqual(actual, expected, 'Expected calling \
                         "_convert_to_minutes" with "1: 41 PM" to return 821')

    def test_util_convert_to_minutes_duration(self):
        actual = _convert_to_minutes("3:12")
        expected = 192
        self.assertEqual(actual, expected, 'Expected calling \
                         "_convert_to_minutes_duration" with "3:12" to \
                         return 192')

    def test_util_convert_to_twelvehour(self):
        actual = _convert_to_twelvehour(821)
        expected = "1:41 PM"
        self.assertEqual(actual, expected, 'Expected calling \
                         "_convert_to_twelvehour"  with 821 to \
                         return "1:41 PM"')

    def test_util_convert_to_twelvehour_zero_hour(self):
        actual = _convert_to_twelvehour(4)
        expected = "12:04 AM"
        self.assertEqual(actual, expected, 'Expected calling \
                "_convert_to_twelvehour" with 04 to return "12:04 AM"')


if __name__ == "__main__":
    unittest.main()
