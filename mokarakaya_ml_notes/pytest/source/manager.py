def sub_method(a, b, c):
    print("this should not be called.")
    return c


def method_under_test():
    print("this should be called.")
    return sub_method("somestring", 1, 120) + 1


def add(var1, var2):
    return var1 + var2


def add_to_manager(my_manager):
    return my_manager.get_test_value() + 1


def failure():
    raise ValueError("error")


class Manager:
    def __init__(self, test_value):
        self.test_value = test_value

    def get_test_value(self):
        print("this should not be called")
        return self.test_value
