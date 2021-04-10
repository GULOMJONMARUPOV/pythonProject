#03/13/21
#working with part of the list
# cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
# for car in cars:
#     print(f"the car is: {car}")

#*** slice of the list list_name[start:stops] start is iclusive, stop is exclusive
#*** values:list_name[start], list_name[starts +1], ....list_name[stop -1]
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
for car in cars[1:2]:
    print(f"the car is: {car}")
print("-------second--------")
for car in cars[:3]:# the same thing as cars [0:3]
    print(f"the car is: {car}")

print("-------third--------")
for car in cars[:2]:# the same thing as cars [2:end of the list]
    print(f"the car is: {car}")

print("-------fourth--------")
for car in cars[:2:10]:# no index out of the range error
    print(f"the car is: {car}")
print("-------copying--------")
print("-------linking the 2 variable to the same value--------")
cars2  = cars
print(f"the car: {cars}")
print(f"the car2: {cars2}")
cars.append('bmw')
print(f"cars after update:{cars}")
print(f"cars2 after update:{cars2}")

#lists are can be modified(muatble)
#Tuples - data structure similar to list  but can not be modified(immutable)
cars_t=('bugatti', 'ferrari', 'porche','lexus')
print(f"first value is : {cars_t[0]}")
cars[0]='honda' # this is possible since cars is  the lsit data stucture
# cars_t[0] = 'honda' # this is not possible since the catrs_t is tuple
print(f"cars_t tuple{cars_t}")

cars_t = ('honda','ferrari','tesla' )
print(f"cars_t tuple: {cars_t}")
print(f"size of the tuple: {len(cars_t)}")