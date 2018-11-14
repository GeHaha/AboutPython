# -*- coding: utf-8 -*-
"""
Created on Tue May 29 20:47:19 2018

@author: Administrator
"""
"""
def display_message():
  
    print("本章学习的是函数的定义")
"""
"""
def favorite_book(bookname):
    print("One of my favorite book is "+bookname.title()+".")
"""   

"""
def describe_pet(animal_type, pet_name):
    print("\nI have a" +animal_type+".")
    print("My"+animal_type +"'s name is" +pet_name.title()+".")
"""
"""
def make_shirt(shirt_size,shirt_type):
    print("the shirt size is"+ shirt_size,"shirt stye is"+shirt_type+"." )
    
"""


"""
def get_formatted_name(first_name,last_name):
    full_name = first_name +' '+last_name
    return full_name.title()
musician = get_formatted_name("jimi","hendrix") 
print(musician)
 
"""
"""
def build_person(first_name,last_name):
    person ={'first':first_name,'last':last_name}
    return person
musician = build_person('jimi','hendrix')
print(musician)

"""
"""
def get_formatted_name(first_name,last_name):
    full_name =first_name + ' '+ last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name ==('q'):
        break
    l_name = input("Last name : ")
    if l_name =='q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, " +formatted_name +"!")

"""
"""
def city_country(city_name,country_name):
    full_name =( city_name + ","+country_name)
    return full_name.title()
        
while True:
    print("\n tell me you city ")
    print("\n enter'q' at any time to quit")
    c_name = input("city name :")
    if c_name ==("q"):
        break
    co_name = input("country name :")
    if co_name ==("q"):
        break
    city_countrys =city_country(c_name,co_name)
    print("\nHello ,welcom to " +city_countrys +"!")

"""
"""
def make_album(singer_name,album_name):
    information ={"name" : singer_name,"album" : album_name}
    return information

album_information = make_album("chenyixun","hongmeigui")
print(album_information)
"""
"""
def greet_users(names):
    for name in names:
        msg = ("Hello," +name.title() + "!")
        print(msg)

usernames =['hanna','ty','margot']
greet_users(usernames)

"""
"""
unprinted_designs = ['ipone case','robot pendant','dodecahedron']
completed_models = []

while unprinted_designs:
    
    current_design = unprinted_designs.pop()
    print("Printing model :" + current_design)
    completed_models.append(current_design)
    
print("\nThe following models have been printed :")
for completed_model in completed_models:
    print(completed_model)

"""
"""
def print_models(unprinted_designs,completed_models):
    
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model:"+ current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    
   
    print("\nThe following models have been printed :")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


"""

 

magicians_names = ['david','hahaha','henghengheng','xixixi']
show_magicians = []
while magicians_names:
    magicians_name = magicians_names.pop()
    print("printing names :" + magicians_name)
    
    show_magicians.append(magicians_name)   
make_great = ("the great ")    
show_magicians = make_great +   magicians_name
print(show_magicians)
    













































