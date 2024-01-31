"""
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

"""

from student_lists import ClassList, StudentError
from unittest import TestCase


class TestStudentLists(TestCase):

    def test_cant_create_class_with_negative_students(self):
        with self.assertRaises(StudentError):
            test_class = ClassList(-1)

    def test_cant_create_class_with_zero_students(self):
        with self.assertRaises(StudentError):
            test_class = ClassList(0)

    def test_can_create_class_with_positive_number_of_students(self):
        test_class = ClassList(1)
        # TODO does this test need anything else?

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)

    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')

    def test_add_remove_student_ensure_removed(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.remove_student('Test Student')
        self.assertNotIn('Test Student', test_class.class_list)

    def test_add_students_remove_student_not_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.add_student('Another Test Student')
        with self.assertRaises(StudentError):
            test_class.remove_student('Student Not in List')

    def test_remove_student_from_empty_list(self):
        test_class = ClassList(2)
        with self.assertRaises(StudentError):
            test_class.remove_student('Student Not in List')

    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))

    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))

    def test_is_enrolled_for_student_not_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student("Alexandrea Parks")
        test_class.add_student("August Pepper")
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))

    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))

    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))

    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))

    def test_index_of_student_is_none_if_class_list_is_empty(self):
        test_class = ClassList(2)
        index = test_class.index_of_student("Test Student")
        self.assertIsNone(index)

    def test_index_of_student_is_none_if_student_not_in_list(self):
        test_class = ClassList(2)
        test_class.add_student("Test Student")
        test_class.add_student("Another Test Student")
        index = test_class.index_of_student("Not a Student")
        self.assertIsNone(index)

    # TODO write a test for your new is_class_full method when the class is full.
    # use assertTrue.

    # TODO write a test for your new is_class_full method for when is empty,
    # and when it is not full. Use assertFalse.
