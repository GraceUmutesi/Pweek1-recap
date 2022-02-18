#!/usr/bin/env python3.9
import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        # create user object
        self.new_user = User("001","Grace","Umutesi","grace@gmail.com") 
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.users_list = []

    def test_init(self):
        self.assertEqual(self.new_user.user_id,"001")
        self.assertEqual(self.new_user.first_name,"Grace")
        self.assertEqual(self.new_user.last_name,"Umutesi")
        self.assertEqual(self.new_user.email,"grace@gmail.com")

    def test_save_user(self):
        '''
        test_save_user test case to test if a user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.users_list),1)
    def test_save_multiple_users(self):
        '''
        testing to check if we can save multiple users
        objects to our users_list
        '''
        self.new_user.save_user()
        # another user
        user2 = User("002","Alice","Umutoni","alice@gmail.com") 
        user2.save_user()
        self.assertEqual(len(User.users_list),2)

    def test_delete_user(self):
        '''
        test_delete_user for testing if we can remove a user from our users list
        '''
        self.new_user.save_user()
        # another user
        user2 = User("003","Alain","Shema","shema@gmail.com") 
        user2.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.users_list),1)

if __name__ == '__main__':
    unittest.main()