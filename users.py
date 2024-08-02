# Python Crash Course Book 

class User:
    def __init__(self, f_name, l_name, age, major):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.major = major

    def describe_user(self):
        print(f'Name: {self.f_name} {self.l_name}, Age: {self.age}, Major: {self.major}')

    def greet_user(self):
        print(f'Hello {self.f_name} {self.l_name}!!')

u1 = User('Arwa','Mohammed', 22, 'CYS')
u2 = User('Maria','Ali', 25, 'AI')
u3 = User('Kawther','Saleh', 20, 'CS')

u1.describe_user()
u1.greet_user()

u2.describe_user()
u2.greet_user()

u3.describe_user()
u3.greet_user()


