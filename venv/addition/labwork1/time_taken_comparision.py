# You live 4 miles from university.The bus drives at 25 mph but spends 2 munites at each of the stop on the way. How
# long will the bus journey take? Alternatively you could run to the university. You jog the first mile at 7mph, then
# run the next two at 15 mph, before jogging the last at 7mph again .Will this be quicker or slower than the bus ?

Dis=int(input("enter the distance of the university from your house: " ))
time_taken_bus1=Dis/25
time_taken_at_stop=2*10
time_taken_bus2 = (time_taken_bus1*60) + time_taken_at_stop
print(f"The bus takes {time_taken_bus2} minutes to reach the university ")

first_mile=(1/7)*60
next_two_miles=(2/15)*60
last_mile=(1/7)*60
time_taken_jog = first_mile + next_two_miles + last_mile
print(f"The time taken to reach the university by jogging is {time_taken_jog} minutes")

if time_taken_bus2>time_taken_jog :
    print("Jogging to university is faster")

elif time_taken_bus2<time_taken_jog :
    print("Taking the bus is faster")

elif time_taken_bus2==time_taken_bus2:
    print("It takes the same time to reach the university")