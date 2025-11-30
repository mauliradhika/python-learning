# Base class
class Chef:
    def make_chicken(self):
        print("The chef makes chicken")

    def make_salad(self):
        print("The chef makes salad")

    def make_special_dish(self):
        print("The chef makes BBQ ribs")


# Child class (inherits from Chef)
class ChineseChef(Chef):
    def make_fried_rice(self):
        print("The chef makes fried rice")

    def make_special_dish(self):
        print("The chef makes orange chicken")


# Using classes
chef = Chef()
chef.make_special_dish()

chinese_chef = ChineseChef()
chinese_chef.make_special_dish()
chinese_chef.make_fried_rice()
