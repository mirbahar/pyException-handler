from ExceptionHandler import *

# test for special character check Exception
try:
    print(specialCharacterCheck('Rahat@!'))
except Exception as e:
    print ("Exception Reson:",e.message)

#test for number check Exception
try:
    print(numberExceptionCheck('Raha12t@!'))
except Exception as e:
    print ("Exception Reson:",e.message)
