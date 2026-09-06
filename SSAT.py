#Input: Welcome message, crew member identification and values for the calculus. .✦ ݁˖

print("Hey! Welcome to SSAT (Suport System for Astronauts)! /ᐠ - ⩊ -マ₊˚⊹♡₊ ⊹ ")
users_name = input("Please, type your name:")
print("Please, provide the system with the following data:")
distance = input("𖹭.ᐟType the distance of the travel: ")
speed = input("𖹭.ᐟType the ship's speed: ")
destiny = input("𖹭.ᐟType the final destination: ")

#Processing: Values' convertion in hours/day for the output. .✦ ݁˖

distance = float(distance)
speed = float(speed)
result = (distance/speed)
total_hours = 24
result2 = (result/total_hours)

#Output: Results and goodbye message. .✦ ݁˖

print("Dear " +users_name+ ", SSAT has measured the estimated travel's time to", destiny,"~")
print(f"Considering the distance of",distance,"km/h, as well as the speed of",speed,"... the approximate")
print(f"hours of your travel is {result:.2f}, which equals to {result2:.2f} days!!! ദ്ദി/ᐠ - ⩊ -マ.ᐟ")
print("Have a wonderful journey throught the galaxy and enjoy the view! ฅ₍^˵◝ ⩊ ◜˵マⳊ")
