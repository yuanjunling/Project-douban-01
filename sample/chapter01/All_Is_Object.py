def ask(name):
    print(name)

# my_func = ask
# my_func("bobby")
class Person:
    def __init__(self):
        print("bobby")
def decor():
    print("dec start")
    return ask
dec_01 = decor()
dec_01("jhj")

# obj_list = []
# obj_list.append(ask)
# obj_list.append(Person)
# for item in obj_list:
#     print(item())
print(Person.__bases__)
