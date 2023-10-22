from copy import copy , deepcopy
from sys import getrefcount
# import random
# people = ['Alice','Bob','Carol','David']
# random.shuffle(people)
# print(people)

# spam = 43
# spam /=2
# print(spam)

# spam = 'Hello, '
# spam += 'world!'
# bacon = ['Zophie']
# bacon*=3
# print(bacon)

# del bacon[2]
# print(bacon)

# spam = ['hello','hi','howdy','heyas']
# result = spam.index('hello')
# result = spam.index('heyas')
# result = spam.index('howdy howdy howdy')
# spam = ['Zophie','Pooka','Fat-tail','Pooka']

# spam = ['cat','bat','rat','elephant']
# a = spam
# # spam.append('Moose')
# # spam.insert(1,'chicken')
# # spam.remove('dog')
# del spam
# result = a
# print(result)

# spam = [2,5,3,14,1,-7]
# spam.sort()
# spam = ['ants','Cats','dogs','badgers','elephants']
# print(sorted(spam,key=str.lower))
# print(spam)

# List = [[1,2,3],[3,5,2],[2,2,2],[1,1,4]]
# List.sort(key=lambda List: (List[0],List[2],List[1]))
# print(List)

# spam = 42
# cheese = spam
# spam = 100
# print(spam)
# print(cheese)

# cheese = spam
# cheese[1] = 'Hello!'
# print(spam)
# print(cheese)



# print(getrefcount(spam))
# spam1 = spam
# print(getrefcount(spam))

# a = str('Howdy')
# b = str('Howdy')
# print(id(a))
# print(id(b))
# print(id('Howdy'))
# del a,b
# print(id('Howdy'))
# print(getrefcount('Howdy'))
# a = 1000
# getrefcount(1000)
# print(getrefcount(1000))
# print(getrefcount('Howdy'))

# a = [1,2,[3,4]]
# b = copy(a)
# print(b)
# print(f"a and b value is same?   {a==b}")
# print(f"a and b identy is same?  {a is b}")
# c = deepcopy(a)
# print(c)
# print(f"a and c value is same?   {a==c}")
# print(f"a and c identy is same?  {a is c}")
# print(f"b and c value is same?   {b==c}")
# print(f"b and c identy is same?  {b is c}")
# print(f"\na[2] and b[2] identy is same?   {a[2] is b[2]}")
# print(f"a[2] and c[2] identy is same?  {a[2] is c[2]}")

# 结论：copy只进行简单的一次复制，对于其中列表的复制时引用的复制
#      deepcopy是对于完整的复制，对于其中的每一项都进行复制

a = 1000
num = getrefcount(a)
print(num)
# print(id(1000))
# print(id(a))