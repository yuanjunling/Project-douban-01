from sample.chapter04.class_method import Date
class User(object):
    def __init__(self,birthday):
        self.birthday = birthday
    def get_age(self):
        return 2019 - self.birthday.year
if __name__=="__main__":
    user = User(Date(1989,9,3))
    print(user.birthday)
    print(user.get_age())

