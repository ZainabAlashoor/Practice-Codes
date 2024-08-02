# Python Crash Course Book 

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    
    def describe_res(self):
        print(f'{self.restaurant_name}, {self.cuisine_type}')

    def res_open(self):
        print(f'{self.restaurant_name} is now open!')


r1 = Restaurant('Tulip Restaurant', 'Eastern Food')
r2 = Restaurant('Kang Restaurant', 'Korean Food')
r3 = Restaurant('Jojo Restaurant', 'Indian Food')

#Calling methods
r1.describe_res()
r2.describe_res()
r3.describe_res()

r2.res_open()
    
