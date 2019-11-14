#coding:utf-8
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    def tomorrow(self):
        self.day +=1
    @staticmethod #静态方法
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))
    @classmethod #类方法
    def from_string(cls,date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return "---{year}/{month}/{day}---".format(year = self.year,month = self.month,day = self.day)
if __name__=="__main__":
    new_day = Date(2019,11,11)
    new_day.tomorrow()
    print(new_day)
    #2019-11-11
    date_str = "2019-11-11"
    new_day = Date.parse_from_string(date_str) #staticmethod 实例化
    print(new_day)
    new_day =Date.from_string(date_str) #classmethod 实例化
    print(new_day)
    print(dir(new_day))
