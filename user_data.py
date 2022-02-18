#!/usr/bin/env python3.9
from user import User


#This are sample object to use while testing functions
dummy_user1 = User("001","Grace","Umutesi","grace@gmail.com")
dummy_user2 = User("002","gaga","Umutesi","grace@gmail.com")

def read_file(my_file):
    """
    Function that reads a text file and returns the data from the text file
    """
    try:
        with open(my_file, "r") as fl:

            users_info = fl.read()
            return users_info
    except FileNotFoundError:

        return None
def write_to_file(my_file):
    """
    Function that reads a text file and returns the data from the text file
    """
    try:
        with open(my_file, "w") as fl:

            users_info = fl.write("Grace")
            return users_info
    except FileNotFoundError:

        return None


def save_user_tofile(sample_user):
    '''
    function to take a user object created and save it to the file
    '''
    user_fullstring= (sample_user.user_id +" "+sample_user.first_name +" "+ sample_user.last_name +" "+ sample_user.email)
    try:
        with open("user_data.txt", "a") as fl:

            users_info = fl.write(user_fullstring+ "\n")
            return users_info
    except FileNotFoundError:

        return None

def delete_user_fromfile(sample_user):
    '''
    Function that deletes a user from the file
    '''
    user_fullstring= (sample_user.user_id +" "+sample_user.first_name +" "+ sample_user.last_name +" "+ sample_user.email)
    try:
        with open("user_data.txt", "r") as fl:
            all_lines = fl.readlines()
        with open("user_data.txt", "w") as fl:
            for line in all_lines:
                if line.strip("\n") != user_fullstring:
                    fl.write(line)

    except FileNotFoundError:
        return None



# save_user_tofile(dummy_user1)
# save_user_tofile(dummy_user2)
delete_user_fromfile(dummy_user1)