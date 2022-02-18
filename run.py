#!/usr/bin/env python3.9

from user import User
from car import Car
from art import *
from simple_colors import *
import user_data as u

def create_user(uid,fname,lname,email):
    '''
    Function to create a user
    '''
    the_user= User(uid,fname,lname,email)
    return the_user

def save_users(user_object):
    '''
    Function to save users
    '''
    user_object.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()



def input_car(plate_no,manu_year,brand,model,price):
    '''
    Function to create a user
    '''
    the_car= Car(plate_no,manu_year,brand,model,price)
    return the_car
def del_car(car):
    '''
    Function to delete a user
    '''
    car.delete_car()

def save_cars(car_object):
    '''
    Function to save users
    '''
    car_object.save_car()


def find_car(platenumber):
    '''
    Function that finds a car by plate number and returns the car
    '''
    return Car.find_by_platenum(platenumber)

def check_existing_car(platenumber):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Car.car_exist(platenumber)
def display_cars():
    '''
    Function that returns all the saved contacts
    '''
    return Car.display_cars()


def main():
    tprint("Car Dealership")
    # print(green('Car Dealership','bold'))
    print('\n')
    print(blue('Hello Welcome to')+ green(' Car Dealership','bold'))

    print(yellow('What is your name?'))
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    print("START REGISTRATION")
    
    while True:
        print("Use these short codes : ca - create account, da - delete account, q - quit")
        short_c = input().lower()
        if short_c == 'ca':
            print("New User")
            print("-"*10)
            print ("Id your desire to have ....")
            u_id = input()
            print ("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()          

            print("Email address ...")
            e_address = input()

            u.save_user_tofile(create_user(u_id,f_name,l_name,e_address))
            save_users(create_user(u_id,f_name,l_name,e_address))
            print ('\n')
            print(f"New User {f_name} {l_name} created")
            print ('\n')
            while True:
                    
                    print("Use these short codes : ic - input car, dc - display cars, fc -find a car, dl - delete a car, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'ic':
                            print("Car Info")
                            print("-"*10)

                            print ("plate_no ....")
                            plate_nom = input()

                            print("Manufacturing Year ...")
                            manu_year = input()

                            print("Brand ...")
                            brand = input()

                            print("Model ...")
                            model = input()

                            print("Price ...")
                            price = input()


                            save_cars(input_car(plate_nom,manu_year,brand,model,price))
                            print ('\n')
                            print(f"New {brand} was created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_cars():
                                    print("Here is a list of all your cars")
                                    print('\n')

                                    for car in display_cars():
                                            print(f"{car.brand}---------{car.model}----Cost{car.price}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any cars saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the plate number of the car you want to search for")

                            search_plnumber = input()
                            if check_existing_car(search_plnumber):
                                    search_car = find_car(search_plnumber)
                                    print(f"{search_car.brand} {search_car.model}")
                                    print('-' * 20)

                            else:
                                    print("That car does not exist")

  
                    elif short_code == 'dl':
                        print('Enter the platenumber of the car you want to delete\n')
                        platenum_todel = input()
                        if check_existing_car(platenum_todel):
                            the_car = find_car(platenum_todel)
                            del_car(the_car)
                            print('...Successfully deleted...')
                        else:
                            print('The car you are trying to delete is not available')
                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                        print("I really didn't get that. Please use the short codes")
        elif short_c == 'da':
            print(red('Ohh this one is for you to implement'))
            aprint("butterfly")
            
        elif short_c == "q":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")                    
if __name__ == '__main__':

    main()