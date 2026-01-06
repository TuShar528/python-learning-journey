#common inputs

driver_name = input("Enter your name:")
print(driver_name)

#input

car_name = input("Enter your car name:")
print(car_name,"is Registered under",driver_name)

#type casting

speed = int(input("Speed of vehicle:"))
if(speed>80): print(car_name," is overspeeding")

#f-string(formatted)

print(f"{car_name} registered under {driver_name} speed is {speed}")
