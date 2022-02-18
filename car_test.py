#!/usr/bin/env python3.9
import unittest


from car import Car

class TestCar(unittest.TestCase):
    def setUp(self):
        self.new_car = Car("RAA_250C","2015","Ford","Explorer",7000) 
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Car.cars_list = []
    def test_init(self):
        self.assertEqual(self.new_car.plate_no,"RAA_250C")
        self.assertEqual(self.new_car.manu_year,"2015")
        self.assertEqual(self.new_car.brand,"Ford")
        self.assertEqual(self.new_car.model,"Explorer")
        self.assertEqual(self.new_car.price,7000)


    def test_save_car(self):
        '''
        test_save_car test case to test if the car object is saved into
         the cars list
        '''
        self.new_car.save_car()
        self.assertEqual(len(Car.cars_list),1)

    def test_save_more_cars(self):
            '''
            test_save_more_cars to check if we can save more than one car
            objects to our cars_list
            '''
            self.new_car.save_car()
            car2 = Car("RBB_600F","2020","Toyota","RAV4",24000)
            car2.save_car()
            self.assertEqual(len(Car.cars_list),2)
    def test_delete_car(self):
            '''
            test_delete_car to test if we can remove a car from our cars list
            '''
            self.new_car.save_car()
            car2 = Car("RBB_600F","2020","Toyota","RAV4",24000)           
            car2.save_car()
            self.new_car.delete_car()
            self.assertEqual(len(Car.cars_list),1)
            
    def test_find_car_by_plate(self):
        '''
        test to check if we can find a car by plate number and display information
        '''

        self.new_car.save_car()
        car2 = Car("RBB_600F","2020","Toyota","RAV4",24000)   
        car2.save_car()
        the_car = Car.find_by_platenum("RBB_600F")

        self.assertEqual(the_car.plate_no,car2.plate_no)

    def test_car_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the car.
        '''

        self.new_car.save_car()
        car2 = Car("RBB_600F","2020","Toyota","RAV4",24000)   
        car2.save_car()

        car_exists = Car.car_exist("RBB_600F")
        self.assertTrue(car_exists)

    def test_display_all_cars(self):
        '''
        method that returns a list of all cars saved
        '''
        self.assertEqual(Car.display_cars(),Car.cars_list)

if __name__ == '__main__':
    unittest.main()