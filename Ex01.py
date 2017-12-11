#http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

import datetime

TARGET_AGE = 100
name = raw_input("Give me your name: ")
age = raw_input("Give me your age: ")
diff = TARGET_AGE - int(age)
thisYear = datetime.datetime.now().year
output = name
if diff >= 0:
    output += ", you will be " + str(TARGET_AGE) + " old in " + str(thisYear + diff)
else:
    output += ", you were " + str(TARGET_AGE) + " years old in " + str(thisYear + diff)

for x in range(0, int(raw_input("Enter a number:"))):
    print(output)

