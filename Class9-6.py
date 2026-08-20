# 9-6
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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Ice_Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print(self.restaurant_name + " has following flavors ice creams: ")
        for flavor in self.flavors:
            print("- " + flavor)


restaurant1 = Restaurant("MaLiuJi", "SiChuan")
# 创建IceCreamStand实例
my_ice_cream_stand = IceCreamStand("Sweet Treats")

# 添加一些口味
my_ice_cream_stand.flavors = ["vanilla", "chocolate", "strawberry", "mint"]

# 调用显示口味的方法
my_ice_cream_stand.show_flavors()

# 也可以调用继承来的方法
my_ice_cream_stand.describe_restaurant()
print("---------以下是9-7, 9-8----------")

# 9-7
# 9-8
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


class Privileges():
    def __init__(self, privileges=None):
        # 修正：使用传入的参数，如果没有传入则使用默认值
        # 你的原始代码里Privileges类的 __init__方法接受了一个 privileges参数却没有使用它
        # 而是直接硬编码了列表。这样当你想要自定义权限列表时就无法实现。
        if privileges is None:
            self.privileges = ["can add post", "can delete post", "can ban user"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("Admin includes these privileges: ")
        for privilege in self.privileges:
            print("- " + privilege)


#class Admin(User):
 #   def __init__(self, first_name, last_name, age, gender, login_attempts):
#        super().__init__(first_name, last_name, age, gender, login_attempts)
 #       self.privilege = Privileges()


# 如果走class Privileges的else分支，需要该定义代码

class Admin(User):
    def __init__(self, first_name, last_name, age, gender, login_attempts,
                 privileges=None):  # ✅ 新增参数
        super().__init__(first_name, last_name, age, gender, login_attempts)
        # 9-8，在Admin类中，将一个Privileges实例用作其属性。P150，9.3.5
        self.privilege = Privileges(privileges)  # ✅ 传入

    def show_admin_privileges(self):
        """在Admin类中封装方法，自动传入管理员名称"""
        full_name = self.first_name + " " + self.last_name
        self.privilege.show_privileges(full_name)

user1 = User("Lei", "Li", 26, "Male", 10)
admin1 = Admin("admin", "Admin", 30, "Male", 100)
admin1.privilege.show_privileges()

# 创建自定义权限列表
my_privileges = ["can add post", "can delete post", "can ban user",
                 "can view reports", "can manage settings"]

# 为了走else分支。创建Admin实例，传入自定义权限
# 只在这里加my_privileges实参，运行会报错，说它是意外实参
# 因为class Admin(User)中没有定义my_privileges参数，需要加上
admin1 = Admin("Zhang", "Wei", 35, "Male", 200, my_privileges)

# 调用show_privileges()方法，此时会走else分支
admin1.privilege.show_privileges()
print("---------以下是9-9----------")

# 9-9
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
        else:
            print("The battery size is " + str(self.battery_size) + ".")


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性，再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()  # 使用默认电瓶容量70


# 创建一辆电瓶容量为默认值的电动汽车
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# 第一次调用get_range()
print("\nBefore upgrade:")
my_tesla.battery.get_range()

# 对电瓶进行升级
print("\nUpgrading battery...")
my_tesla.battery.upgrade_battery()

# 再次调用get_range()
print("\nAfter upgrade:")
my_tesla.battery.get_range()