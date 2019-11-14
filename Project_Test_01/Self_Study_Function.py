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
print("a:",a)

#replace查找并替换

b = {}.fromkeys(['name','age','sex'],None)
print('b:',b)
def recursion():
    return recursion()

tag = "Python web site"
print('tag: ',tag[0:2])
print('python '*5)
lst = [1,2,3,4,5]
lst.append(6)
print('lst: ',lst)

sss = ['1','2','3','4','5']
sss1 = '+'
s = sss1.join(sss)
print(s)

d = {'x':1,'y':2,'a':3}
print(d.popitem())

a = y = 'aaaaa'
print(a)
print(y)

def fibs(num):
    result = [0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result


print('fibs: ',fibs(10))


def squarc(x):
    "我是文档注释"
    return x*x

print(squarc.__doc__)
print(squarc.__name__)
print(squarc.__call__)
print(squarc.__class__)

def hello1(greeting=None,*name):
    print('{},{}'.format(greeting,name))


print(hello1('AAAA','BBBB','asdasd','asdas'))





class SomeCustomException(Exception):
    pass

try:
    def error(num):
        return num
except SomeCustomException as e:
    print(e)


print(error('AAAA'))
print('python一切皆对象')