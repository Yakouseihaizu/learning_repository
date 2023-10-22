import re

class Note:
    def __init__(self) -> None:
        self.next = None
        self.data = None

    def push(self,data):
        new = Note()
        new.data = data
        new.next = self.next
        self.next = new
    
    def pop(self):
        if self.next:
            result = self.next
            self.next = self.next.next
            return result
        else:
            return None
    
    def is_empty(self):
        if self.next == None:
            return True
        else:
            return False
    def print_stark(self):
        p = self.next
        while p :
            print(p.data,end=' ')
            p = p.next
        print()

def calculate(cal,num1,num2):
    print(num1+cal+num2,end='')
    num1 = int(num1)
    num2 = int(num2)
    if cal == '+':
        result = num1+num2
    elif cal == '*':
        result =  num1*num2
    elif cal =='/':
        result =  num1/num2
    elif cal == '-':
        result = num1-num2
    print('='+str(result))
    return str(result)

def cal(c,head_c,head_n):
    if c == '(':
        head_c.push(c)
    elif c == ')':
        while head_c.next and head_c.next.data !='(':
            num1 = head_n.pop().data
            num2 = head_n.pop().data
            num1 = calculate(head_c.pop().data,num1,num2)
            head_n.push(num1)
        head_c.pop()
    elif c in '+-' and head_c.next and head_c.next.data in '*/':
        while head_c.next and head_c.next.data not in  '+-' :
            num1 = head_n.pop().data
            num2 = head_n.pop().data
            num1 = calculate(head_c.pop().data,num1,num2)
            head_n.push(num1)
        head_c.push(c)
        head_n.push(n_list.pop())

    else:
        head_c.push(c)
        head_n.push(n_list.pop(0))

head_c = Note()
head_n = Note()
exp = input('Enter your expression:\n')
# TODO: 从前往后读
regex = re.compile(r'[()*+-/]')
c_list = regex.findall(exp)
tn_list = regex.sub(' ',exp)
tn_list  = list(tn_list.split(' '))
n_list = []
for tn in tn_list:
    if tn and tn.isspace() == False:
        n_list.append(tn)

# TODO: 遇到前括号入栈，遇到后括号出栈
head_n.push(n_list.pop(0))
for c in c_list:

    print('head_c: ',end='')
    head_c.print_stark()
    print('head_n: ',end='')
    head_n.print_stark()
    
    cal(c,head_c,head_n)

num2 = head_n.pop().data
print('ending')
while not head_c.is_empty() and not head_n.is_empty():
    cal = head_c.pop().data
    num1 = head_n.pop().data
    num2 = calculate(cal,num1,num2)
    head_n.push(num2)
    num2 = head_n.pop().data
print(num2)