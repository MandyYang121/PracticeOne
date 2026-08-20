# 9-1
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The " + self.restaurant_name + " is a " + self.cuisine_type + " type restaurant.")

    def open_restaurant(self):
        print(self.restaurant_name + " is open.")

# 9-1, 9-2


restaurant1 = Restaurant("MaLiuJi", "SiChuan")
restaurant2 = Restaurant("ErShiChuFang", "Russia")
restaurant3 = Restaurant("CunShangYiWu", "Japanese")
print("I like " + restaurant1.restaurant_name +
      "restaurant. It is a " + restaurant1.cuisine_type + " type restaurant.")
restaurant2.describe_restaurant()
restaurant3.open_restaurant()
print("--------以下是9-3---------")

# 9-3


class User():
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print("This " + self.gender + " " + self.first_name + " "
              + self.last_name + "'s age is " + str(self.age) + ".")

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name + "!")


user1 = User("Lei", "Li", 26, "Male")
user2 = User("Meimei", "Han", 25, "Female")

user1.describe_user()
user2.greet_user()
print("-------以下是9-4 --------")
# 9-4


class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The " + self.restaurant_name + " is a " + self.cuisine_type + " type restaurant.")

    def open_restaurant(self):
        print(self.restaurant_name + " is open.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, numbers):
        self.number_served += numbers


restaurant1 = Restaurant("MaLiuJi", "SiChuan")
print("I like " + restaurant1.restaurant_name +
      "restaurant. It is a " + restaurant1.cuisine_type
      + " type restaurant, it served " + str(restaurant1.number_served) + " people.")
restaurant1.set_number_served(500)
# 也可以把下面这两个Print语句写一个read_number()方法，如P144页标记2
print("Now, it saved " + str(restaurant1.number_served) + " people.")
restaurant1.increment_number_served(100)
print("Now, it saved " + str(restaurant1.number_served) + " people.")
print("---------以下是9-5----------")

# 9-5


class User():
    def __init__(self, first_name, last_name, age, gender, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = login_attempts

    def describe_user(self):
        print("This " + self.gender + " " + self.first_name + " "
              + self.last_name + "'s age is " + str(self.age)
              + ", login the system " + str(self.login_attempts) + " times.")

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name + "!")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Lei", "Li", 26, "Male", 10)
# 登录三次
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.describe_user()
# 重置登录次数
user1.reset_login_attempts()
user1.describe_user()

