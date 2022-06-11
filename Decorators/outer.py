import functools

def outer(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        print("Before")
        return func(*args,**kwargs)
    return inner

@outer
def hi():
    print("Hi Hannah")

@outer
def hiName(name):
    print("Hello {0}".format(name))


if __name__ == '__main__':
   # h = outer(hi)
   # h()
   hi()
   hiName("Hannah")
   print(hi.__name__)

# def outer(func):
#     def inner():
#         print('Before func()..')
#         func()
#         print('After func()..')
#     return inner
#
#
# def hi():
#     print('Hi World')
#
#
# h = outer(hi)
# h()