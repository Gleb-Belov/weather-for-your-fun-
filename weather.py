#First we import pyowm and colorama
import pyowm
from colorama import init
from colorama import Fore, Back, Style
#it helps the colorama to work properly
init()

#Here we color the background

print( Back.GREEN )

#Here is a greeting

print('Hi , i am the developer of this application! ')
#And here we can set a password for the fun
p = input('What do you want?You can:\n set password(1) \n enter the application(2): ')

y = input('Set password!: ')
if y == 'pass1':
	print( Back.BLUE )

#Here we write api

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc' , language = "en")

print( Back.BLUE )

#Here we ask in which city

place = input('Write your city: ')

#Commands for PyOwm

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]
    
print( "in " + place + " now " + w.get_detailed_status())
print( "Temperature is now " + str(temp) + ("°С"))

print( Back.BLACK )

#Here we recommend how to get dressed

if temp < 0:
	print( Fore.BLUE )
	print("It's cold, put on your jacket! ")
elif temp < 10:
	print( Fore.CYAN )
	print("Now it's not very cold, but better put a hat!")
elif temp < 20:
	print( Fore.YELLOW )
	print("Now it's normal , you can dress as you like :)")
elif temp > 21:
	print( Fore.MAGENTA )
	print("it's hot now , don't go out without panama, because it will be a sunny blow!")
