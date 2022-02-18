class Car:
    """
    Class that generates new instances of cars.
    """

    cars_list = [] 

    def __init__(self,plate_no,manu_year,brand,model,price):


        self.plate_no = plate_no
        self.manu_year = manu_year
        self.brand = brand
        self.model = model
        self.price = price
        
    def save_car(self):
        '''
        save_car method saves car objects into cars_list
        '''
        Car.cars_list.append(self)
    
    def delete_car(self):
        '''
        delete_car method deletes a saved car from the cars_list
        '''
        Car.cars_list.remove(self)
        
    @classmethod
    def find_by_platenum(cls,platenum):
        for car in cls.cars_list:
            if car.plate_no == platenum:
                return car


    @classmethod
    def car_exist(cls,platenum):
        '''
        Method that checks if a car exists from the cars list.
        '''
        for car in cls.cars_list:
            if car.plate_no == platenum:
                    return True

        return False
    @classmethod
    def display_cars(cls):
        '''
        method that returns the list of cars
        '''
        return cls.cars_list