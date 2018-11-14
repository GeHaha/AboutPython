# -*- coding: utf-8 -*-
"""
Created on Tue May 29 13:47:22 2018

@author: Administrator
"""
"""
alien_0 = {'color':'green','points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

"""

"""
user_0 = {
    'username':'gehaha',
    'first':'ge'
    }
for key,value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
"""



"""
prompt = ("If you tell us who you are,we can personalize the message you see.")
prompt =prompt+("\nwhat is you first name?")

name = input(prompt)
print("\nHello,"+name+"!")
"""
"""
height = input("how tall are you,in inches?")
height = int(height)
if height >=36:
    print("\nyou're tall enough to ride!")
else:
    print("\nyou'll be able to ride when you're a little older.")
        
"""
"""
number = input("Enter a number,and I'll tell you if it's even or add:")

number = int(number)
if number % 2 == 0:
    print("\nThe number" +str(number)+"is even.")
else:
    print("\nThe number" +str(number)+"is odd.")

"""
"""
rent_car =input("请问你想租赁什么样的车：")

print("\nLet me see if I can find you a Subaru")

"""
"""
number =input("how many people to eat?")
number =int(number)
if number > 8:
    print("sorry,there are no seat for you ")
else:
    print("wlcome to our restraunt")

"""
"""
prompt =("\nPlease entry the name of a city you have visited : ")
prompt +=("\n(enter 'quite'when you are finished.)")
while True:
    city = input(prompt)
    if city ==('quit'):
        break
    else:
        print("I'd love to go to " + city.title() +"!")
        
"""
"""

unconfirmed_users =['alice','brain','candace']
confirmed_users =[]

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: "+current_user.title())
    confirmed_users.append(current_user)
print("\nThe following uers have been confirmed:")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())

"""

"""
responses ={}
polling_active = True
while polling_active:
    name = input("\nWhat is you name?")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat ==("no"):
        polling_active =False
print("\n-----Poll Results----")
for namr,response in responses.items():
    print(name+"would like to climb "+response +".")
"""

""'
sandwich_orders = ["egg","vetebeast","meat","fish","chicken"]
finished_sandwich = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print("I made you " +sandwich_order +" sandwich.")
    finished_sandwich.append(sandwich_order)
print("\n The following finished sandwich ：")
for finished_sandwiche in sandwich_order:
    print(finished_sandwiche.title())




















































