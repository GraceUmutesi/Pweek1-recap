#!/usr/bin/env python3.9
import unittest
import user_data

class TestReadFiles(unittest.TestCase):
    """
    Class to test the  function in user_data file
    """
    def test_not_thefile(self):
        """
        Test to confirm that an exeption is raised when a wrong file is inputted
        """
        self.assertEqual(None,user_data.read_file("anyother.txt"))

    def test_read_user(self):
        """
        Test case to confirm that we are getting data from the file
        """
        with open("user_data.txt","r") as fl:
            content = fl.read()
            self.assertEqual(content,user_data.read_file("user_data.txt"))

    def test_write_user(self):
        """
        Test case to confirm that we are getting data from the file
        """
        with open("user_data.txt","w") as fl:
            content = fl.write("Grace")
            self.assertEqual(content,user_data.write_to_file("user_data.txt"))
            fl.truncate(0)  #for clearing the file after the test
    
if __name__ == "__main__":
    unittest.main()