Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def TableToList(table):
...     list = []
...     for row in table:
...         for item in row:
...             list.append(item)
...     return list
... 
>>> TableToList([[1,2,3],[7,8,9]])
[1, 2, 3, 7, 8, 9]
