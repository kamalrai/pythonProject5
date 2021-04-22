#If temerature is greater than 30, it's a hot day otherwise if less than 10 ;its a cold day; otherwise its neither cold
#nor hot
temp=int(input("enter the temperature : "))
if temp<=10 :
    print("it's a cold day")
elif temp >= 30 :
    print("it's a hot day")
else:
    print("its neither hot nor cold")
