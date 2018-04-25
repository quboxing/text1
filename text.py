# from functools import wraps
# def zsq(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         print('111')
#         func(*args,**kwargs)
#     return wrapper
#
# @zsq
# def haha(a):
#     print(a)
# # haha('hehe')
# print(haha.__name__)
def a (b):

    print('haha')
    b(a)
def b(a):
    print('hehe')
    a(b)

a(b)
