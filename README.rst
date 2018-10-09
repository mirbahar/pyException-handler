# pyException-handler
Python Exception Handler Package

Installation
============
Configuration
-------
from ExceptionHandler import *

Step two:
--------
using:
------
using for Special Character Check:
---------------------------------

try:
    print(specialCharacterCheck('Rahat@!'))
except Exception as e:
    print ("Exception Reson:",e.message)

using for Number Check: 
-----------------------

try:
    print(specialCharacterCheck('Rahat@!'))
except Exception as e:
    print ("Exception Reson:",e.message)
    
example LINK: 
============
https://github.com/mirbahar/pyException-handler/blob/master/example.py

List:
=====
Special Character : ['@','!', '$', '~', '&', '#']
Number List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
