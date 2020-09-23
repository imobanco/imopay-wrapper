from unittest import TestCase


class RegexTestCase(TestCase):
    def test_date_regex(self):
        from imopay_wrapper.regex import date_regex

        expected = "^\d{4}-\d{2}-\d{2}$"  # noqa

        self.assertEqual(date_regex, expected)
