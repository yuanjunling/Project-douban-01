class Company(object):
    def __init__(self,employee_list):
        self.emp = employee_list
    def __getitem__(self, item):
        return self.emp[item]

company1 = Company(["tom","boo","jane"])

for em in company1:
    print(em)