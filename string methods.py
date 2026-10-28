Python 3.14.8 (tags/v3.14.8:8e6e75d, Sep 30 2026, 18:19:33) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a='python'
len(a)
6
a='python course'
len(a)
13
len(python)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    len(python)
NameError: name 'python' is not defined
len("python")
6
len("course")
6

#count
a="python course"
count (o)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count (o)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count(o)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.count(o)
NameError: name 'o' is not defined
count(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("t")
5

#find a string
a="python"
a.find a string("h")
SyntaxError: invalid syntax
a.find string("h")
SyntaxError: invalid syntax

#escape sequence
a="name\nmobileno:\tmailid\ncollege name\tbranch
SyntaxError: unterminated string literal (detected at line 1)
a="name\nmobileno:\tmailid\ncollege name\tbranch"
print(a)
name
mobileno:	mailid
college name	branch
a="name:pravallika\nmobileno:8919355847\tmailid:pravallikad32@gmail.com\ncollege name:sksd mahila kalasala\tbranch:b.com computers
SyntaxError: unterminated string literal (detected at line 1)
>>> a="name:pravallika\nmobileno:8919355847\tmailid:pravallikad31@gmail.com\ncollege name
SyntaxError: unterminated string literal (detected at line 1)
>>> a="name:pravallika\nmobile:8919355847\tmailid:pravallikad31@gmail.com\ncollege:sksd mahila kalasala\tbranch:b.com computers"
>>> print(a)
name:pravallika
mobile:8919355847	mailid:pravallikad31@gmail.com
college:sksd mahila kalasala	branch:b.com computers
>>> 
>>> #replace
>>> a="pravallisa
SyntaxError: unterminated string literal (detected at line 1)
>>> 

>>> 

... 
... 
>>> a="pravallisa"
>>> a.replace("s","k")
'pravallika'
>>> a="python java"
>>> a.replace("java","course")
'python course'
