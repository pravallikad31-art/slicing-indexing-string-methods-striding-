Python 3.14.8 (tags/v3.14.8:8e6e75d, Sep 30 2026, 18:19:33) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string mrhoids
#upper()
a="code"
a="code"
a.upper()
'CODE'
b= "python"
b.upper()
'PYTHON'
#lower()
c="HELLO"
c. lower()
'hello'
d="HI"
d.lower()
'hi'
a="pthon"
a.upper("p")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.upper("p")
TypeError: str.upper() takes no arguments (1 given)
a[0] .upper()
'P'
#capitalize
a.capitalize()
'Pthon'
b="python course"
b.little()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b.little()
AttributeError: 'str' object has no attribute 'little'. Did you mean: 'title'?
b.title()
'Python Course'
c="i am in class"
c.title()
'I Am In Class'
c.capitalize()
'I am in class'
a="hello"
a.isupper()
False
a.isalpha()
True
b="hello world"
b.isalpha()
False
c="helloworld"
c.isalpha()
True
a.isdigit()
False
b=12345
b.isdigit()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    b.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
c="12345"
c.isdigit()
True
a="python course"
a.startswityh("p")
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.startswityh("p")
AttributeError: 'str' object has no attribute 'startswityh'. Did you mean: 'startswith'?
a.startswith("p")
True
a.endswith('e")
           
SyntaxError: unterminated string literal (detected at line 1)
a.endswith("e")
True
b="pyhton COURSE"
b.isupper()
False
c="pravallika1202
SyntaxError: unterminated string literal (detected at line 1)
c="pravallika1202"
c.isalnum()
True
#strip()
#estrip(),lstrip()
a="       pappu        "
a.strip()
'pappu'
a.rstrip()
'       pappu'
a.lstrip()
'pappu        '
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am learing python"
b.split()
['i', 'am', 'learing', 'python']
c=b.split()

c
['i', 'am', 'learing', 'python']
c[1].upper()
'AM'
#join()
a="apple","banana","grapes"
"".join(a)
'applebananagrapes'
" ".join(a)
'apple banana grapes'
"k".join(a)
'applekbananakgrapes'
b="hello"
"k".join(b)
'hkeklklko'
#concatenation()
a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="course"
print(a+b)
pythoncourse
print(a""+b)
SyntaxError: invalid syntax
print(""+b)
course
print(a""+b)
SyntaxError: invalid syntax
print+""+b)
SyntaxError: unmatched ')'
printa+""+b)
SyntaxError: unmatched ')'
print(a+""+b)
pythoncourse
fname="pravallika"
lname="dodda"
print(fname=lname)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    print(fname=lname)
TypeError: print() got an unexpected keyword argument 'fname'
print(fname+lname)
pravallikadodda
print(fname+" "+lname)
pravallika dodda
print(fname.tittle()+" "+lname.tittle())
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    print(fname.tittle()+" "+lname.tittle())
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
print (fname.tittle()+" "+lname.tittle())
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    print (fname.tittle()+" "+lname.tittle())
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
print (fname. tittle()+" "+lname. tittle())
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    print (fname. tittle()+" "+lname. tittle())
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?

#formatting
a=5
b=7
print(a+b)
12
print("the sum is",a+b)
the sum is 12
print("the sum is a+b")
the sum is a+b
>>> city="vja"
>>> print("city is",city)
city is vja
>>> a="motu"
>>> b="pathlu"
>>> #format()
>>> print("hello {}{}".format(a,b))
hello motupathlu
>>> print("hello {} {}".format(a,b))
hello motu pathlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello pathlu
>>> #fstring
>>> a="sweety"
>>> b="cuty"
>>> print(f"hello {a} {b}")
hello sweety cuty
>>> print(f"hello {a}{b}
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"hello {a}{b}")
hello sweetycuty
>>> print(f"hello {a} hello {b}")
hello sweety hello cuty
