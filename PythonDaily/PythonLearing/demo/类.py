# -*- coding: utf-8 -*-
"""
Created on Wed May 30 15:50:22 2018

@author: Administrator
"""
"""
class Dog():
    
    def _init_(self,na`me,age):
        self.name = name
        self.age  = age
    def sit(self):
        print(self.name.title() + "is now sitting.")
    
    def roll_over(self):
        print(self.name.title() + "rolled over!" )
"""

"""
class Restaurant():
    def __init__ (self, restaurant_name, cuisine_type):#神坑，这里左右都是两个下划线
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def descriable_restaurant(self):
        print(self.restaurant_name.title()  +"是一个" + self.cuisine_type)
        
    def open_restaurant(self):
        print("餐馆正常营业，欢迎新老顾客过来品尝")

my_restaurant = Restaurant('xixi','chuang')
my_restaurant.descriable_restaurant()
my_restaurant.open_restaurant()

"""
"""
class Car():
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' +self.model
        return long_name.title()

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

"""
"""
class Car():
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' +self.model
        return long_name.title()
        
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + "miles on it")
        
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

"""

"""
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometeer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + (" ") +self.make + (" ") +self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) +"miles on it")
        
    def update_odometer(self,mileage):
        if mileage >= self.odometeer_reading:
            self.odometeer_reading = mileage
        else:
            print("you can't roll back an odometer")
            
    def increment_odometer(self,miles):
        self.odometeer_reading += miles
        
class ElectricCar(Car):
    
    def __init__(self, make , model, year):
        super().__init__(make, model ,year)
        self.battery_size = 70
        
    def describe_battery(self):
        print("this car has a" +str(self.battery_size)+ "-KWH battery .")
        
my_tesla = ElectricCar('tesla',' model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
"""

class Restaurant():
    def __init__ (self, restaurant_name, cuisine_type):#神坑，这里左右都是两个下划线
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def descriable_restaurant(self):
        print(self.restaurant_name.title()  +"是一家" + self.cuisine_type)
        
    def open_restaurant(self):
        print("餐馆正常营业，欢迎新老顾客过来品尝")
           
class IceCreamStand(Restaurant):
    
    def __init__(self,restaurant_name,cuisine_type):
        
        super().__init__(restaurant_name, cuisine_type) 
        
        self.flavors_icecream = ["草莓","香蕉","菠萝"]
        
    def descriable_icecream(self):
         print("我们新出冰激凌的口味有 " + self.flavors_icecream)
        

my_restaurant = Restaurant('xixi','西餐店')
my_restaurant.descriable_restaurant()
my_restaurant.open_restaurant()
my_restaurant.descriable_icecream()







































































