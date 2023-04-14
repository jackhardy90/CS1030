print ('Jackson', 'Hardy')

cars = ['Ford', 'Chrysler' ,'Dodge', 'Ram' ,'Jeep', 'Chevy' ,'GMC']

print (cars)
print(len(cars))

cars.append('Buick')
print (cars)
print (cars[4])

cars.insert(3, 'Toyota')
print (cars)

cars.pop(5)
print(cars)

cars.sort()
print(cars)


cars.sort(reverse=True)
print(cars)

my_array_length = len(cars)
print(my_array_length)

array_string = 'The length of my array is'

print (array_string, my_array_length)