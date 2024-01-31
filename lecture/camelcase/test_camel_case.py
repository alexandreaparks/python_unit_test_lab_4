from unittest import TestCase
import camel_case


class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):
        self.assertEqual("helloWorld", camel_case.camelcase("Hello World"))
        self.assertEqual("", camel_case.camelcase(""))
        self.assertEqual("helloWorld", camel_case.camelcase("      Hello    World     "))
        