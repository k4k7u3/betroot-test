import unittest
from unittest import TestCase
import sys
sys.path.insert(0, "D:\\github_test\\betroot-test")


from phonebook_class.main import menu, Person


class TestPerson(TestCase):
    def test_class_person_init_success(self):
        expected_name = "A"
        expected_surname = "B"
        expected_full_name = expected_name + ' ' + expected_surname
        expected_telephone = "123"
        expected_city = "C"
        test_person = Person(expected_name,
                             expected_surname,
                             expected_telephone,
                             expected_city)
        self.assertEqual(test_person.name, expected_name)
        self.assertEqual(test_person.surname, expected_surname)
        self.assertEqual(test_person.full_name, expected_full_name)
        self.assertEqual(test_person.telephone, expected_telephone)
        self.assertEqual(test_person.city, expected_city)

    def test_correct_print_class_object(self):
        test_object = Person("A", "B", "123", "C")
        expected_print = "A from C"
        actual_print = f"{test_object.name} from {test_object.city}"
        self.assertEqual(actual_print, expected_print)

    def test_get_dict_success(self):
        test_object = Person("A", "B", "123", "C")
        expected_dict = {"name": "A",
                         "surname": "B",
                         "full_name": "A" + " " + "B",
                         "telephone": "123",
                         "city": "C"}
        actual_dict = test_object.get_dict()
        self.assertEqual(expected_dict, actual_dict)

    def test_search_success(self):
        test_object = Person("A", "B", "123", "C")
        expected_result = None
        test_attribute = "name"
        test_value = "A"
        for attr, value in test_object.__dict__.items():
            if attr == test_attribute and value == test_value:
                expected_result = True
        actual_result = test_object.search(test_attribute, test_value)
        self.assertEqual(expected_result, actual_result)


class TestPreInitialization(TestCase):
    def test_pre_init_succes(self):
        test_list = []
        test_json_file = [{"name": "A",
                           "surname": "B",
                           "telephone": "123",
                           "city": "C"}]
        expected_list = []
        expected_list.append(Person("A", "B", "123", "C"))
        if len(test_json_file) > 0:
            for i in test_json_file:
                test_list.append(Person(**i))
        self.assertEqual(expected_list, test_list)


if __name__ == "__main__":
    unittest.main()