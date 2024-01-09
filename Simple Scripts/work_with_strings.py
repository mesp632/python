#make a python string using '' and ""
print("string using single quotes: 'string' in single quotes")
print("string using 3 single quotes: '''string''' in 3 single quotes")
print("string using 2 double quotes: \"\"string\"\" in 3 single quotes")
print("string using double quotes:", "string")

#build string example
kittysound = "meow"
basesound = ""
basesound += "cats make the sound: "
basesound += kittysound
print(basesound)

#convert data types to string and using escape with \
print("converting data types to strings:", str(127),"\\", str(1.5e3),"\t\n", str(True))
#combine strings
print("a" + "b")
duplicatestrings = 'bye ' * 3 #prints bye 3 times
print(duplicatestrings)

teststring = 'teststring'
print("print the 4th letter of \"teststring:\"",teststring[3])

changeword = 'Round'
print("Original Word:", changeword)
print("New Word:",changeword.replace('R','P'))
print("Other way to change word:", 'P'+changeword[1:])
print("Prove original word immutable:", changeword)
print("extract substring:", changeword[2:5:2])#start at offset 2 go to offset 8 skip every 2 letters
print("exctract the last 3 letters:",changeword[-3:])
print("exctract from string",changeword[2:-1])
print("get length of string",len(changeword))
commalist = 'String 1, String 2, String 3'
newcommalist = commalist.split(",")
print("split list using comma delimiter",newcommalist)
print("split lit using space delimieter",commalist.split())
newlinecommalist = "string 1\n string 2\n string 3"
print("split lit using newline delimieter",newlinecommalist.splitlines())

print("joinlist:", ",".join(newcommalist))
print("use startswith() function:", commalist.startswith('String'))
print("use endsswith() function:", commalist.endswith('3'))
print("use find() function:", commalist.find('String'))
print("use rfind() function:", commalist.rfind('String')) #finds next occurance of 'string'
print("use count() function:", commalist.count('String'))
print("use isallnum() function:", commalist.isalnum())
 #strip() removes list of words from the beginning and end of string only
print("use strip() to remove ends until only 2 remains:", commalist.strip('String 1 , 3'))
print("use replace() to remove commas:",commalist.replace(',','')) #can replace in the middle of the string
print("capitalize first word:",commalist.capitalize())
print("capitalize all words:",commalist.title())
print("Capitalize all letters:", commalist.upper())
print("Lowercase all letters:", commalist.lower())
print("Swap cases:", commalist.swapcase())
print("Center string with 20 spaces: \n",commalist.center(20))
print("Left jusify string: \n",commalist.ljust(20))
print("Right jusify string: \n",commalist.rjust(20))
print("use replace() to remove 1 comma:\n",commalist.replace(',','',1)) #can replace in the middle of the string
print("use replace() to replace i with o:\n",commalist.replace('i','o',1)) #can replace in the middle of the string
seconds = 60
minutes = 60
seconds_per_hour = seconds * minutes
print("caluclate seconds in an hour =", seconds_per_hour)
hours = 24
seconds_per_day = seconds_per_hour * hours
print("seconds in a day =", seconds_per_day)
floatdiv = seconds_per_day/seconds_per_hour
print("test float division = ", floatdiv)
intdiv = seconds_per_day//seconds_per_hour
print("test integer division =",intdiv)
