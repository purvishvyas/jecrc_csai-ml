Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
5=3
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
5+9
14
'hello'*5
'hellohellohellohellohello'
'duck'+'you'
'duckyou'
'duck' +'you'
'duckyou'
'duck '+'you'
'duck you'
'duck'+' you'
'duck you'
'duck'+''+'you'
'duckyou'
'duck'+' '+'you'
'duck you'
import keyword
keyword.kwlist{}
SyntaxError: invalid syntax
SyntaxError: invalid syntaxkeyword.kwlist
SyntaxError: invalid syntax
keyword.kwlist()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    keyword.kwlist()
TypeError: 'list' object is not callable
import keyword
keyword.kwlist()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    keyword.kwlist()
TypeError: 'list' object is not callable
import keyword
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
len(keyword.kwlist)
35
-='vyas'
SyntaxError: invalid syntax
_='vyas'
print(_)
vyas
#a=bkl
#a=comment
'''sdyagfkjgsatfkjg'''
'sdyagfkjgsatfkjg'
"""hufgusftyet"""
'hufgusftyet'
a,b,c=10,20,50
print(a)
10
print(c)
50
d=f=g=69
print(g)
69
x *=6
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    x *=6
NameError: name 'x' is not defined
x=6
x*=3
print(x)
18
6*9
54
boolean 9!=5
SyntaxError: invalid syntax
5**2
25
5<52
True
6>58
False
#lofic gate
#logic gate
2<5 and 25<100
True
2>5 or 25<100
True
2>5 and 25<100
False
2>4 or 25>100
False
a=5
type (a)
<class 'int'>
b=5.5
type()b
SyntaxError: invalid syntax
b=5.5
type(b)
<class 'float'>
c=1+5j
type(c)
<class 'complex'>
my_list=[12,'abc',2,3]
type(my_list)
<class 'list'>
a=(65,gg,6.6)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a=(65,gg,6.6)
NameError: name 'gg' is not defined. Did you mean: 'g'?
typea=(12,'gg'6.3)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a=(12,'gg',6.6)
type(a)
<class 'tuple'>
s=(name:'vyas',age:'18')
SyntaxError: invalid syntax
s=('name':'vyas','Age':'18')
SyntaxError: invalid syntax
s=('Name':'Vyas':'Age':18)
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax
s=('Name':'Vyas','Age':18)
SyntaxError: invalid syntax
s={'Name':'Vyas','Age':18}
type(s)
<class 'dict'>
bool(True)
True
bool(False)
False
False
False
a='Hello World!'
print(a)
Hello World!
a[0]
'H'
a[11]
'!'
a[-1]
'!'
a[-6]
'W'
a[18]
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a[18]
IndexError: string index out of range
a[-18]
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a[-18]
IndexError: string index out of range
#above ex is of indexing
a='hello world'
a[0:2]
'he'
a[1:5]
'ello'
i[1:8:2]
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    i[1:8:2]
NameError: name 'i' is not defined. Did you mean: 'id'?
a[1:8:2]
'el o'
a[:4]
'hell'
a[:5:1]
'hello'
a[:8:3]
'hlw'
a[-2:-12:-1]
'lrow olleh'
'lrow olleh'
'lrow olleh'
a[-1::-9]
'de'
a[-1:-9:]
''
a[-3:-8:-1]
'row o'
a[-7:-9:-1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a[-8:-6]
'lo'
a.capitalized()
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    a.capitalized()
AttributeError: 'str' object has no attribute 'capitalized'. Did you mean: 'capitalize'?
a='hello world'
a.capitalized
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a.capitalized
AttributeError: 'str' object has no attribute 'capitalized'. Did you mean: 'capitalize'?
a.capitalized()
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    a.capitalized()
AttributeError: 'str' object has no attribute 'capitalized'. Did you mean: 'capitalize'?
a.capitalize()
'Hello world'
a.title()
'Hello World'
a.center{50}
SyntaxError: invalid syntax
a.center()
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a.center()
TypeError: center expected at least 1 argument, got 0
a.center(20)
'    hello world     '
a.center(25,'duck')
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a.center(25,'duck')
TypeError: The fill character must be exactly one character long
a.center(25,'%')
'%%%%%%%hello world%%%%%%%'
a.count(4)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    a.count(4)
TypeError: must be str, not int
a.count('4')
0
a.lstrip(25)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    a.lstrip(25)
TypeError: lstrip arg must be None or str
a.lstrip()
'hello world'
a=a.center(25)
a
'       hello world       '
a.lstrip()
'hello world       '
a.rstrip()
'       hello world'
a.strip()
'hello world'
a.upper()
'       HELLO WORLD       '
a.lupper()
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    a.lupper()
AttributeError: 'str' object has no attribute 'lupper'. Did you mean: 'upper'?
a=a.upper()
a
'       HELLO WORLD       '
a.supper()
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    a.supper()
AttributeError: 'str' object has no attribute 'supper'. Did you mean: 'isupper'?
a.isuppera90
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    a.isuppera90
AttributeError: 'str' object has no attribute 'isuppera90'. Did you mean: 'isupper'?
a.isupper()
True
c='abc@gmail.com'
c.split('@')
['abc', 'gmail.com']
c=c.split('@')
c
['abc', 'gmail.com']
'@'.join(c)
'abc@gmail.com'

m=[12,'duck',15,2.2]
m[1:4]
['duck', 15, 2.2]
'duck' in m
True
'15' in m
False
15 in m
True
14 in m
False
3*m
[12, 'duck', 15, 2.2, 12, 'duck', 15, 2.2, 12, 'duck', 15, 2.2]
m=+['new val']
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    m=+['new val']
TypeError: bad operand type for unary +: 'list'
m+=['new val']
m
[12, 'duck', 15, 2.2, 'new val']
m+=['suck']
m
[12, 'duck', 15, 2.2, 'new val', 'suck']
#cant give 2 values
but
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    but
NameError: name 'but' is not defined
#but
m.extend(['x','y'])
m
[12, 'duck', 15, 2.2, 'new val', 'suck', 'x', 'y']
m.insert(3,'padhle')
>>> m
[12, 'duck', 15, 'padhle', 2.2, 'new val', 'suck', 'x', 'y']
>>> m.pop()
'y'
>>> m
[12, 'duck', 15, 'padhle', 2.2, 'new val', 'suck', 'x']
>>> h
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    h
NameError: name 'h' is not defined
>>> m.pop(4)
2.2
>>> m
[12, 'duck', 15, 'padhle', 'new val', 'suck', 'x']
>>> m.clear()
>>> m
[]
>>> []
[]
>>> a=25,2.6,'agd'
>>> type()a
SyntaxError: invalid syntax
>>> type(a)
<class 'tuple'>
>>> r=12,25,48325
>>> type(r)
<class 'tuple'>
>>> r={12,25,48325}
>>> type(r)
<class 'set'>
>>> r={12,25,48325,'dshjahsgd'}
>>> type(r)
<class 'set'>
>>> r={12,25,48325,(5,'sdgsyag',2.58)'dshjahsgd'}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> r={12,25,48325,(5,'sdgsyag',2.58),'dshjahsgd'}
>>> type(e)
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    type(e)
NameError: name 'e' is not defined
>>> type(r)
<class 'set'>
>>> r=(12,25,48325,(5,'sdgsyag',2.58),'dshjahsgd')
>>> type(r)
<class 'tuple'>
>>> r[3]
(5, 'sdgsyag', 2.58)
