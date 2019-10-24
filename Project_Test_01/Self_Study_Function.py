data = [1,2,3,4,5,6]
print(data[0])
data={}
data['error'] = 'data'
data['int'] = 'int'
print(data['error'])

name = list('Perl')
print(name)
name[2:] = list('br')
print(name)

names = ['aa','bb','cc','dd']
print(names.index('aa'))

names.insert(2,'ter')
print(names)
url = "http://www.{0}baidu{1}.com"
print(url.format('baidu','qidian'))
formats = "The numble is{num:e}".format(num=43)
# The = "The Middle by jimmy Eat World".center(39,"*")
The = "The Middle by jimmy Eat World"
print(The)
print(The.find('Middle'))

seq = ['1','2','3','4','5']
sep = '+'

print(sep.join(seq))

dirs = '','usr','bin','env'

print('C:'+'/'.join(dirs))
a = "that s all folks".title()
print(a)

#replace查找并替换

b = {}.fromkeys(['name','age'],'unknown')
print(b)
def recursion():
    return recursion()