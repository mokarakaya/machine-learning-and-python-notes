



def sub_method(a,b,c):
    print('this should not be called.')
    return c

def method_under_test():
    print('this should be called.')
    return sub_method('somestring', 1, 120) + 1


